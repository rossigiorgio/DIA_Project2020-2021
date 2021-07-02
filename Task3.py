#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:25:45 2021

@author: amandaseger
"""
"Task 3"
import numpy as np
import matplotlib.pyplot as plt
from Pricing.Environment.PricingEnv import *
from Pricing.Learners.TS_Learner import *
from Pricing.Learners.UCB1 import *

#Fixed parameters: Bid
#Known parameters: Daily clicks, daily cost per click

def main():
    T = 365
    n_experiments = 150
    price_env = PricingEnv()
    arms_candidates = np.array(price_env.prices)
    n_arms = len(arms_candidates)
    prob = price_env.probabilities
    classes = price_env.classes
    
    #HELP: How do I get the converstion rates here?
    conv_rate = np.array([[1,2,3,4,5],
                          [1,2,3,4,5],
                          [1,2,3,4,5]])
    #Bid is fixed, 1 for every class?
    bid = np.array([[5],
                    [6], 
                    [7]])
    
    ts_reward_per_experiment = []
    ucb_reward_per_experiment = []
    
    #Learning simulation
    ts_learner = TS_Learner(n_arms = n_arms)
    ucb_learner = UCB1(n_arms = n_arms)
    ts_reward_per_experiment = []
    ucb_reward_per_experiment = []
    for t in range(0,T):
        #Thompson Sampling Learner
        pulled_arm1 = ts_learner.pull_arm()
        reward1 = price_env(pulled_arm1)
        ts_learner.update(pulled_arm1, reward1)
        
        #UCB1 Learner
        pulled_arm2 = ucb_learner.pull_arm()
        reward2 = price_env(pulled_arm2)
        ucb_learner.update(pulled_arm2, reward2)
        
    ts_reward_per_experiment.append(ts_reward_per_experiment)
    ucb_reward_per_experiment.append(ucb_reward_per_experiment)