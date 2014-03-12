#!/usr/bin/python

import sys
import random 
import string

def testfn():
	a = []
	
	i=0
	f1=open("accuracy", 'rU')
	for line in f1:
		x=line.split(' ')
		if x[0] not in a:
			a.append(x[0])
			i=i+1
	f1.close()
	print a

	b = []
	for j in range(i):
		for k in range(i):
			b.append(0)
	
	count=0
	f1=open("accuracy", 'rU')
	for line in f1:
		x=line.split(' ')
		y =  x[1].split('\n') 
		x[1] = y[0]
		for j in range(i):
			for k in range(i):
				if x[0] == a[j] and x[1] == a[k]:
					count = count +1
					b[j*i+k] = b[j*i+k]+1

	print count
	count = 0
	for x in b:
		count = count + 1
	   	if count%i == 0: 
	  	 	print x
		else:
			print x,

	f1.close()

def main():
	testfn()

if __name__ == '__main__':
	main()

