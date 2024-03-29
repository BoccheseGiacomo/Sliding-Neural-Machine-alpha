import numpy as np
import matplotlib.pyplot as plt
import scipy
import time
from scipy import optimize
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import torch
import torch.nn as nn
import torch.nn.functional as F

class KernelNetwork(nn.Module):
    def __init__(self):
        super(KernelNetwork, self).__init__()
        # Define the layers
        self.fc1 = nn.Linear(9, 32)  # Input layer
        self.fc2 = nn.Linear(32, 9)  # Output layer

        # Custom weight initialization
        self.init_weights()

    def init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                # Initialize weights to a higher value, e.g., using a uniform distribution
                nn.init.normal_(m.weight, mean=0, std=0.3)

    def forward(self, x):
        # Flatten the input 3x3 grid
        x = x.view(-1, 9)
        # Apply layers
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        # Reshape output to 3x3 grid
        x = x.view(-1, 3, 3)
        return x
    
class SNM:
    def __init__(self):
        # Configurations
        self.dim = (20, 20)
        self.max_steps = 200  # Maximum number of steps in the simulation
        self.kernel_net=KernelNetwork()
        self.kernel_pos=(1,1)
        self.state = np.zeros(self.dim)  # Initialize the state grid
        self.halting_threshold = 0.7
        self.dt=0.1
        self.time_idx=0

        self.state_history=[]

        # Significant cells
        self.input_indexes = [(3, 0), (6, 0)]
        self.output_indexes = [(3, 19), (6, 19)]
        self.halting_index = (10, 19)
        self.reward_index = (15, 19)

    def set_input(self,input_values):
        for idx, value in zip(self.input_indexes, input_values):
            self.state[idx] = value

    def set_reward(self,reward):
        self.state[self.reward_index] = reward

    def get_output(self):
        return [self.state[idx] for idx in self.output_indexes]
    
    def get_halting(self):
        return self.state[self.halting_index]
    
    def reset_halting(self):
        # Reset the halting cell
        self.state[self.halting_index] = 0

        # Define the halving kernel
        halving_kernel = np.array([[0.3, 0.3, 0.3],
                                   [0.3, 0.0, 0.3],
                                   [0.3, 0.3, 0.3]])

        # Get the coordinates of the halting cell
        y, x = self.halting_index

        # Determine the slicing bounds, ensuring they are within the grid boundaries
        y_start, y_end = max(y - 1, 0), min(y + 2, self.dim[0])
        x_start, x_end = max(x - 1, 0), min(x + 2, self.dim[1])

        # Adjust the kernel size if slicing bounds are at the edges
        kernel_y_start, kernel_x_start = max(1 - y, 0), max(1 - x, 0)
        kernel_y_end, kernel_x_end = 3 - max(y + 2 - self.dim[0], 0), 3 - max(x + 2 - self.dim[1], 0)

        # Apply the halving kernel to the surrounding cells
        self.state[y_start:y_end, x_start:x_end] *= halving_kernel[kernel_y_start:kernel_y_end, kernel_x_start:kernel_x_end]


    def reset_recording(self):
        self.state_history=[]

    def save_state(self):
        self.state_history.append(self.state.copy())

    
    def step_kernel(self):
        # Get current kernel position
        y,x = self.kernel_pos

        # Extract the current 3x3 region
        kernel_region = self.state[y-1:y+2, x-1:x+2]

        # Convert to PyTorch tensor and process through the kernel network
        kernel_input = torch.tensor(kernel_region, dtype=torch.float32).unsqueeze(0)
        kernel_output = self.kernel_net(kernel_input).squeeze(0).detach() #warning: maybe needed to modify "detach" for RL

        # Assuming the mapping: 'u' (1), 'd' (7), 'l' (3), 'r' (5), 's' (4)
        movement_indices = torch.tensor([1, 7, 3, 5, 4])
        movement_values = kernel_output.flatten()[movement_indices]

        # Apply softmax to get movement probabilities
        movement_probabilities = F.softmax(movement_values, dim=0).numpy()

        # Movement directions corresponding to indices
        directions = ['u', 'd', 'l', 'r', 's']
        movement = np.random.choice(directions, p=movement_probabilities)

        # Update kernel position based on selected movement
        if movement == 'u' and y > 1:
            y -= 1
        elif movement == 'd' and y < self.dim[0] - 2:
            y += 1
        elif movement == 'l' and x > 1:
            x -= 1
        elif movement == 'r' and x < self.dim[1] - 2:
            x += 1
        # No movement for 's'

        self.kernel_pos = (y, x)

        # Update the state space with the output of the kernel
        self.state[y-1:y+2, x-1:x+2] = kernel_output.numpy()


    def forward(self, input_values, reward):
            if len(input_values) != len(self.input_indexes):
                raise ValueError("Input values size does not match input indexes size.")

            #reset halting
            self.reset_halting()

        
            for step in range(self.max_steps):
                
                self.set_input(input_values)
                self.set_reward(reward)

                # Add the current state
                self.save_state()

                # Apply convolution with edge padding
                self.step_kernel()

                # Check halting condition
                if self.get_halting() >= self.halting_threshold:
                    self.save_state()
                    break

            # Retrieve output values
            outputs = self.get_output()
            
            return outputs
    
    def visualize(self):
        # Set up the figure for animation
        fig, ax = plt.subplots()
        ims = []

        for state in self.state_history:
            # Create the heatmap from the state
            im = ax.imshow(state, animated=True, cmap='jet', vmin=-1, vmax=1)

            # Function to draw border around a cell
            def draw_border(y, x, color):
                rect = plt.Rectangle((x-0.5, y-0.5), 1, 1, fill=False, edgecolor=color, lw=4)
                ax.add_patch(rect)

            # Draw borders around the special cells
            for y, x in self.input_indexes:
                draw_border(y, x, 'green')  # Green for input
            for y, x in self.output_indexes:
                draw_border(y, x, 'blue')  # Blue for output
            y, x = self.halting_index
            draw_border(y, x, 'red')  # Red for halting
            y, x = self.reward_index
            draw_border(y, x, 'orange')  # Orange for reward

            ims.append([im])

        # Create the animation
        ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True)

        # Add a colorbar
        fig.colorbar(im, ax=ax)

        # Save the animation to a file
        ani.save('simulation.mp4', writer='ffmpeg')

        # Close the plot to prevent it from displaying inline or in a new window
        plt.close(fig)

    def visualize2(self): #for visualizing also the kernel, not implemented yet
        # Set up the figure for animation
        fig, ax = plt.subplots()
        ims = []

        for state in self.state_history:
            # Create the heatmap from the state
            im = ax.imshow(state, animated=True, cmap='jet', vmin=-1, vmax=1)

            # Function to draw a large square around the kernel
            def draw_kernel_border(y, x, color, width=2):
                # Draw a square border of 3x3 around the kernel's center
                rect = plt.Rectangle((x-1, y-1), 3, 3, fill=False, edgecolor=color, lw=width)
                ax.add_patch(rect)

            # Draw borders around the special cells
            for y, x in self.input_indexes:
                draw_kernel_border(y, x, 'green')  # Green for input
            for y, x in self.output_indexes:
                draw_kernel_border(y, x, 'blue')  # Blue for output
            y, x = self.halting_index
            draw_kernel_border(y, x, 'red')  # Red for halting
            y, x = self.reward_index
            draw_kernel_border(y, x, 'orange')  # Orange for reward

            # Get the kernel's current position and draw the border
            kernel_y, kernel_x = self.kernel_pos
            draw_kernel_border(kernel_y, kernel_x, 'white')

            ims.append([im])

        # Create the animation
        ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True)

        # Add a colorbar
        fig.colorbar(im, ax=ax)

        # Save the animation to a file
        ani.save('simulation.mp4', writer='ffmpeg')

        # Close the plot to prevent it from displaying inline or in a new window
        plt.close(fig)