
import matplotlib.pyplot as plt
import csv

with open('usacanIcehockeymanWomen.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        Us.append(int(row[0]))
        Can.append(int(row[1]))

plt.plot(usa,can, label='USA vs Canada')
plt.xlabel('usa')
plt.ylabel('can')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
