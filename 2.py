#!/usr/bin/python
import sys
import random
import string

def testfn(infile,trainfile,testfile):
	f2=open(trainfile, 'w')
	f3=open(testfile, 'w')
	
	i=0
	j=0
	a = []
	b = []
	c = []
	
	f1=open(infile, 'rU')
	for line in f1:
		if i==0:
			z1=line.split(',')
			for z2 in z1:
				i = i+1
	f1.close()
	print i
	
	f1=open(infile, 'rU')
	for line in f1:
		a.append(j)
		y=line.split(',')
		c.append(y[i-1])
		b.append(line)
		j=j+1
	random.shuffle(a)
#	print c,
	f1.close()

	flag=[]
	
	for x in range(j):
		if c[x] not in flag:
			flag.append(c[x])

	print flag
	f1=open(infile, 'rU')
	for x in range(j):
		if c[a[x]] not in flag:
			flag.append(c[a[x]])	
			f2.write(b[x])
		else:
			f3.write(b[x])
			flag.remove(c[a[x]])

		
	f1.close()
	f2.close()
	f3.close()

def main():
	testfn(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
	main()
