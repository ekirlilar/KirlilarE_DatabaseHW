import matplotlib.pyplot as pyplot

hours =[4, 8, 2]
activities = ['sleep', 'work', 'play']
colors = ['gold', 'silver', 'red']

plt.pie(hours, lables=activities, colors=colorst,
	startangle=45, autopct='%1f%%')

plt.show()