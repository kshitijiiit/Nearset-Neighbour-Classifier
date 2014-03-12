#!/usr/bin/python
import sys
import random
import string

def testfn(infile):
	f1=open(infile, 'rU')
	f2=open("meanAndDeviation", 'a')
	total=0.0
	correct=0.0
	for line in f1:
		total = total + 1
		x = line.split(' ')
		z = x[1].split('\n')
		x[1] = z[0]
#		print x[0],x[1]
		if x[0] == x[1]:
			correct = correct + 1

	f2.write(str((correct*100.0)/total)+'\n')
	f1.close()


def main():
	testfn(sys.argv[1])

if __name__ == '__main__':
	main()
