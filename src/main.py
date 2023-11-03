import gym
from gym import spaces
import numpy as np

class RobotPathPlanningEnv(gym.Env):
    def __init__(self):
        super(RobotPathPlanningEnv, self).__init__()
        
        # Define action and state spaces
        self.action_space = spaces.Discrete(4)  # Forward, Left, Right, Stop
        self.observation_space = spaces.Box(low=0, high=100, shape=(10, 10), dtype=int)  # 10x10 grid

        # Define robot, target, and obstacle positions
        self.robot_pos = [0, 0]
        self.target_pos = [9, 9]
        self.obstacles = [[5, 5], [6, 6]]  # Example obstacles

    def step(self, action):
        """
        Execute the given action and return the new state, reward, done and info.
        """
        # Update robot position based on action
        if action == 0:  # Forward
            self.robot_pos[1] += 1
        elif action == 1:  # Left
            self.robot_pos[0] -= 1
        elif action == 2:  # Right
            self.robot_pos[0] += 1
        elif action == 3:  # Stop
            pass  # No movement
        
        # Check for collisions with obstacles
        if self.robot_pos in self.obstacles:
            reward = -10
            done = True
            return self.get_state(), reward, done, {}

        # Check if target reached
        if self.robot_pos == self.target_pos:
            reward = 10
            done = True
            return self.get_state(), reward, done, {}

        # Otherwise, provide a negative reward for each step taken
        reward = -1
        done = False
        return self.get_state(), reward, done, {}

    def reset(self):
        """
        Reset the environment to its initial state and return the initial state.
        """
        self.robot_pos = [0, 0]
        return self.get_state()

    def render(self, mode='human'):
        """
        Render the environment.
        """
        grid = np.zeros((10, 10))
        grid[tuple(self.robot_pos)] = 1  # Mark robot position
        grid[tuple(self.target_pos)] = 2  # Mark target position
        for obstacle in self.obstacles:
            grid[tuple(obstacle)] = -1  # Mark obstacles

        print(grid)  # Simple text rendering

    def get_state(self):
        """
        Construct the state from the robot position, target position, and obstacle positions.
        """
        state = {
            'robot_pos': self.robot_pos,
            'target_pos': self.target_pos,
            'obstacles': self.obstacles
        }
        return state

# Usage:
env = RobotPathPlanningEnv()
