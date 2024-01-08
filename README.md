# Sliding-Neural-Machine-alpha

# README for Sliding Neural Machine (SNM) Project

## Abstract
The Sliding Neural Machine (SNM) is an experimental project focused on exploring the capabilities of neural networks in simulating complex dynamical systems. It represents a novel approach in neural computing by combining the concepts of localized processing with dynamic, adaptive behavior. This project is in its alpha stage, embodying a blend of theoretical intuition and empirical exploration. It's essential to note that many of the ideas and claims made about the SNM are based on heuristic understanding and unproven hypotheses.

## Introduction
The SNM is an evolutionary step from the Convolutional Turing Machine (CTM), inspired by Lenia-like cellular automata and designed to demonstrate adaptive learning systems. Unlike the CTM, which updates the entire state space, the SNM focuses on updating only a specific part of the state space where the kernel is currently located. This project is the brainchild of Giacomo Bocchese, whose background in Machine Learning, AI, and Deep Learning, combined with an experimental approach to research, has shaped the development of this model.

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
