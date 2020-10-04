# pythagorean triplets in a range(n): (x,y,z) : x**2 + y**2 = z**2

import math
def pyTriplet_V0(n):
	"""returns a pythagorean triplets using generator expressions.
	x < y < z
	"""
	return ((x, y, z) 
	for x in range(1, n+1) 
	for y in range(x+1, n+1)
	for z in range(y+1, n+1) 
	if x**2 + y**2 == z**2)

def pyTriplet_V1(n):
	"""returns a pythagorean triplets using generator functions. aka lazy tuples ;-)
	x < y < z
	source : https://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets#lang-py%20s-code-block%20hljs%20python
	"""
	for z in range(1, n+1):
		z2= z*z # avoid computing z*z for each iteration in the while loop
		x= x2= 1; xstep= 3
		y= z - 1; y2= y*y; ystep= 2*y - 1
		while x < y:
			x2_y2= x2 + y2
			if x2_y2 == z2:
				yield x, y, z
				x+= 1; x2+= xstep; xstep+= 2
				y-= 1; y2-= ystep; ystep-= 2
			elif x2_y2 < z2:
				x+= 1; x2+= xstep; xstep+= 2
			else:
				y-= 1; y2-= ystep; ystep-= 2

if __name__ == "__main__":
	try:
		number = int(input("Enter your number: "))
		triplets0 = pyTriplet_V0(number)
		triplets1 = pyTriplet_V1(number)
		print(list(triplets0),end='\n\n')
		print(sorted(list(triplets1)))
	except ValueError as e:
		print(e)