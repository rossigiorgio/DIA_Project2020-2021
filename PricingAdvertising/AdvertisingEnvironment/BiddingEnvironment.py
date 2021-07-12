#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:58:05 2021

@author: amandaseger
"""
#time horizon: 60 days
#Fixed daily budget
# 20 possible bids
#since we have fixed daily budget, the optimal bid is not necessary the one the higher value 

import numpy as np

def fun(x):
    return 100 * (1.0 - np.exp(-4*x+3*x**3)) #the function maps the bid corresponding the number of clicks

class BiddingEnvironment():
    def __init__(self, bids, sigma): #array of possible bids and (sigma) standard deviation of the reward function and we assume.
        self.bids = bids
        self.means = fun(bids) #mean of reward function
        self.sigmas = np.ones(len(bids)) * sigma

    def round(self, pulled_arm):
        reward = np.random.normal(self.means[pulled_arm], self.sigmas[pulled_arm], 1)
        return reward