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
    conv_rate = price_env.probabilities
    classes = price_env.classes
    costPerClick = ....
    n = ...
    
    #HELP: How do I get the converstion rates here?
    #conv_rate = np.array([[1,2,3,4,5],
                          #[1,2,3,4,5],
                          #[1,2,3,4,5]])
    #Bid is fixed, 1 for every class?
    bid = np.array([[5],
                    [6], 
                    [7]])
    
    ts_reward_per_experiment = []
    ucb_reward_per_experiment = []
    #Learning simulation
    ts_learner = TS_Learner(n_arms = n_arms)
    ucb_learner = UCB1(n_arms = n_arms)
    
    ts_daily_reward= []
    ucb_daily_reward= []
    
    ucb_reward_per_experiment = []
    for t in range(0,T):
        ts_daily_profits = 0
        ucb_daily_profits = 0
        #Revenue function
        for c in range(0,3): #Classes
        #Thompson Sampling Learner
            ts_pulled_arm = ts_learner.pull_arm()
            ts_reward = price_env(ts_pulled_arm)
            ts_learner.update(ts_pulled_arm, ts_reward)
            
            #Revenue function
            ts_class_profit = (t*conv_rate[ts_pulled_arm]*price-costPerClick)*n
            
            #UCB1 Learner
            ucb_pulled_arm = ucb_learner.pull_arm()
            ucb_reward = price_env(ucb_pulled_arm)
            ucb_learner.update(ucb_pulled_arm, ucb_reward)
            
            #Revenue function
            ucb_class_profit = (t*conv_rate[ucb_pulled_arm]*price-costPerClick)*n
            
            ts_daily_profits += ts_class_profit
            ucb_daily_profits += usb_class_profit
            
        ts_daily_reward.append(ts_daily_profits)
        ucb_daily_reward.append(ucb_daily_profits)
        
    #ts_reward_per_experiment.append(ts_)
    #ucb_reward_per_experiment.append(ucb_reward_per_experiment)
    
    

            

    

    