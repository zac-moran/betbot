# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:00:10 2018

@author: zmoran
"""

import pandas as pd
import random as r

data = pd.read_csv('afl.csv', encoding = "ISO-8859-1",header=1)

homeWin = []

scores = data.iloc[:,5:7].values

odds = data.iloc[:,12:14].values

for i in range(len(scores)):
    homeWin.append(scores[i][0] > scores[i][1])

flatOdds = []
holdOdds = []

realResults = []
holdresults = []
action = []
actions = []


for j in range(207):
    holdOdds = []
    holdresults =  []
    action = []
    for i in range(9):
        holdOdds.append(odds[i][0])
        holdOdds.append(odds[i][1])
        holdresults.append(int(homeWin[i]))
        action.append([r.randint(0,2),r.randint(0,2),r.randint(0,2),r.randint(0,100)])
    flatOdds.append(holdOdds)
    realResults.append(holdresults)
    actions.append(action)
    
  
    
# 0 = away bet
# 1 = home bet
# 2 = no bet
    
# 207 rounds of 9
    


    

def reward(action,row,results):
    reward = 1
    for multi in action:
        success = True
        if multi[3]==0:
            continue
        for i in range(3):
            if multi[i]==2:
                continue
            if multi[i]!=results[i]:
                success = False
        if success:
            for j in range(len(multi)):
                if j == len(action) and multi[j] != 0:
                    reward *= multi[j]
                elif multi[j] == 0:
                    reward *= row[j*2+1]
                elif multi[j] == 1:
                    reward *= row[j*2]
        
    if reward == 1:
        return 0               
    return reward

def investment(action):
    inv = 0
    for multi in action:
        inv += multi[3]
    return inv

def difference(inv,ret):
    return ret-inv

print(reward(actions[0],flatOdds[0],realResults[0]))

print(investment(actions[0]))

print("")

print(difference(investment(actions[0]),reward(actions[0],flatOdds[0],realResults[0])))

















                