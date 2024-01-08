# Sliding-Neural-Machine-alpha


## Abstract
The Sliding Neural Machine (SNM) is an exploratory extension of the Convolutional Turing Machine (CTM), conceived with the goal of refining adaptive learning systems in computational models. Diverging from the CTM's approach of updating the entire state space, the SNM innovates by selectively updating only the region beneath its kernel. This targeted approach brings about a shift from the CTM's O(n) computational complexity (depending on the state space dimension n, number of cells in the state space grid) to a more efficient O(1) paradigm in the SNM, representing a significant stride in computational efficiency.

This O(1) dependence on the state space is crucial in reaching (finite memory bounded) Turing Completeness, since we theoretically need an infinite memory tape to model any possible function and algorithm with a turing machine. The O(1) dependence on "tape length" (that is the state space), assures that we can scale the state space dimension without affecting simulation speed (if enough RAM is given).
The model also embeds "Adaptive Computation Time", that is a fundamental feature for allowing Turing Completeness since it allows for looping operations.

Central to this efficiency is the SNM's use of a neural network-based transformation for its kernel operations, as opposed to the convolution operations used in the CTM. This kernel network, which is trainable, drives the kernel and updates the region beneath it, adding a layer of adaptability and learning capability to the SNM's processing. Its mobile kernel, which autonomously moves in the state space, is driven by its internal processing. This mobility allows the SNM to execute computations and updates in specific zones of the state space as needed, enhancing the system's operational focus and efficiency. The current implementation of the SNM also includes the potential for first-order meta-learning emergence (see the CTM for better understanding).

The SNM's capability for self-reprogramming its kernel, an ambitious feature aimed at achieving full meta-learning (different from first-order meta learning), is yet to be included in the current version. This feature, while yet ideated how, is yet to be coded and integrated into the model. It promises to enable the SNM to adapt its kernel autonomously, furthering its learning and evolutionary capabilities.

Currently, the SNM can be trained using a combination of Genetic Algorithms and advanced Reinforcement Learning techniques like policy gradient and Proximal Policy Optimization (PPO). This hybrid training approach is intended to optimize the model's learning effectiveness and adaptability. *not experimented yet, but true in theory:* Once meta learning occours, learning would speed up dramaticaly and external optimizers can be removed (maybe kept only for stability reasons). This net will have continual learning and ability to self-improve at all computational levels (assuming enough state space memory).

It's important to emphasize that the SNM project, at this juncture, is highly experimental. *Some of the theoretical claims present in this description are not formally proved yet, many of them come from "rigorous deduction" unified with some intuition based on known concepts in deep learning and emergent systems*. The future steps outlined are exploratory in nature and aimed at gradually uncovering the potential and limitations of the model. As the project progresses, these steps will be critical in transitioning from heuristical concepts to tangible results and insights.
The project is in the early stages of development, and while it shows promise, it should be approached with an understanding of its experimental nature.


## Design and Operation


### State space, input, ouptut and reward encoding:
- These features are identical to the CTM, please refer to the link for better understanding. [link].
  
### Kernel Design
- The SNM features a shallow neural network kernel.
- It processes a 3x3 (changeable) input area from the state space, with a hidden layer of 128 neurons, outputting a 3x3 grid.
- It's yet to be understood what is the minimum dimension of the kernel in order to allow the network to have the desired features, but since information and processing capabilities can be encoded on the full state space rather then on the kernel capabilities, we think a very small kernel is enough.

### Kernel Movement
- The movement of the kernel is determined by the network's output activations.
- Some of these activations determine the probabilities of moving: up, down, left, right, or stay. Then they are sampled and the kernel reaches a new position, and so on.

### State Space Update
- In each iteration, only the 3x3 area under the kernel is updated, reflecting the kernel's output.

### Flow control and halting: Adaptive Computation Time
- The systems implements a halting cell in the state space. This cell adds the feature of Adaptive Computation Time.
- Adaptive computation time gives a flow control ability to the model, allowing for performing more or less steps depending on the task complexity.
- This allows for (bounded memory) Turing Completeness, since it allows to perform loop operations that are foundamental for modeling recursive processes, without them it's impossible to reach TC.
- When the halting cell value exceeds a threshold, computation is stopped, outputs are retrieved and we go to the next input.

### Iteration vs. Inference Steps
- **Iteration Step**: Involves the kernel processing its current 3x3 area, updating the state space, and then moving.
- **Inference Step**: A complete cycle starting from the kernel's initial position to the point where the halting state exceeds a threshold.

## Computational Complexity
- The operation of the SNM is O(1) in relation to the state space size, with each iteration step processing a fixed-size region.
- The duration of a complete inference step is not a constant O(1) and can vary, depending on the task complexity since it self adapts (it would be always greater than O(1)).

### Note for users
*In the current version only inference is implemented, training procedure is yet to be coded.*

## Contributing
Contributions to the SNM project are welcome. Interested researchers, students, and enthusiasts in the fields of neural computing, dynamical systems, and machine learning are encouraged to collaborate, test, and expand on the project. Whether it's refining the existing model, testing its hypotheses, or implementing new features, your input can help advance this exploratory tool.

## Citation
If you utilize the SNM in your research or projects, please acknowledge this work as follows:

```bibtex
@misc{snm2024,
  author = {Giacomo Bocchese},
  title = {Sliding Neural Machine: An efficient emergent model architecture},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/GiacomoBocchese/SNM}}
}
```

## Contact
For queries, suggestions, or collaborations, feel free to reach out. Your feedback and insights are valuable to the continuous improvement and evolution of the SNM project.
