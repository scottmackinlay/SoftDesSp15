""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
num_trials = 1000
train_percentages = range(5,95,1)
test_accuracies = numpy.zeros(len(train_percentages))

for trial in range(num_trials):
	if not trial%(num_trials/10):
		print trial 	#this is to show what trial we are on so you dont get bored
	for (i,percentage) in enumerate(train_percentages):
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=percentage)
		model = LogisticRegression(C=10**-10)
		model.fit(X_train, y_train)
		test_accuracies[i]+=float(model.score(X_test,y_test))/num_trials

fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()
