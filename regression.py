# Sample data
X = [1, 2, 3, 4, 5]  # Independent variable
y = [2, 4, 6, 8, 10]  # Dependent variable

# Calculate the means of X and y
mean_x = sum(X) / len(X)
mean_y = sum(y) / len(y)

# Calculate the deviations
deviations_x = [xi - mean_x for xi in X]
deviations_y = [yi - mean_y for yi in y]

# Calculate the slope (b1)
numerator = sum(deviations_x[i] * deviations_y[i] for i in range(len(X)))
denominator = sum(deviation_x ** 2 for deviation_x in deviations_x)
b1 = numerator / denominator

# Calculate the intercept (b0)
b0 = mean_y - b1 * mean_x

# Make predictions
X_new = [6, 7, 8]  # New data points to predict
predictions = [b0 + b1 * xi for xi in X_new]

# Print the coefficients and predictions
print("Intercept:", b0)
print("Coefficient:", b1)
print("Predictions:", predictions)


#Can use below commented code also


# import matplotlib.pyplot as plt

# # Sample data
# X = [1, 2, 3, 4, 5]  # Independent variable
# y = [2, 4, 6, 8, 10]  # Dependent variable

# # Calculate the means of X and y
# mean_x = sum(X) / len(X)
# mean_y = sum(y) / len(y)

# # Calculate the deviations
# deviations_x = [xi - mean_x for xi in X]
# deviations_y = [yi - mean_y for yi in y]

# # Calculate the slope (b1)
# numerator = sum(deviations_x[i] * deviations_y[i] for i in range(len(X)))
# denominator = sum(deviation_x ** 2 for deviation_x in deviations_x)
# b1 = numerator / denominator

# # Calculate the intercept (b0)
# b0 = mean_y - b1 * mean_x

# # Make predictions
# X_new = [6, 7, 8]  # New data points to predict
# predictions = [b0 + b1 * xi for xi in X_new]

# # Plotting the points and the regression line
# plt.scatter(X, y, color='blue', label='Data Points')
# plt.plot(X, [b0 + b1 * xi for xi in X], color='red', label='Regression Line')
# plt.scatter(X_new, predictions, color='green', label='Predictions')
# plt.xlabel('Independent Variable (X)')
# plt.ylabel('Dependent Variable (y)')
# plt.title('Linear Regression')
# plt.legend()
# plt.show()
