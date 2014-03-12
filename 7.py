#!/usr/bin/python
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy
import sys
import random 
import string

def testfn(filename):
	f1=open(filename,'rU')
	a=[]
	s1=[]
	p1=[]
	s2=[]
	p2=[]
	s3=[]
	p3=[]
	a.append('Iris-setosa\n')
	a.append('Iris-versicolor\n')
	a.append('Iris-virginica\n')
	maxx=0.0
	maxy=0.0
	av1x=0
	av1y=0
	av2x=0
	av2y=0
	av3x=0
	av3y=0
	y=[]
	for line in f1:
		x=line .split(',')
		x.pop(0)
		x.pop(2)
		if maxx<float(x[0]):
			maxx=float(x[0])
		if maxy<float(x[1]):
			maxy=float(x[1])
		x[0]=float(x[0])
		x[1]=float(x[1])
		y.append(x)
		for j in range(3):
			if x[2] == a[j]:
				if j==0:
					s1.append(x[0])
					p1.append(x[1])
					av1x=av1x+x[0]
					av1y=av1y+x[1]
				if j==1:
					s2.append(x[0])
					p2.append(x[1])
					av2x=av2x+x[0]
					av2y=av2y+x[1]
				if j==2:
					s3.append(x[0])
					p3.append(x[1])
					av3x=av3x+x[0]
					av3y=av3y+x[1]
	f1.close()
	av1x= av1x/50.0
	av2x= av2x/50.0
	av3x= av3x/50.0
	av1y= av1y/50.0
	av2y= av2y/50.0
	av3y= av3y/50.0

	dbx=[]
	dby=[]
	ind=0
	preind=0
	i=0.0
	j=0.0
	print x,
	x=y
	while i<5:
		j=0
		while j<8:
			dist=1000000
			preind=ind
			mine=10000000
			for k in range(150):
				if mine>pow(x[k][0]-i,2)+pow(x[k][1]-j,2):
					mine=pow(x[k][0]-i,2)+pow(x[k][1]-j,2)
					if x[k][2]=='Iris-setosa\n':
						ind=1
					elif x[k][2]=='Iris-versicolor\n':
						ind=2
					else :
						ind=3
			if preind !=ind:
				dbx.append(i)
				dby.append(j)
			j=j+0.1
		i=i+0.1
	print dbx,
	plt.plot(s1, p1, 'ro', s2, p2, 'gs', s3, p3, 'b^',dbx, dby,'bx', 5, 8)
	plt.show()

def main():
	testfn(sys.argv[1])

if __name__ == '__main__':
	main()

