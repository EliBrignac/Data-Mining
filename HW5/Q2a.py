import pandas as pd
import numpy as np
import math



df = pd.read_csv('HW5 - Sheet3.csv')

# ASSUMPTION: The empty rows are also instances with CONDITION=good
df['CONDITION'].replace(' ', 'good', inplace=True)


filtered_df = df[(df['LOCATION'] == 'city') & (df['CONDITION'] == 'good')]
total_instances = len(filtered_df)
#total_instances += 3 # Assume the the empty rows are also instances

kind_counts = filtered_df['KIND'].value_counts()
#kind_counts += 3
for i in range(len(kind_counts)):
    print(f'P({kind_counts.index[i]}) = {kind_counts[i]} / {total_instances} = {round(kind_counts[i] / total_instances,3)}')
kind_probabilities = kind_counts / total_instances
# Calculate entropy using the formula: -Σ(p(x) * log2(p(x)))
entropy = -sum(p * math.log(p,2) for p in kind_probabilities)

print(f'Entropy with LOCATION=city and CONDITION=good: {round(entropy,3)}')

'''
-------------------------OUTPUT-------------------------
P(townhouse) = 4 / 10 = 0.4
P(condo) = 3 / 10 = 0.3
P(house) = 3 / 10 = 0.3
Entropy with LOCATION=city and CONDITION=good: 1.571
--------------------------------------------------------
'''



