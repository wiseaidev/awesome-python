"""
Compute the square root of a number.
1. The input is a number.
2. The outputs are the program's estimate of the square root
using Newton's method of successive approximations, and
Python's own estimate using math.sqrt.
"""
import math
if __name__ == "__main__":
	try :
		# Receive the input number from the user
		x = float(input("Enter a positive number: "))
		# Initialize the tolerance and estimate
		tolerance = 0.000001
		estimate = 1.0
		# Perform the successive approximations
		while True:
			estimate = (estimate + x / estimate) / 2
			difference = abs(x - estimate ** 2)
			if difference <= tolerance:
				break
		# Output the result
		print("The program's estimate:", estimate)
		print("Python's estimate:", math.sqrt(x))
	except ValueError:
		print("ValueError exception has been raised!")
