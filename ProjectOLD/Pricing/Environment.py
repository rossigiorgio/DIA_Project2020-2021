#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:33:29 2021

@author: amandaseger
"""
import numpy as np

class Environment():
    def __init__(self, n_arms, probabilities):
        self.n_arms = n_arms
        self.probabilities = probabilities
        
    def round(self, pulled_arm):
        reward = np.random.bionomial(1, self.probabilities[pulled_arm])
        return reward
        