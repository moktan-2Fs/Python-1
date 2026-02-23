import matplotlib.pyplot as plt

years = [2000, 2005, 2010, 2015, 2020]
population = [50, 55, 60, 65, 70]

# Create the plot
plt.plot(years, population, marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.title('Population Growth Over Time')

# Show grid
plt.grid(True)

# Display the plot
plt.show()