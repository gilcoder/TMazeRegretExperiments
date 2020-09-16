# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 09:30:45 2020

@author: gilza
"""
import gym
from gym.envs.registration import register

from TMazeRLEnv import TMazeRLEnv
if "TMazeRLEnv-v0" in gym.envs.registration.registry.env_specs:
    del gym.envs.registration.registry.env_specs["TMazeRLEnv-v0"]
register(id="TMazeRLEnv-v0", entry_point=TMazeRLEnv, max_episode_steps=1000000, reward_threshold=30.0)

