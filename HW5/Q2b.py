import pandas as pd
import numpy as np
import math


df = pd.read_csv('HW5 - Sheet3.csv')
df = df[df['LOCATION'] == 'city']

filtered_df = df[(df['LOCATION'] == 'city') & ((df['CONDITION'] == 'OK') | (df['CONDITION'] == ' '))]
total_instances = len(filtered_df)
#print(filtered_df)

decision_counts = filtered_df['DECISION'].value_counts()
#print(decision_counts)

only_ok = df[(df['LOCATION'] == 'city') & (df['CONDITION'] == 'OK')]
total_ok = len(only_ok)
ok_counts = only_ok['DECISION'].value_counts()
#print(ok_counts)

max_decision_counts = decision_counts[decision_counts == decision_counts.max()]

maxes = {}
for decision_label, decision_count in max_decision_counts.items():
    maxes[decision_label] =  decision_count
print("Max values assuming unknown instances: ",maxes)

ok_maxes = {}
max_ok_counts = ok_counts[ok_counts == ok_counts.max()]
for ok_label, ok_count in max_ok_counts.items():
    ok_maxes[ok_label] = ok_count
print("Max values NOT assuming unknown instances: ",ok_maxes)

def find_best_value(maxes, ok_maxes):
    if len(maxes) == 1:
        return list(maxes.keys())[0]
    for i in maxes:
        if i in ok_maxes:
            return i
    return None

print(f"Best value is {find_best_value(maxes, ok_maxes)}")

'''
-------------------------OUTPUT-------------------------
Max values assuming unknown instances:  {'BUY': 3, 'NO': 3}
Max values NOT assuming unknown instances:  {'BUY': 2, 'MAYBE': 2}
Best value is BUY
--------------------------------------------------------

We choose BUY for this leaf because if we take into consideration
the unknown instances, we have 3 BUY instances and 3 NO instances.
We choose BUY over NO because we are certain that there is 2 BUY instances,
but we are not certain that there are 2 NO instances.

This means we are more confident in BUY than NO, so we choose BUY.
'''
