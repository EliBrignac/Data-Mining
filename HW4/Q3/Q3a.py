import pandas as pd
import numpy as np
import math

df = pd.read_csv('HW4 - Sheet2.csv')

def calculate_entropy(data):
    class_counts = data['DECISION'].value_counts()
    probabilities = class_counts / len(data)
    entropy = -sum(probabilities * np.log2(probabilities))

    return entropy

def calculate_weighted_entropy(data, split_point):
    left = data[data['LENGTH'] <= split_point]
    right = data[data['LENGTH'] > split_point]
    
    # Calculate entropy for each subset
    entropy1 = calculate_entropy(left)
    entropy2 = calculate_entropy(right)
    print(f"({split_point}) Left side Entropy: {entropy1}")
    print(f"({split_point}) Right side Entropy: {entropy2}")

    
    weighted_entropy = (len(left) / len(data)) * entropy1 + (len(right) / len(data)) * entropy2
    print(f"({split_point}) Weighted Entropy: {weighted_entropy}")
    
    return weighted_entropy


split_point_118 = 118
split_point_147 = 147

print("Calculations:")
weighted_entropy_118 = calculate_weighted_entropy(df, split_point_118)
print('')
weighted_entropy_147 = calculate_weighted_entropy(df, split_point_147)

print("\n")
print("Summary:")
print(f'Weighted Entropy at split point 118: {weighted_entropy_118}')
print(f'Weighted Entropy at split point 147: {weighted_entropy_147}')

better = "118" if  weighted_entropy_118 < weighted_entropy_147 else "147"
print(f'The better split point is {better}')


'''
------------------------ File Output ------------------------
Calculations:
(118) Left side Entropy: 1.584962500721156
(118) Right side Entropy: 1.1897319168207328
(118) Weighted Entropy: 1.2436269964435178

(147) Left side Entropy: 1.3787834934861753
(147) Right side Entropy: 0.9055872616982603
(147) Weighted Entropy: 1.056149699085324


Summary:
Weighted Entropy at split point 118: 1.2436269964435178
Weighted Entropy at split point 147: 1.056149699085324
The better split point is 147
------------------------------------------------------------

We choose 147 as our split point because it has a lower weighted
entropy than 118.

'''