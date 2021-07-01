#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:07:39 2021

@author: amandaseger
"""
from Environment import Environment
import numpy as np


class Non_Stationary_Environment(Environment):
    def __init__(self, n_arms, probabilities, horizon):
        super().__init__(n_arms, probabilities)
        self.t = 0
        n_phases = len(self.probabilities)
        self.phase_size = horizon/n_phases

    def round(self, pulled_arm):
        current_phase = int(self.t / self.phase_size)
        p = self.probabilities[current_phase][pulled_arm]
        reward = np.random.binomial(1, p)
        self.t += 1
        return reward