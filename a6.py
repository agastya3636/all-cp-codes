AI
Least square Line fit-Regression: Lab 7

Fit the best straight line for the data points

import numpy as np
import matplotlib.pyplot as plt

# Generate random data points
np.random.seed(42)

x = np.random.rand(50) * 10  # Random x values between 0 and 10
y = 2.5 * x + np.random.randn(50) * 2  # Corresponding y values with noise

# Compute the mean of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Compute the slope (m) and intercept (c) using the formulas
m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
c = y_mean - m * x_mean

# Output the slope and intercept
print(f"Slope (m): {m}")
print(f"Intercept (c): {c}")

# Plot data points
plt.scatter(x, y, color='blue', label='Data Points')

# Calculate the regression line values
regression_line = m * x + c

# Plot the regression line
plt.plot(x, regression_line, color='red', label='Regression Line (y = {:.2f}x + {:.2f})'.format(m, c))

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Regression Line')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the Mean Squared Error (MSE)
mse = np.mean((y - regression_line) ** 2)
print(f"Mean Squared Error (MSE): {mse}") 


Find the changes made to above code; establish the importance of training data on your test model and role of outliers; can you manipulate these
import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility
np.random.seed(42)

# Generate random data points
x = np.random.rand(50) * 10  # Random x values between 0 and 10
y = 2.5 * x + np.random.randn(50) * 2  # Corresponding y values with noise

# Introduce 2.5% of outlier data
num_outliers = int(0.025 * len(x))  # Calculate the number of outliers
x_outliers = np.random.rand(num_outliers) * 10  # Random x values for outliers
y_outliers = 2.5 * x_outliers + np.random.randn(num_outliers) * 20 + 50  # Outliers with higher deviation

# Combine the original data with outliers
x = np.concatenate((x, x_outliers))
y = np.concatenate((y, y_outliers))

# Ask user for the training set percentage
train_percent = float(input("Enter the percentage of data to be used for training (e.g., 80 for 80%): ")) / 100
num_train = int(train_percent * len(x))

# Split data into training and testing sets
indices = np.random.permutation(len(x))
train_indices = indices[:num_train]
test_indices = indices[num_train:]

x_train = x[train_indices]
y_train = y[train_indices]
x_test = x
y_test = y

# Compute the mean of x and y for training data
x_mean_train = np.mean(x_train)
y_mean_train = np.mean(y_train)

# Compute the slope (m) and intercept (c) using the least squares method for training data
m_train = np.sum((x_train - x_mean_train) * (y_train - y_mean_train)) / np.sum((x_train - x_mean_train) ** 2)
c_train = y_mean_train - m_train * x_mean_train

# Calculate regression line values for the training data
regression_line_train = m_train * x_train + c_train

# Calculate regression line values for the full data
regression_line_test = m_train * x_test + c_train

# Plot data points
plt.scatter(x, y, color='blue', label='All Data Points')
plt.scatter(x_train, y_train, color='green', label='Training Data Points')

# Plot the regression lines
plt.plot(x_test, regression_line_test, color='red', label='Regression Line on Full Data (y = {:.2f}x + {:.2f})'.format(m_train, c_train))
plt.plot(x_train, regression_line_train, color='orange', label='Regression Line on Training Data')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Regression Line with Outliers and Train/Test Split')
plt.legend()
plt.grid(True)
plt.show()

# Calculate and print the Mean Squared Error (MSE) for training and testing
mse_train = np.mean((y_train - regression_line_train) ** 2)
mse_test = np.mean((y_test - regression_line_test) ** 2)

print(f"Mean Squared Error (MSE) on Training Data: {mse_train}")
print(f"Mean Squared Error (MSE) on Full Data (Testing Data): {mse_test}")



Fitting of plane to 3D data points

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the seed for reproducibility
np.random.seed(42)

# Generate random 3D data points
x = np.random.rand(50) * 10  # Random x values between 0 and 10
y = np.random.rand(50) * 10  # Random y values between 0 and 10
z = 3 * x + 2 * y + np.random.randn(50) * 3  # Corresponding z values with noise

# Introduce 2.5% of outlier data
num_outliers = int(0.025 * len(x))  # Calculate the number of outliers
x_outliers = np.random.rand(num_outliers) * 10  # Random x values for outliers
y_outliers = np.random.rand(num_outliers) * 10  # Random y values for outliers
z_outliers = 3 * x_outliers + 2 * y_outliers + np.random.randn(num_outliers) * 30 + 50  # Outliers with higher deviation

# Combine the original data with outliers
x = np.concatenate((x, x_outliers))
y = np.concatenate((y, y_outliers))
z = np.concatenate((z, z_outliers))

# Ask user for the training set percentage
train_percent = float(input("Enter the percentage of data to be used for training (e.g., 80 for 80%): ")) / 100
num_train = int(train_percent * len(x))

# Split data into training and testing sets
indices = np.random.permutation(len(x))
train_indices = indices[:num_train]
test_indices = indices[num_train:]

