#!/usr/bin/python
import sys
import random
import string
from math import *

def testfn(trainfile,testfile):
	f1 = open(trainfile, 'rU')
	f2 = open(testfile, 'rU')
	f3 = open('accuracy', 'w')

	i=0
	j=0
	trainline=0
	c = []

	for line in f1:
		trainline = trainline + 1
		if j==0:
			c = line.split(',')
			for x in c:
				j=j+1

	print trainline
	f1.close()

#	a = [[0]*j]*15
	a = []
	i=0
	
	f1 = open(trainfile, 'rU')
	for line in f1:
		y = line.split(',')
		a.append(y)
		for x in range(j-1):
			a[i][x] = float(a[i][x])
#		print a[i]
		i = i+1
#		print a[i][0]*a[i][1]
	f1.close()
	b = []
	k=0

	for line in f2:
#		if k<150:
#			k=k+1
			b = line.split(',')
			for y in range(j-1):
				b[y] = float(b[y])
			i=0
			minval = 10000000000.0
			ind = 0
			while i<trainline:
			 	comp = 0.0
			 	for y in range(j-1):
					comp = comp + pow(a[i][y]-b[y], 2)

				if minval>comp:
					minval = comp
					ind = i
				i = i + 1
#			print b, a[ind][j-1]
			x=b[j-1].split('\n')
			f3.write(x[0]+' '+a[ind][j-1])
	f2.close()
	f3.close()
			

def main():
	testfn(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()
