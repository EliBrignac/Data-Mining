import math

# Calculate the weighted entropy of attribute SHOTS
enone = 0
eall = -8/14 * math.log(8/14, 2) - 6/14 * math.log(6/14, 2)
SHOTS = 14/20 * eall + 6/20 * enone
print("shots = ", SHOTS)

# Calculate the weighted entropy of attribute HAIR
elong = -6/8 * math.log(6/8, 2) - 2/8 * math.log(2/8, 2)
eshort = -2/12 * math.log(2/12, 2) - 10/12 * math.log(10/12, 2)
HAIR = 8/20 * elong + 12/20 * eshort
print("hair = ", HAIR)

# I am leaving this here even though it is not used
# Calculate the weighted entropy of attribute HEIGHT
# etiny = -3/4 * math.log(3/4, 2) - 1/4 * math.log(1/4, 2)
# emedium = -4/5 * math.log(4/5, 2) - 1/5 * math.log(1/5, 2)
# ehuge = -10/11 * math.log(10/11, 2) - 1/11 * math.log(1/11, 2)
# SIZE = 4/20 * etiny + 5/20 * emedium + 11/20 * ehuge
# print("size = ", SIZE)


'''
------------------ File Output ------------------
shots =  0.6896596952239761
hair =  0.7145247027726656

Shots has the smallest weighted entropy, so it is the best
attribute to split on.
--------------------------------------------------
'''