import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Python', 'C++', 'Java', 'JavaScript', 'Other']
sizes = [40, 30, 20, 10, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Add a title
plt.title('Programming Language Usage')

# Show the plot
plt.show()
