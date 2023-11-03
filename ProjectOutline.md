# CS 4180/5180: Reinforcement Learning and Sequential Decision Making (Fall 2023)
## Final Project Proposal: Adaptive Robot Path Planning

**Team Member**: Puja Chaudhury

### Problem Description
The primary focus of this project is on Adaptive Robot Path Planning, which involves developing a strategy for navigating a robot through a dynamic environment with moving obstacles to reach a designated target point.

### Problem Formulation

**Objective**: To develop a reinforcement learning model that navigates a robot from a starting position to a target position while dynamically avoiding obstacles.

**State Space**: Includes the robot's current position, orientation, and sensor data.

**Action Space**: Consists of movements such as moving forward, turning left or right, and stopping.

**Reward Function**: Defined to give positive rewards for moving closer to the target and negative rewards for colliding with obstacles or moving away from the target.

**Ideal Outcome**: A model that can efficiently guide a robot to a target in dynamic environments, with an evaluation of two algorithms for their computational and path efficiency trade-offs.

### Algorithms

- **Q-Learning** (Baseline)
- **Advantage Actor-Critic (A3C)** (Advanced)

### Learning and Tools

**Topics to Learn**:
- Deep understanding of Q-Learning and A3C.
- Working knowledge of ROS (Robot Operating System).

**Libraries**:
- TensorFlow/PyTorch for reinforcement learning.
- ROS for robot simulation.

**References**:
- *Reinforcement Learning: An Introduction* by Richard S. Sutton and Andrew G. Barto.
- ROS Documentation.
- Research papers on A3C.

### Domain and Simulator

The project will utilize ROS to simulate the robot's environment, which will generate simulated sensor data for training the reinforcement learning model. No new simulator will be developed.

### Week-by-Week Plan

#### Week 1 (Nov 2 - Nov 8)
- **Task**: Problem formulation, literature review, and initial setup.
- **Deliverable**: A well-defined problem statement and a list of references.

#### Week 2 (Nov 9 - Nov 15)
- **Task**: Set up the ROS environment and TensorFlow/PyTorch.
- **Deliverable**: A running ROS simulation and a basic RL environment.

#### Week 3 (Nov 16 - Nov 22)
- **Task**: Implement and train the Q-Learning model.
- **Deliverable**: A trained Q-Learning model with initial results.

#### Week 4 (Nov 23 - Nov 29)
- **Task**: Implement and train the A3C model.
- **Deliverable**: A trained A3C model and comparative results.

#### Week 5 (Nov 30 - Dec 4)
- **Task**: Final evaluations, bug fixes, and preparations for presentation.
- **Deliverable**: Final results and preparation of presentation materials.

#### December 5: Final Presentation
- Present the project, focusing on the problem, algorithms, results, and learnings.

### Submission
- [x] November 1: Proposal Submission
