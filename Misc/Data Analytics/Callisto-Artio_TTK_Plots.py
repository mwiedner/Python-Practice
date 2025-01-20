import matplotlib.pyplot as plt
import numpy as np

# Create a scatter plot
plt.figure(figsize=(10, 6))

# Colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black']

# Sample data
x = [80, 0]

count = 0
while count <= 7:
    y = [(912 / (360 * (count + 1))) * x[0], 0]
    plt.plot(x, y, color=colors[count])
    count += 1

# Add title and labels
plt.title('Relationship of Artio TTK on Callisto TTK for equivalent expected time to Voidwaker Hilt, based on group size')
plt.ylabel('Callisto TTK')
plt.xlabel('Artio TTK')

# Show the plot
plt.show()