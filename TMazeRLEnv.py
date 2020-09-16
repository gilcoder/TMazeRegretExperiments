import gym
from gym import spaces
from tmaze import TMaze
import numpy as np

class TMazeRLEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, main_len=10, right_len=3, left_len=3, rewards = None, max_steps = 0):
        super(TMazeRLEnv, self).__init__()
        self.action_space = spaces.Discrete(4) #forward, backward, right, left
        self.observation_space = spaces.Box(low=0, high=max(main_len, right_len, left_len), shape=(2,), dtype=np.uint32)
        self.maze = TMaze(main_len, right_len, left_len)
        self.right_len = right_len
        self.left_len = left_len
        self.max_steps = max_steps
        self.steps = 0
        self.done = False
        if rewards is None:
            self.rewards = {(1, 2): 4, (2, 2): -3}
        else:
            self.rewards = rewards
    
    def set_reward(self, pos, value):
        assert len(pos) == 2, 'pos must be a integer  array with at least two elements.'
        self.rewards[pos[0], pos[1]] = value
    
    def step(self, action):
        assert action >= 0 and action <= 4, "Action must be 0 (forward), 1 (backward), 2 (right), 3 (left) or 4 (NoOp)."
        r = 0
        pos1 = self.maze.get_position()
        if action == 0:
            self.maze.forward()
        elif action == 1:
            self.maze.backward()
        elif action == 2:
            self.maze.right()
        elif action == 3:
            self.maze.left()
        
        pos2 = self.maze.get_position()
        if pos1 == pos2:
            r += -1

        pk = self.maze.get_position()
        self.done = pk == (1, self.right_len-1) or pk == (2, self.left_len-1)

        if pk in self.rewards:
            r += self.rewards[pk]
    
        self.steps += 1
        if self.max_steps > 0 and self.steps >= self.max_steps:
            self.done = True
        return np.array(list(self.maze.get_position())), r, self.done, {}

    def render(self, mode='human'):
        print(self.maze.get_position())
    
    def reset(self):
        self.steps = 0
        self.done = False
        self.maze.reset()
        return np.array(list(self.maze.get_position()))

    def close(self):
        pass
