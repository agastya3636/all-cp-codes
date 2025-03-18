import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate 5 2D data points (x, y)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.2, 2.8, 3.6, 4.5, 5.1])

# Display the data points
print("Data Points:")
for i in range(len(x)):
    print(f"({x[i]}, {y[i]})")

# Step 2: Fit line using matrix solution (AX = B)
# We want to fit y = mx + c, so the matrix system is derived from:
# [x1, 1] [m] = [y1]
# [x2, 1] [c] = [y2]
# ...
A = np.vstack([x, np.ones(len(x))]).T
B = y

# Display matrix A and vector B
print("\nMatrix A:")
print(A)
print("\nVector B:")
print(B)

# Solve for [m, c] using the least squares solution
X, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)
m, c = X

# Display the solution vector X
print("\nSolution Vector X (m, c):")
print(X)

# Display the fitted line parameters
print(f"\nFitted Line Parameters using Matrix Solution:\nSlope (m): {m:.2f}\nIntercept (c): {c:.2f}")

# Step 3: Fit line using algebraic equations
# Using formulas for slope (m) and intercept (c)
X_mean = np.mean(x)
Y_mean = np.mean(y)
m_algebraic = (np.sum(x * y) - len(x) * X_mean * Y_mean) / (np.sum(x ** 2) - len(x) * X_mean ** 2)
c_algebraic = Y_mean - m_algebraic * X_mean

# Display the algebraic solution parameters
print(f"\nFitted Line Parameters using Algebraic Equations:\nSlope (m): {m_algebraic:.2f}\nIntercept (c): {c_algebraic:.2f}")

# Step 4: Plot the data points and the fitted line
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Data Points')

# Plot the fitted line from matrix solution
x_fit = np.linspace(min(x), max(x), 100)
y_fit = m * x_fit + c
plt.plot(x_fit, y_fit, color='red', linestyle='--', label='Fitted Line (Matrix Solution)')

# Plot the fitted line from algebraic equations
y_fit_algebraic = m_algebraic * x_fit + c_algebraic
plt.plot(x_fit, y_fit_algebraic, color='green', linestyle='--', label='Fitted Line (Algebraic Solution)')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Fit using Matrix Solution and Algebraic Equations')
plt.legend()
plt.grid(True)
plt.show()
