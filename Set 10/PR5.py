import matplotlib.pyplot as plt
year = [1960, 1970, 1980, 1990, 2000, 2010]
pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]

# line chart
plt.plot(year, pop_pakistan, color='blue')
plt.plot(year, pop_india, color='red')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('Pakistan India Population till 2010')
plt.show()

# pie chart
plt.pie(pop_india,labels=year,startangle=90, autopct='%.1f%%')
plt.title('Pakistan India Population till 2010')
plt.show()

plt.bar(year,pop_india, align='center', alpha=0.5,color='r')
plt.bar(year,pop_pakistan, align='center', alpha=0.5,color='b')
plt.xlabel('Year')
plt.ylabel('Population in million')
plt.title('Pakistan India Population till 2010')
plt.show()