x_train = x[train_indices]
y_train = y[train_indices]
z_train = z[train_indices]
x_test = x
y_test = y
z_test = z

# Prepare the design matrix for training data
A_train = np.c_[x_train, y_train, np.ones(len(x_train))]  # Design matrix for plane fitting

# Compute the least squares solution for plane fitting (Ax = b => x = (A^T A)^-1 A^T b)
coefficients = np.linalg.lstsq(A_train, z_train, rcond=None)[0]  # Coefficients: [a, b, c] for plane ax + by + c = z

# Compute the predicted z values for both training and full data
z_pred_train = coefficients[0] * x_train + coefficients[1] * y_train + coefficients[2]
z_pred_test = coefficients[0] * x_test + coefficients[1] * y_test + coefficients[2]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data points
ax.scatter(x, y, z, color='blue', label='All Data Points')
ax.scatter(x_train, y_train, z_train, color='green', label='Training Data Points')

# Plot the regression plane for the full data
x_plane, y_plane = np.meshgrid(np.linspace(min(x), max(x), 10), np.linspace(min(y), max(y), 10))
z_plane = coefficients[0] * x_plane + coefficients[1] * y_plane + coefficients[2]
plane = ax.plot_surface(x_plane, y_plane, z_plane, color='orange', alpha=0.5)

# Add custom legend
scatter_blue = ax.scatter([], [], [], color='blue', label='All Data Points')
scatter_green = ax.scatter([], [], [], color='green', label='Training Data Points')
scatter_plane = plt.Line2D([0], [0], linestyle="none", marker='o', markersize=10, markerfacecolor='orange', alpha=0.5, label='Fitted Plane')
ax.legend(handles=[scatter_blue, scatter_green, scatter_plane])

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Least Squares Plane Fit with Outliers and Train/Test Split')

plt.show()

# Calculate and print the Mean Squared Error (MSE) for training and testing
mse_train = np.mean((z_train - z_pred_train) ** 2)
mse_test = np.mean((z_test - z_pred_test) ** 2)

print(f"Mean Squared Error (MSE) on Training Data: {mse_train}")
print(f"Mean Squared Error (MSE) on Full Data (Testing Data): {mse_test}")

Fitting of plane to 4D data points (X,Y,Z,I) using any three chosen dimensions

 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

# Set the seed for reproducibility
np.random.seed(42)

# Generate random 4D data points
R = np.random.rand(50) * 10  # Random Red channel values between 0 and 10
G = np.random.rand(50) * 10  # Random Green channel values between 0 and 10
B = np.random.rand(50) * 10  # Random Blue channel values between 0 and 10
I = 3 * R + 2 * G + np.random.randn(50) * 3  # Intensity with some noise

# Introduce 2.5% of outlier data
num_outliers = int(0.025 * len(R))  # Calculate the number of outliers
R_outliers = np.random.rand(num_outliers) * 10
G_outliers = np.random.rand(num_outliers) * 10
B_outliers = np.random.rand(num_outliers) * 10
I_outliers = 3 * R_outliers + 2 * G_outliers + np.random.randn(num_outliers) * 30 + 50  # Outliers with higher deviation

# Combine the original data with outliers
R = np.concatenate((R, R_outliers))
G = np.concatenate((G, G_outliers))
B = np.concatenate((B, B_outliers))
I = np.concatenate((I, I_outliers))

# Normalize RGB values to the range [0, 1] for coloring
R_norm = R / 10.0
G_norm = G / 10.0
B_norm = B / 10.0
colors = np.vstack((R_norm, G_norm, B_norm)).T

# Ask user for the training set percentage
train_percent = float(input("Enter the percentage of data to be used for training (e.g., 80 for 80%): ")) / 100
num_train = int(train_percent * len(R))

# Split data into training and testing sets
indices = np.random.permutation(len(R))
train_indices = indices[:num_train]
test_indices = indices[num_train:]

R_train = R[train_indices]
G_train = G[train_indices]
B_train = B[train_indices]
I_train = I[train_indices]
R_test = R
G_test = G
B_test = B
I_test = I

# Ask user which three dimensions to use for 3D plotting
print("Choose three dimensions for the 3D plot:")
print("1. Red (R)")
print("2. Green (G)")
print("3. Blue (B)")
print("4. Intensity (I)")
choices = input("Enter your choice of three dimensions separated by commas (e.g., 1,2,3): ")

choice_mapping = {1: 'R', 2: 'G', 3: 'B', 4: 'I'}
selected_dims = [choice_mapping[int(c.strip())] for c in choices.split(',')]

# Extract data based on user choice
data_dict = {'R': R, 'G': G, 'B': B, 'I': I}
train_data_dict = {'R': R_train, 'G': G_train, 'B': B_train, 'I': I_train}
test_data_dict = {'R': R_test, 'G': G_test, 'B': B_test, 'I': I_test}

