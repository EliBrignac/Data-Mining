import pandas as pd
import numpy as np
import math



df = pd.read_csv('HW5 - Sheet2.csv')

df = df[df['RATING'] == '4-star']
#print(df)


# Normal Tree No Pruining
def trace_tree(row):
    instances = row['#OF-INSTANCES']
    size = row['SIZE']
    sector = row['SECTOR']
    #turnover = row['TURNOVER']
    decision = row['DECISION?']

    if sector == 'Technology':
        if size == 'medium':
            correct = 1 if decision == 'REJECT' else 0
            return correct * instances
        elif size == 'small':
            correct = 1 if decision == 'REJECT' else 0
            return correct * instances
        elif size == 'large':
            correct = 1 if decision == 'INVEST' else 0
            return correct * instances

E = df.apply(trace_tree, axis=1).sum()
N = df['#OF-INSTANCES'].sum()
print("NO Pruning: ", E / N)
'''
-------------------------- Output ----------------------------
NO Pruning:  0.5769230769230769
--------------------------------------------------------------
this means that the accuracy of the tree is 57.69% without pruning
'''


'''
Suppose that you don’t have a pruning dataset and must instead rely on the training set for pruning.
Instead of the training set given earlier, suppose that the following training instances end up at the leaf nodes of
the rightmost SIZE subtree indicated by *** in the decision tree on the preceding page.

Data:

#-OF-INSTANCES, SIZE, SECTOR, RATING, DECISION?
17, large, Technology, 4-star, INVEST,
14 large Technology 4-star REJECT
15 medium Technology 4-star INVEST
22 medium Technology 4-star REJECT
4 small Technology 4-star INVEST
6 small Technology 4-star REJECT

Use pessimistic error pruning to determine whether to prune the node indicated by *** — use a confidence value
of 58%. Please show the details of your work. If you decide not to prune, explain why. If you decide to prune,
please explain why and draw the resulting decision tree.

'''
# Pessimistic Pruning
df = pd.read_csv('HW5 - Sheet2.csv')

small = 4/6
med = 15/22
large = 17/14
confidence = 0.58
Z = confidence/2 # Z = .29
Z = .81 # from table

#Small
E = 4/10
N = 10
equation_s = E + (math.pow(Z,2)/(2*N)) + Z * math.sqrt((E/N) - (math.pow(E,2)/N) + (math.pow(Z,2)/(4*math.pow(N,2))))
equation_s = equation_s / (1 + math.pow(Z,2)/N)
print("Pessimistic Pruning SMALL: ", equation_s)

#Med
E = 15/37
N = 37
equation_m = E + (math.pow(Z,2)/(2*N)) + Z * math.sqrt((E/N) - (math.pow(E,2)/N) + (math.pow(Z,2)/(4*math.pow(N,2))))
equation_m = equation_m / (1 + math.pow(Z,2)/N)
print("Pessimistic Pruning MED: ", equation_m)

#Large
E = 14/31
N = 31
equation_l = E + (math.pow(Z,2)/(2*N)) + Z * math.sqrt((E/N) - (math.pow(E,2)/N) + (math.pow(Z,2)/(4*math.pow(N,2))))
equation_l = equation_l / (1 + math.pow(Z,2)/N)
print("Pessimistic Pruning LARGE: ", equation_l)

weighted = (10/78) * (equation_s) + (37/78) * (equation_m) + (31/78) * (equation_l)

print("Weighted Pessimistic Pruning: ", weighted)

'''
-------------------------- Output ----------------------------
NO Pruning:  0.5769230769230769
Pessimistic Pruning SMALL:  0.5278730894016012
Pessimistic Pruning MED:  0.47188162736989114
Pessimistic Pruning LARGE:  0.5242673262337877
Weighted Pessimistic Pruning:  0.4998799771788385
--------------------------------------------------------------

We do NOT prune the tree

'''


