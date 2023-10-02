import pandas as pd
import numpy as np
import math

df = pd.read_csv('HW4 - Sheet1.csv')
df = df.drop(columns=['SIZE'])
#print(df)
'''
Calculate the GINI index for the initial dataset

LaTeX formula for Gini Index
Gini(S) = 1 - \sum_{i=1}^{n} p_i^2

'''
def calculate_gini(data):
    total_samples = len(data)
    if total_samples == 0:
        return 0
    
    counts = data['TAKE-HOME'].value_counts()
    p0 = counts.get('no', 0) / total_samples
    p1 = counts.get('yes', 0) / total_samples
    gini = 1 - (p0**2 + p1**2)
    return gini

initial_gini = calculate_gini(df)

attributes = df.columns[:-1]  # Exclude the 'TAKE-HOME' column
best_attribute = None
best_gini_reduction = 0

'''
NOTICE -- We don't have to do every permutation of attributes because 
           we are only looking at SHOTS and HAIR

This does 

δGini_A(S) = Gini(S) - Gini_A(S)

Gini_A(S) = Sj/S * Gini(Sj) + Sk/S * Gini(Sk)
'''
#print("att", attributes)
all_gini = {}
for attribute in attributes:
    unique_values = df[attribute].unique()
    giniA = 0
    
    for value in unique_values:
        subset = df[df[attribute] == value]
        #print(subset)
        #print('\n')
        weight = len(subset) / len(df)
        giniJ = calculate_gini(subset)
        giniA += weight * giniJ

    gini_reduction = initial_gini - giniA
    all_gini[attribute] = round(gini_reduction,3)
    if gini_reduction > best_gini_reduction:
        best_gini_reduction = gini_reduction
        best_attribute = attribute

print("Best Attribute to Split:", best_attribute)
print("GINI Reduction:", round(best_gini_reduction,3))
print("All GINI Reductions:", all_gini)


'''
File Output

Best Attribute to Split: HAIR
GINI Reduction: 0.163
All GINI Reductions: {'SHOTS': 0.137, 'HAIR': 0.163}

Considering the HAIR attribute has the highest score, we will split on that.
'''
