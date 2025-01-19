import matplotlib.pyplot as plt
import numpy as np

# Create a scatter plot
plt.figure(figsize=(10, 6))

# Colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black']

# Sample data
x = []
for number in range(8):
    x.append([80, 0])
y = []

count = 0
while count <= 7:
    y.append([(912/(360*(count+1)))*x[0][0], 0])
    # Calculate linear regression (first-degree polynomial)
    plt.plot(x[count], y[count], color=colors[count])
    count+=1

# Add title and labels
plt.title('Relationship of Artio TTK on Callisto TTK for equivalent expected time to Voidwaker Hilt, based on group size')
plt.ylabel('Callisto TTK')
plt.xlabel('Artio TTK')

# Show the plot
plt.show()