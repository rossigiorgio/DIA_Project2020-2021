#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:17:00 2021

@author: amandaseger
"""
import numpy as np
class Learner:
    def __init__(self,n_arms):
        self.n_arms = n_arms
        self.t = 0
        self.rewards_per_arm = [[] for i in range(n_arms)]
        self.collected_rewards = np.array([])
        
    def pull_arm(self):
        pass

    def update_observations(self, pulled_arm, reward):
        self.rewards_per_arm[pulled_arm].append(reward)
        self.collected_rewards = np.append(self.collected_rewards,reward)