#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:46:24 2021

@author: amandaseger
"""
from ProjectEnviroment.projectEnviroment import *
import numpy as np
from pricingEnviroment.Non_Stationary_Enviroment import *
from pricingEnviroment.TS_Learner import *
from pricingEnviroment.UCB1 import *
#from Learner import Learner
import matplotlib.pyplot as plt

context= contextEnv()
price=context.prices

print(price)

p=context.probabilities
c=np.zeros(10)
for i in range(0,9):
    c[i]=(p[0][i]+p[1][i]+p[2][i])/3

opt=np.max(c)

n_arms=10;
T=365
n_experiment=50

ts_rewards=[] #reward per gli esperimenti del ts algorithm
ucb1_rewards=[] #reward per gli esperimenti dell'algoritmo ucb1

totalRevenueTS=[]
totalRevenueUCB1=[]
dailyTS=0
dailyUCB1=0

cumRewardTS=0
cumRewardUCB1=0




nrClick=500



env = Non_Stationary_Enviroment(n_arms= n_arms, probabilities=c)
ts_learner= TS_Learner(n_arms=n_arms)
ucb1_learner= UCB1(n_arms= n_arms)

ts_daily_reward= []
ucb_daily_reward= []
for t in range (0,T):
    ts_daily_profits = 0
    ucb_daily_profits = 0
    for class in range(0,3)
    
        #pull TS arm
        pulled_armTS=ts_learner.pull_arm() #prendo l'arm
        
        #pull UCB1 arm
        pulled_armUCB1=ucb1_learner.pull_arm()
        
    #I pull a new arm every day, and i propose the same price to the same person
    
        for c in range(0, nrClick):
            #Thompson Sampling Learner
            
            reward= env.round(pulled_armTS) #calcolo il reward
            cumRewardTS+=reward
            dailyTS+=reward*price[pulled_armTS]
            
            
            #totalRevenueTS=totalRevenueTS.append(prezzi[pulled_arm])
            #ts_learner.update(pulled_arm, reward)
            
            
            #UCB1 Learner 
            
            reward=env.round(pulled_armUCB1)
            cumRewardUCB1+=reward
            dailyUCB1+=reward*price[pulled_armUCB1]
            #totalRevenueUCB1=totalRevenueUCB1.append(prezzi[pulled_arm])
            #ucb1_learner.update(pulled_arm, reward)
            
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
    
    
    #make the average of the cumulative reward 
    totalRevenueTS.append(dailyTS)
    totalRevenueUCB1.append(dailyUCB1)
    ts_rewards.append(cumRewardTS/nrClick)
    ucb1_rewards.append(cumRewardUCB1/nrClick)
    #print(totalRevenueTS[t])
    #print(totalRevenueUCB1[t])
    ts_learner.update(pulled_armTS,cumRewardTS/nrClick)
    ucb1_learner.update(pulled_armUCB1, cumRewardUCB1/nrClick)
    dailyTS=0
    dailyUCB1=0
    cumRewardTS=0
    cumRewardUCB1=0







plt.figure(0)
plt.xlabel("t")
plt.ylabel("Revenue")
plt.plot(np.cumsum(totalRevenueTS, axis=0), 'r')
plt.plot(np.cumsum(totalRevenueUCB1, axis=0), 'b')
plt.legend(["TS", "UCB1"])



plt.figure(1)
plt.xlabel("t")
plt.ylabel("Regret")
plt.plot(np.cumsum(opt-ts_rewards, axis=0), 'r')
plt.plot(np.cumsum(opt-ucb1_rewards, axis=0), 'b')
plt.legend(["TS", "UCB1"])

plt.show()