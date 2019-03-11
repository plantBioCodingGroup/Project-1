#!/Users/alanyocca/anaconda3/bin/python
#Alan E. Yocca
#03-04-19
#rabbit_field.py


import argparse
import random as ra
import numpy as np
import matplotlib.pyplot as plt

'''move rabbit around the field
plotting results
since plotting the results, going to give rabbit x and y coordinates
cannot exceed max / min xy coords
change in xy coords equally likely
variables to specify on command line:
- movements
- number of squares
	- must be perfect square... lets make field have to be a square
	- width (x) and length (y) instead of number of squares
- output
	- graphical output
'''

#parser = argparse.ArgumentParser(description='Move some rabbits.')
#parser.add_argument('movements', metavar='N', type=int, nargs='+',
#                    help='times to move rabbit around')
#parser.add_argument('--movements', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

#args = parser.parse_args()
#print(args.accumulate(args.integers))


#figure that shit out later

class Animal:	
	def __init__(self,species,width,length):
		#super(Animal, self).__init__(width,length)
		self.width = width
		self.length = length
		self.species = species
		self.xloc = ra.randint(0,self.width)
		self.yloc = ra.randint(0,self.length)
		self.xhistory = []
		self.yhistory = []
	
	def move(self,movements):
		for i in range(1,movements,1):
			#move randomly
			self.xloc += ra.randint(-1,1)
			self.yloc += ra.randint(-1,1)
		
			#keep within bounds of the field
			if self.xloc < 0:
				self.xloc = 0
			if self.xloc > self.width:
				self.xloc = self.width
			if self.yloc < 0:
				self.yloc = 0
			if self.yloc > self.length:
				self.yloc = self.length
	
			#add to plot_coords attribute for plotting
			self.xhistory.append(self.xloc)
			self.yhistory.append(self.yloc)
	
	def plot(self):
		plt.figure()
		plt.plot(self.xhistory,self.yhistory)
		plt.savefig("/Users/alanyocca/Documents/pbcoding_group/local/tmp_plot.png")
				
	def clear_movements(self):
		self.xloc = ra.randint(0,self.width)
		self.yloc = ra.randint(0,self.length)


#initialize an animal in the field
rabbit = Animal("rabbit",10,10)

#move the animal 10 times
rabbit.move(100)

#plot the output
rabbit.plot()














