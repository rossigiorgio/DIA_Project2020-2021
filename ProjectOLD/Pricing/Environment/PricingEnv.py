# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import numpy as np

class PricingEnv():
    
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
        
    def conversionRateFunctionMale(price):
        rate=0.0001*(price)^3-0.0072*(price)^2+0.0842*price +0.3294
        return rate
    
    def conversionRateFunctionFelameA(price):
        rate= 0.0001*(price)^3-0.0053*(price)^2+0.0988*price+0.1855
        return rate
    
    def conversionRateFunctionFemaleY(price):
        rate=0.0001*(price)^3-0.0074*(price)^2+0.0804*price+0.3241
        return rate
        

with open('C:/Users/MorganaGiorgio/Project enviroment/pricing_config.json') as json_file:
    data = json.load(json_file)

print(data["product"][0]["probabilities"][1][0])