x_data = data_dict[selected_dims[0]]
y_data = data_dict[selected_dims[1]]
z_data = data_dict[selected_dims[2]]

x_train = train_data_dict[selected_dims[0]]
y_train = train_data_dict[selected_dims[1]]
z_train = train_data_dict[selected_dims[2]]
x_test = test_data_dict[selected_dims[0]]
y_test = test_data_dict[selected_dims[1]]
z_test = test_data_dict[selected_dims[2]]

# Prepare the design matrix for training data
A_train = np.c_[x_train, y_train, np.ones(len(x_train))]  # Design matrix for plane fitting

# Compute the least squares solution for plane fitting
coefficients = np.linalg.lstsq(A_train, z_train, rcond=None)[0]  # Coefficients: [a, b, c] for plane ax + by + c = z

# Compute the predicted z values for both training and full data
z_pred_train = coefficients[0] * x_train + coefficients[1] * y_train + coefficients[2]
z_pred_test = coefficients[0] * x_test + coefficients[1] * y_test + coefficients[2]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data points with their RGB colors
ax.scatter(x_data, y_data, z_data, color=colors, label='All Data Points')
ax.scatter(x_train, y_train, z_train, color=colors[train_indices], label='Training Data Points')

# Plot the regression plane for the full data
x_plane, y_plane = np.meshgrid(np.linspace(min(x_data), max(x_data), 10), np.linspace(min(y_data), max(y_data), 10))
z_plane = coefficients[0] * x_plane + coefficients[1] * y_plane + coefficients[2]
plane = ax.plot_surface(x_plane, y_plane, z_plane, color='orange', alpha=0.5)

# Add custom legend
scatter_all = Line2D([0], [0], linestyle="none", marker='o', markersize=10, markerfacecolor='black', label='All Data Points')
scatter_train = Line2D([0], [0], linestyle="none", marker='o', markersize=10, markerfacecolor='black', label='Training Data Points')
scatter_plane = Line2D([0], [0], linestyle="none", marker='o', markersize=10, markerfacecolor='orange', alpha=0.5, label='Fitted Plane')
ax.legend(handles=[scatter_all, scatter_train, scatter_plane])

# Add labels and title
ax.set_xlabel(selected_dims[0])
ax.set_ylabel(selected_dims[1])
ax.set_zlabel(selected_dims[2])
plt.title(f'Least Squares Plane Fit with RGB Colors and Train/Test Split - {selected_dims[0]}, {selected_dims[1]}, {selected_dims[2]}')

plt.show()

# Calculate and print the Mean Squared Error (MSE) for training and testing
mse_train = np.mean((z_train - z_pred_train) ** 2)
mse_test = np.mean((z_test - z_pred_test) ** 2)

print(f"Mean Squared Error (MSE) on Training Data: {mse_train}")
print(f"Mean Squared Error (MSE) on Full Data (Testing Data): {mse_test}")


Fit circle to a few (x,y) points
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate 10 2D data points (x, y) for a circle with some noise
np.random.seed(42)
angle = np.linspace(0, 2 * np.pi, 10)  # 10 equally spaced points on a circle
true_center = (5, 7)
true_radius = 4

# Generate points on a circle around the true center with true radius
x = true_center[0] + true_radius * np.cos(angle)
y = true_center[1] + true_radius * np.sin(angle)

# Introduce small random noise (error) in the data points
noise_x = np.random.normal(0, 0.2, size=x.shape)  # Small noise in x
noise_y = np.random.normal(0, 0.2, size=y.shape)  # Small noise in y
x_noisy = x + noise_x
y_noisy = y + noise_y

# Step 2: Set up the linear system to solve for circle parameters
A = np.c_[x_noisy, y_noisy, np.ones(len(x_noisy))]
b = x_noisy**2 + y_noisy**2

# Step 3: Solve the linear system using the least squares method
c = np.linalg.lstsq(A, b, rcond=None)[0]

# Extract circle parameters from the solution
a = c[0] / 2
b = c[1] / 2
r = np.sqrt(c[2] + a**2 + b**2)

# Step 4: Plot the original points and the fitted circle
fig, ax = plt.subplots()

# Plot the noisy data points
ax.scatter(x_noisy, y_noisy, color='blue', label='Noisy Data Points')

# Generate points for the fitted circle for plotting
circle_angles = np.linspace(0, 2 * np.pi, 100)
x_fit = a + r * np.cos(circle_angles)
y_fit = b + r * np.sin(circle_angles)

# Plot the fitted circle
ax.plot(x_fit, y_fit, color='orange', label='Fitted Circle', linestyle='--')

# Set labels and title
ax.set_aspect('equal', 'box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Least Squares Circle Fitting with Noisy Data Points')

plt.legend()
plt.grid(True)
plt.show()

# Print the fitted circle parameters
print(f"Fitted Circle Center: ({a:.2f}, {b:.2f})")
print(f"Fitted Circle Radius: {r:.2f}")

Fit a straight line using Algebric equation and using using Matrix equation 
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
