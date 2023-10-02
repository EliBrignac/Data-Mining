import math

'''
For several years, the University of Delaware has had difficulty predicting which high school students
would accept Delaware’s offer of admission. Alice has developed a new model for predicting whether a high
school senior, who has been offered admission to the University, will actually enroll. The model is based
on state of residency, student’s high school GPA, the student’s SAT scores, the student’s major, etc. Alice
wants to sell her model to the Admissions Office. She tells them that she has tested her model on 8000 high
school seniors from previous years who were offered admission to the University and that her model made a
correct prediction for 7000 of them. The Admissions Office would very much benefit from Alice’s model if
it truly gives good predictions. With 95% confidence, what can Alice tell the Admissions Office is the true
range of success of her model?
'''

# 95% confidence means Z = 1.96
n = 8000
p = 7000/8000
z = 1.96

# Calculate the confidence interval
ci = z * math.sqrt((p * (1-p)) / n)
lower_bound = p - ci
upper_bound = p + ci
print(f"95% confidence interval: ({round(lower_bound,3)} to {round(upper_bound,3)})")
print("Lower Bound: ", lower_bound)
print("Upper Bound: ", upper_bound)

'''
------------------ File Output ------------------
95% confidence interval: (0.868 to 0.882)
Lower Bound:  0.867752802265703
Upper Bound:  0.882247197734297
--------------------------------------------------

We can say with 95% confidence that the true accuracy
of Alice's model is between 86.8% and 88.2%.
'''




