import pandas as pd
import numpy as np
import math



df = pd.read_csv('HW5 - Sheet1.csv')

df = df[df['RATING'] == '4-star']
print(df)

# Normal Tree No Pruining
def trace_tree(row):
    size = row['SIZE']
    sector = row['SECTOR']
    turnover = row['TURNOVER']
    decision = row['DECISION?']

    if sector == 'Commodity':
        if turnover == 'very-high':
            correct = 1 if decision == 'INVEST' else 0
            return correct
        elif turnover == 'high':
            correct = 1 if decision == 'INVEST' else 0
            return correct
        elif turnover == 'good':
            correct = 1 if decision == 'REJECT' else 0
            return correct
        elif turnover == 'low':
            correct = 1 if decision == 'REJECT' else 0
            return correct
    elif sector == 'Chemical':
        correct = 1 if decision == 'REJECT' else 0
        return correct
    elif sector == 'Technology':
        if size == 'medium':
            correct = 1 if decision == 'REJECT' else 0
            return correct
        elif size == 'small':
            correct = 1 if decision == 'REJECT' else 0
            return correct
        elif size == 'large':
            correct = 1 if decision == 'INVEST' else 0
            return correct
    elif sector == 'Health':
        correct = 1 if decision == 'MAYBE' else 0
        return correct

result = df.apply(trace_tree, axis=1).sum()
print("NO Pruning: ",result / len(df))
'''
-------------------------- Output ----------------------------
NO Pruning:  0.5909090909090909
--------------------------------------------------------------
this means that the accuracy of the tree is 59.09% without pruning
'''

# Pruned to Rating
def prune_to_rating(row):
    size = row['SIZE']
    sector = row['SECTOR']
    turnover = row['TURNOVER']
    decision = row['DECISION?']

    correct = 1 if decision == 'INVEST' else 0
    return correct


result = df.apply(trace_tree, axis=1).sum()
print("Pruned: ",result / len(df))
'''
-------------------------- Output ----------------------------
Pruned:  0.5909090909090909
--------------------------------------------------------------
This means that the accuracy of the tree is 59.09% after pruning to rating.
Because this accuracy is the same as when we didn't prune to rating, 
we can prune to rating based on Reduced Error Pruning.
'''