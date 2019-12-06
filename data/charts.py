import matplotlib.pyplot as plt

years = [1992, 1994, 1998, 2002, 2006, 2010, 2014]

medals = [1, 2, 20, 20, 19, 21, 21]

plt.plot(years, medals, color=(50/255, 100/255, 70/255), linewidth=3.0)

plt.ylabel("Canada Women")
plt.xlabel("Years")
plt.title("Global Population Growth by Year", pad=20)
plt.show()
