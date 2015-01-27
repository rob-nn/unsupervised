import random
import matplotlib.pyplot as pyplot
from math import *

def plot(t_set, color = 'b'):
	x = []
	y = []
	for index in range(len(t_set)):
		x.append(t_set[index][0])
		y.append(t_set[index][1])
	pyplot.plot(x, y, color + 'x', markersize=8) 

def run():
	random.seed()

	num_items = 20
	num_iter = 10000
	num_mus = 3 

	t_set = []
	while True:
		t_set.append([random.uniform(0, 5), random.uniform(0,5)])
		t_set.append([random.uniform(6, 10), random.uniform(6,10)])
		if len(t_set) >= num_items:
			break

	mus = []
	for index in range(num_mus):
		mus.append([random.uniform(0, 10), random.uniform(0,10)])

	
	for iteration in range(num_iter):
		mu_points = []
		for par in range(num_mus):
			mu_points.append([])

		for item in range(num_items):
			tmp = []
			for j in range(num_mus):
				tmp.append(pow(sqrt(pow(t_set[item][0]-mus[j][0],2) + pow(t_set[item][1] - mus[j][1],2)),2))
			min_mu = min(tmp)
			ind = tmp.index(min_mu)
			mu_points[ind].append(t_set[item])
	for mu in range(len(mus)):
		if len(mu_points[mu]) > 0:
			x0 = 0
			x1 = 0
			for point in range(len(mu_points[mu])):
				x0 = x0 + mu_points[mu][point][0]
				x1 = x1 + mu_points[mu][point][1]
			mus[mu][0] = x0 / len(mu_points[mu])
			mus[mu][1] = x1 / len(mu_points[mu])
		else:
			mus[mu] = [0, 0]


	plot(t_set, 'b')
	pyplot.hold(True)
	plot(mus, 'r')	
	pyplot.show()



if __name__ == '__main__':
	run()
