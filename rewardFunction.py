# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:00:10 2018

@author: zmoran
"""

import pandas as pd

data = pd.read_csv('afl.csv', encoding = "ISO-8859-1",header=1)

homeWin = []

scores = data.iloc[:,5:7].values

for i in range(len(scores)):
    homeWin.append(scores[i][0] > scores[i][1])
  
    
# 0 = away bet
# 1 = home bet
# 2 = no bet

    
action1 = [[1,2,0,10],[2,2,2,0],[2,1,2,5]]

exampleRow = [1.3,2.5,1.1,2.2,2.1,3.4]

gameResults = [1,0,0]

def reward(action,row,results):
    reward = 1
    for multi in action:
        success = True
        if multi[3]==0:
            continue
        for i in range(len(action)):
            if multi[i]==2:
                continue
            if multi[i]!=results[i]:
                success = False
        if success:
            for j in range(len(multi)):
                if (j == len(action) and multi[j]) != 0:
                    reward *= multi[j]
                elif multi[j] == 0:
                    reward *= row[j*2+1]
                elif multi[j] == 1:
                    reward *= row[j*2]
        
    if reward == 1:
        return 0               
    return reward

print(reward(action1,exampleRow,gameResults))
                