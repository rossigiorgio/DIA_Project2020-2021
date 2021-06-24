# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import numpy as np

class PricingEnv:
    
    def __init__(self):
        with open('/pricing_config.json') as json_file:
            data = json.load(json_file)
        self.name=data["product"][0]["name"]
        self.features=data["product"][0]["features"]
        self.classes=data["product"][0]["classes"]
        self.prices=data["product"][0]["prices"]
        self.probabilities=data["product"][0]["probabilities"]
        
    def nextTimeProbability(month):
        return(month/(1+month))
    
    def costPerClick(bid):
        s= np.random.uniform(bid-0.05*bid, bid+0.05*bid,1)
        return(s)
        
        

with open('C:/Users/MorganaGiorgio/Project enviroment/pricing_config.json') as json_file:
    data = json.load(json_file)

print(data["product"][0]["probabilities"][1][0])
