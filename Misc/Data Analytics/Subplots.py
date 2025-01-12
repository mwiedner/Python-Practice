import matplotlib.pyplot as plt

# Create some sample data
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Line plot
ax1.plot(x, y1, label="y = x^2", color='b', marker='o')
ax1.set_title('Line Plot')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.grid(True)

# Second subplot: Scatter plot
ax2.scatter(x, y2, color='g')
ax2.set_title('Scatter Plot')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
