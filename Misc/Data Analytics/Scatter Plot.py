import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]

# Create a scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red')

# Calculate parabolic regression (second-degree polynomial)
coefficients = np.polyfit(x, y, 2)
a, b, c = coefficients
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * x_fit**2 + b * x_fit + c
plt.plot(x_fit, y_fit, color='blue')

# Add title and labels
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()