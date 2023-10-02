import pandas as pd
from scipy.stats import chi2_contingency, chi2

# Create a Pandas DataFrame with your data
data = pd.read_csv('HW4 - Sheet2.csv')
# categorize LENGTH
data = data[data['LENGTH'] <= 175]
data = data[data['LENGTH'] >= 112]
#print(data)

C = [
    [4, 0, 1],
    [0, 1, 7]
]

row_totals = []
col_totals = []
N = len(data)

# Calculate the row totals
for i in C:
    row_totals.append(sum(i))

# Calculate the column totals
for i in range(len(C[0])):
    total = 0
    for j in range(len(C)):
        total += C[j][i]
    col_totals.append(total)

E = [[0, 0, 0],
     [0, 0, 0]]

for i in range(len(row_totals)):
    for j in range(len(col_totals)):
        E[i][j] = (row_totals[i] * col_totals[j]) / N

print("Expected frequencies:")
for i in E:
    print(i)

# Calculate the chi-squared statistic
chi2 = 0
for i in range(len(C)):
    for j in range(len(C[0])):
        chi2 += ((C[i][j] - E[i][j])**2) / E[i][j]

print(f"Chi-Squared Statistic: {chi2} > 4.605")

'''
------------------------ File Output ------------------------
Expected frequencies:
[1.5384615384615385, 0.38461538461538464, 3.076923076923077]
[2.4615384615384617, 0.6153846153846154, 4.923076923076923]

Chi-Squared Statistic: 9.303125 > 4.605
------------------------------------------------------------

We reject the null hypothesis and we do NOT merge

'''