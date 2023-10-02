import pandas as pd
from scipy.stats import chi2_contingency, chi2

# Create a Pandas DataFrame with your data
df = pd.read_csv('HW4 - Sheet2.csv')
# categorize LENGTH
df = df[df['LENGTH'] >= 147]

C = [
    [0, 1, 7],
    [1, 1, 5]
]

row_totals = []
col_totals = []
N = len(df)

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

print(f"Chi-Squared Statistic: {chi2} < 4.605")
'''
------------------------ File Output ------------------------
Expected frequencies:
[0.5333333333333333, 1.0666666666666667, 6.4]
[0.4666666666666667, 0.9333333333333333, 5.6]

Chi-Squared Statistic: 1.2723214285714284 < 4.605
------------------------------------------------------------

We do NOT reject the null hypothesis and we DO merge

'''