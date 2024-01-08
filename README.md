# Sliding-Neural-Machine-alpha


## Abstract
The Sliding Neural Machine (SNM) is an exploratory extension of the Convolutional Turing Machine (CTM), conceived with the goal of refining adaptive learning systems in computational models. Diverging from the CTM's approach of updating the entire state space, the SNM innovates by selectively updating only the region beneath its kernel. This targeted approach brings about a shift from the CTM's O(n) computational complexity (depending on the state space dimension n, number of cells in the state space grid) to a more efficient O(1) paradigm in the SNM, representing a significant stride in computational efficiency.

This O(1) dependence on the state space is crucial in reachingn (finite memory bounded) Turing Completeness and Universal Computation abilities, since we theoretically need infinite memory tape to model any possible function and algorithm with a turing machine. The O(1) dependence on "tape length" (that is the state space), assures that we can scale the SS dimension without affecting simulation speed (if enough RAM is given).

Central to this efficiency is the SNM's use of a neural network-based transformation for its kernel operations, as opposed to the convolution operations used in the CTM. This kernel network, which is trainable, drives the kernel and updates the region beneath it, adding a layer of adaptability and learning capability to the SNM's processing. Its mobile kernel, which autonomously moves in the state space, is driven by its internal processing. This mobility allows the SNM to execute computations and updates in specific zones of the state space as needed, enhancing the system's operational focus and efficiency. While inheriting the foundational features of the CTM, the current implementation of the SNM also includes the potential for first-order meta-learning emergence.

The SNM's capability for self-reprogramming its kernel, an ambitious feature aimed at achieving full meta-learning (different from first-order meta learning), is yet to be included in the current version. This feature, while yet ideated how, is yet to be coded and integrated into the model. It promises to enable the SNM to adapt its kernel autonomously, furthering its learning and evolutionary capabilities.

Currently, the SNM can be trained using a combination of Genetic Algorithms and advanced Reinforcement Learning techniques like policy gradient and Proximal Policy Optimization (PPO). This hybrid training approach is intended to optimize the model's learning effectiveness and adaptability. Once meta learning occours, learning would speed up dramaticaly and external optimizers can be removed (maybe kept only for stability reasons). This net will have continual learning and ability to self-improve at all computational levels (assuming enough state space memory).

It's important to emphasize that the SNM project, at this juncture, is highly experimental. *Some of the theoretical claims present in this description are not formally proved yet, many of them come from a kind of "rigorous deduction" and some intuition based on known concepts in deep learning and emergent systems*. The future steps outlined are exploratory in nature and aimed at gradually uncovering the potential and limitations of the model. As the project progresses, these steps will be critical in transitioning from heuristical concepts to tangible results and insights.


## Design and Operation
### Kernel Design
- The SNM features a shallow neural network kernel.
- It processes a 3x3 input area from the state space, with a hidden layer of 128 neurons, outputting a 3x3 grid.

### Kernel Movement
- The movement of the kernel is determined by the network's output activations.
- These activations dictate the direction of movement: up, down, left, right, or stay.

### State Space Update
- In each iteration, only the 3x3 area under the kernel is updated, reflecting the kernel's output.

### Iteration vs. Inference Steps
- **Iteration Step**: Involves the kernel processing its current 3x3 area, updating the state space, and then moving.
- **Inference Step**: A complete cycle starting from the kernel's initial position to the point where the halting state exceeds a threshold.

## Computational Complexity
- The operation of the SNM is \( O(1) \) in relation to the state space size, with each iteration step processing a fixed-size region.
- The duration of a complete inference step is not constant (\( O(1) \)) and can vary.

## Current Status and Limitations
As an alpha version project, the SNM is primarily an exploratory and experimental tool. Its development is grounded in heuristic reasoning and empirical methods, with several aspects yet to be rigorously tested or formally proven. The project is in the early stages of development, and while it shows promise, it should be approached with an understanding of its experimental nature.

### Limitations and Future Work
- **Experimental Nature**: Many features and claims about the SNM are based on intuition and are not yet empirically validated. This project is a conceptual exploration and should be viewed as a starting point for further research and development.
- **Unproven Claims**: Some of the theoretical claims and functionalities are based on hypotheses and require further investigation and validation.
- **Incomplete Functionalities**: As an alpha version, not all intended functionalities of the SNM are implemented. Future versions aim to expand on these capabilities.
- **Scalability and Efficiency**: While the SNM is designed to be scalable and efficient, these aspects need rigorous testing, especially in different application scenarios.
- **Application in Complex Systems**: The model's potential in simulating complex dynamical systems and pattern recognition tasks is a key area for future exploration.

## Contributing
Contributions to the SNM project are welcome. Interested researchers, students, and enthusiasts in the fields of neural computing, dynamical systems, and machine learning are encouraged to collaborate, test, and expand on the project. Whether it's refining the existing model, testing its hypotheses, or implementing new features, your input can help advance this exploratory tool.

## Citation
If you utilize the SNM in your research or projects, please acknowledge this work as follows:

```bibtex
@misc{snm2024,
  author = {Giacomo Bocchese},
  title = {Sliding Neural Machine: An Experimental Approach to Neural Computing},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/GiacomoBocchese/SNM}}
}
```

## Contact
For queries, suggestions, or collaborations, feel free to reach out. Your feedback and insights are valuable to the continuous improvement and evolution of the SNM project.
