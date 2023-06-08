import csv
import matplotlib.pyplot as plt

# Static data
data = [
    ['Age', 'Income'],
    [25, 25000],
    [23, 22000],
    [24, 26000],
    [28, 29000],
    [34, 38600],
    [32, 36500],
    [42, 41000],
    [55, 81000],
    [45, 47500]
]

# Extracting age and income from the data
age = [row[0] for row in data[1:]]
income = [row[1] for row in data[1:]]

# Number of points
num = len(age)

# Calculate mean of age and income
mean_age = sum(age) / num
mean_income = sum(income) / num

# Calculate cross-deviation and deviation about age
CD_ageincome = sum([x * y for x, y in zip(age, income)]) - num * mean_income * mean_age
CD_ageage = sum([x ** 2 for x in age]) - num * mean_age ** 2

# Calculate regression coefficients
b1 = CD_ageincome / CD_ageage
b0 = mean_income - b1 * mean_age

# Display coefficients
print("Estimated Coefficients:")
print("b0 =", b0)
print("b1 =", b1)

# Plot the actual points as a scatter plot
plt.scatter(age, income, color="b", marker="o")

# Predict response vector
response_vec = [b0 + b1 * x for x in age]

# Plot the regression line
plt.plot(age, response_vec, color="r")

# Labels for the axes
plt.xlabel('Age')
plt.ylabel('Income')

# Display the plot
plt.show()
