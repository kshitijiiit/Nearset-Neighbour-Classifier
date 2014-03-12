#!/usr/bin/python
import sys
import random
import string
from math import *

def testfn():
	f1=open("meanAndDeviation", 'rU')
	total=0.0
	count=0
	u=0.0
	for line in f1:
		count = count+1
		x=line.split('\n')
		total = total + float(x[0])
		u = u + pow(float(x[0]), 2)
	print "Mean: ",
	print total/float(count)
	print "Standard Deviation: ",
	print sqrt(u/float(count)-pow(total/float(count), 2))
	f1.close()


def main():
	testfn()

if __name__ == '__main__':
	main()
