import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#load dataset
dataset = pd.read_csv("housepricebang.csv")
#intialise variables
theta = np.zeros(5)
epoch = 2000
alpha = 0.001 # learning rate
samples = dataset.shape[0]

#visualize data before normalizing
def plotdata():
	xaxis = {'area':'g','bedroom':'b','distance':'r'}
	plt.figure(figsize=(9,3))
	row = 1
	for axis in xaxis:
		#plt.subplot(3,1,row)
		plt.plot(axis,'price',xaxis[axis]+'o',data=dataset,label=axis)
		row=row+1
	plt.suptitle("attributes vs price")
	plt.show()
#normalize values ex : value - mean / standard deviation
def normalize():
	xaxis = ['area','bedroom','distance','price']
	for axis in xaxis:
		dataset[axis] = (dataset[axis]-dataset[axis].mean())/dataset[axis].std()
#cost function
def cost(xs,ys,theta):
	cost = (1/(2*samples))*((np.dot(xs,theta)-ys)**2)
	return cost.sum()
#regression model
def linearregression():
	dataset.insert(0, "ones", np.ones(samples)) #insert ones to first column
	ys = dataset['price'].to_numpy()
	xs = dataset.loc[:,:'furnished'].to_numpy()
	costs = []
	for i in range(epoch):
		gradientdescent(xs,ys,alpha)
		costs.append(cost(xs,ys,theta))
	#plot and check for convergence
	'''
	plt.plot(costs)
	plt.xlabel("iterations")
	plt.ylabel("cost")
	plt.show()
	'''
def gradientdescent(xs,ys,alpha):
	#print(theta.shape," ",xs.shape," ",ys.shape)
	global theta
	theta = theta-(alpha/samples)*(np.dot(np.transpose(xs),(np.dot(xs,theta)-ys)))
def testmodel():
	global theta
	area = float(input("enter area : "))
	bedrooms = float(input("enter no of bedrooms : "))
	distance = float(input("enter distance: "))
	furnished = float(input("enter furnished status : "))
	xs = [1.0,area,bedrooms,distance,furnished]
	price = np.dot(xs,theta)
	print("Predicted Price : ",price)
if __name__ == '__main__':
	#plotdata()
	normalize()
	#plotdata()
	linearregression()
	# testmodel()
#todo : implement in normal form
#todo : implement same for exercise
