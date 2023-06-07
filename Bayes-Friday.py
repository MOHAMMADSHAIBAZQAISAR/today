def calculate(P_A, P_B, P_B_given_A):
    return ((P_B_given_A* P_A)/P_B)

P_A = 0.03
P_B = 0.2
P_B_given_A = 1
print("the probability that a student is absent given that today is Friday:")
print(100 * calculate(P_A, P_B, P_B_given_A))

#output:
# the probability that a student is absent given that today is Friday:
# 15.0
