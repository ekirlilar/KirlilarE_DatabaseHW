import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = [] #first row not data

with open('usaIcehockeyWomen.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spereadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				print("won agold medal")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("won silver medal")
				silvers.append(row[7])
			else:
				print("won a bronze medal")
				bronzes.append(row[7])

			print(line_count)
			line_count += 1

#now lets seeour medal counts
print(len(golds), "gold medals")
print(len(silvers), "silver medals")
print(len(bronzes), "bronze medals")

lables = ["Gold", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes)]
color = ["gold", "silver", "darkgoldenrod"]
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=color, autopct='1%.f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.legend(lables, loc=1)
plt.title("Hockey Medal Wins - Historic Medal Counts")
plt.xlabel("Medal Count Since 1924")
plt.show()