AI: Lab 8: Understanding Gradient Descent for least square line fit

Attention: 1. User input-data 2. Learning rate (alter), 3. No of steps (alter); 4. Initial Trial solution (for slope and intercept) alter 5. Outlier data -impact? 6. Home task –can you modify the code for plane

import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Sum of Squared Residuals (SSR)
def compute_ssr(x, y, intercept, slope):
    y_pred = intercept + slope * x
    ssr = np.sum((y - y_pred) ** 2)
    return ssr

# Function to compute gradient with respect to intercept
def gradient_wrt_intercept(x, y, intercept, slope):
    y_pred = intercept + slope * x
    d_intercept = -2 * np.sum(y - y_pred) / len(x)
    return d_intercept

# Function to compute gradient with respect to slope
def gradient_wrt_slope(x, y, intercept, slope):
    y_pred = intercept + slope * x
    d_slope = -2 * np.sum((y - y_pred) * x) / len(x)
    return d_slope

# Gradient descent function to minimize SSR by updating intercept and slope
def gradient_descent(x, y, intercept, slope, learning_rate, steps):
    n = len(x)
    ssr_history = []  # To track SSR values over steps

    for step in range(steps):
        # Predict y values
        y_pred = intercept + slope * x
        
        # Compute gradients
        d_intercept = gradient_wrt_intercept(x, y, intercept, slope)
        d_slope = gradient_wrt_slope(x, y, intercept, slope)

        # Update intercept and slope using the gradients
        intercept -= learning_rate * d_intercept
        slope -= learning_rate * d_slope

        # Calculate the current SSR and store it
        ssr = compute_ssr(x, y, intercept, slope)
        ssr_history.append(ssr)

        # Print progress
        if step % 100 == 0:
            print(f"Step {step}: Intercept = {intercept}, Slope = {slope}, SSR = {ssr}")

    return intercept, slope, ssr_history

# Function to systematically vary the intercept while keeping slope constant
def plot_ssr_vs_intercept(x, y, slope, intercept_range):
    ssr_values = []
    intercept_values = np.linspace(intercept_range[0], intercept_range[1], 100)
    
    for intercept in intercept_values:
        ssr = compute_ssr(x, y, intercept, slope)
        ssr_values.append(ssr)
    
    plt.plot(intercept_values, ssr_values)
    plt.xlabel('Intercept')
    plt.ylabel('SSR')
    plt.title(f'SSR vs Intercept (Slope={slope})')
    plt.grid(True)
    plt.show()

# Function to systematically vary the slope while keeping intercept constant
def plot_ssr_vs_slope(x, y, intercept, slope_range):
    ssr_values = []
    slope_values = np.linspace(slope_range[0], slope_range[1], 100)
    
    for slope in slope_values:
        ssr = compute_ssr(x, y, intercept, slope)
        ssr_values.append(ssr)
    
    plt.plot(slope_values, ssr_values)
    plt.xlabel('Slope')
    plt.ylabel('SSR')
    plt.title(f'SSR vs Slope (Intercept={intercept})')
    plt.grid(True)
    plt.show()

# Function to plot d(SSR)/d(intercept) vs intercept (keeping slope constant)
def plot_gradient_wrt_intercept(x, y, slope, intercept_range):
    gradient_values = []
    intercept_values = np.linspace(intercept_range[0], intercept_range[1], 100)
    
    for intercept in intercept_values:
        grad_intercept = gradient_wrt_intercept(x, y, intercept, slope)
        gradient_values.append(grad_intercept)
    
    plt.plot(intercept_values, gradient_values)
    plt.xlabel('Intercept')
    plt.ylabel('d(SSR)/d(Intercept)')
    plt.title(f'd(SSR)/d(Intercept) vs Intercept (Slope={slope})')
    plt.grid(True)
    plt.show()

# Function to plot d(SSR)/d(slope) vs slope (keeping intercept constant)
def plot_gradient_wrt_slope(x, y, intercept, slope_range):
    gradient_values = []
    slope_values = np.linspace(slope_range[0], slope_range[1], 100)
    
    for slope in slope_values:
        grad_slope = gradient_wrt_slope(x, y, intercept, slope)
        gradient_values.append(grad_slope)
    
    plt.plot(slope_values, gradient_values)
    plt.xlabel('Slope')
    plt.ylabel('d(SSR)/d(Slope)')
    plt.title(f'd(SSR)/d(Slope) vs Slope (Intercept={intercept})')
    plt.grid(True)
    plt.show()

# Main function to get user input and run gradient descent
if __name__ == "__main__":
    # Sample data points (x, y)
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = np.array([1.2, 1.9, 3.0, 3.9, 5.1], dtype=float)

    # Get user inputs for learning rate and number of steps
    learning_rate = float(input("Enter learning rate (recommended between 0.001 and 0.01): "))
    steps = int(input("Enter number of steps (recommended between 1000 and 10000): "))

    # Initial guess for slope and intercept
    intercept_init = 0.5  # Initial intercept guess
    slope_init = 0.9  # Initial slope guess

    # Run gradient descent to optimize intercept and slope
    intercept_opt, slope_opt, ssr_history = gradient_descent(x, y, intercept_init, slope_init, learning_rate, steps)

    # Final optimized values
    print(f"Optimized Intercept: {intercept_opt}, Optimized Slope: {slope_opt}")
    
    # Plot SSR vs Intercept (keeping slope constant)
    intercept_range = (-2, 4)  # Adjust this range based on your data
    plot_ssr_vs_intercept(x, y, slope_opt, intercept_range)

    # Plot SSR vs Slope (keeping intercept constant)
    slope_range = (-1, 2)  # Adjust this range based on your data
    plot_ssr_vs_slope(x, y, intercept_opt, slope_range)

    # Plot d(SSR)/d(Intercept) vs Intercept (keeping slope constant)
    plot_gradient_wrt_intercept(x, y, slope_opt, intercept_range)

    # Plot d(SSR)/d(Slope) vs Slope (keeping intercept constant)
    plot_gradient_wrt_slope(x, y, intercept_opt, slope_range)

    # Optional: Plot SSR history to observe learning
    plt.plot(ssr_history)
    plt.xlabel('Steps')
    plt.ylabel('SSR')
    plt.title('SSR Reduction Over Time (Gradient Descent)')
    plt.grid(True)
    plt.show()
