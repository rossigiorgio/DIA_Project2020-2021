#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:33:18 2021

@author: amandaseger
"""
from Learner import *
import numpy as np

class TS_Learner(Learner):
    def __init__(self,n_arms):
        super().__init__(n_arms)
        self.beta_parameters = np.ones((n_arms,2)) #Equal to the number of arms times 2

    #TS algorithm selects the arm to pull by samplinga value for each arm from a Beta distribution
    #selects the arm that is associated to the Beta distribution that generated this sample with maximum value
    #--> argmax
    def pull_arm(self):
        idx =  np.argmax(np.random.beta(self.beta_parameters[:,0],self.beta_parameters[:,1]))
        return idx
    #Update 
    def update(self, pulled_arm, reward):
        '''
        Update the beta parameters each time a reward is observed
        '''
        self.t += 1
        self.update_observations(pulled_arm,reward)
        self.beta_parameters[pulled_arm, 0] = self.beta_parameters[pulled_arm,0] + reward
        self.beta_parameters[pulled_arm, 1] = self.beta_parameters[pulled_arm,1] + 1.0 - reward
    