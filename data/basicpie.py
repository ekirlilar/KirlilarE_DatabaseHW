import matplotlib.pyplot as plt

hours =[4,8]
activities =['sleep', 'work']
colors =['gold', 'silver']

plt.pie(hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()