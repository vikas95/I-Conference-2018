#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import operator

dictw = {'Health': 54, 'Computational': 8, 'Human': 34, 'Computer': 69, 'Interaction': 35, 'Informatics': 84, 'cyber': 7, 'security': 44, 'Game': 9, 'Design': 151, 'Web': 130, 'Development': 64, 'Machine': 10, 'Learning': 35, 'Technology': 110, 'Digital': 178, 'Graphic': 5, 'NLP': 4, 'software': 94, 'coding': 6, 'programming': 127, 'cryptography': 0, 'data': 532, 'science': 114}

sorted_dict = sorted(dictw.items(), key=operator.itemgetter(1))

max_x = len(sorted_dict)
max_y = sorted_dict[-1][1]

#print max_x, max_y

labels = []
y = []

for term in sorted_dict:
	labels.append(term[0])
	y.append(term[1])

N = len(y)
x = range(N)
#print x, y
width = 0.1
plt.bar(x, y, width, color="blue")
plt.xticks(x, labels)

fig = plt.gcf()
fig.set_size_inches(35, 13)
fig.savefig('test2png.png', dpi=100)

#plt.show()
