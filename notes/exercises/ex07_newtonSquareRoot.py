# MIT License
# Copyright (c) 2022 Mahmoud Harmouch
"""
Compute the square root of a number.
1. The input is a number.
2. The outputs are the program's estimate of the square root
using Newton's method of successive approximations, and
Python's own estimate using math.sqrt.

• real value : 1.414235624 (sqrt(2))
• formula: new_estimate = old_estimate/2 + x/(old_estimate * 2)
• old_estimate = 1 # initial guess of sqrt(2) (x = 2)
• new_estimate = old_estimate/2 + 1 = 1.5
• new_estimate = new_estimate/2 + 2/3 = 1.41666
• new_estimate = 0.7083 + 2/2.833 = 1.41425

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
