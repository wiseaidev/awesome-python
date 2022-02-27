# MIT License
# Copyright (c) 2022 Mahmoud Harmouch
"""
Prints the median of a set of numbers in a file.
"""
if __name__ == "__main__":
	try:
		f = open("numbers.txt", 'r')
		# Input the text, convert it to numbers, and
		# add the numbers to a list
		numbers = []
		for i,line in enumerate(f):
			words = line.strip().split(" ")
			numbers += list(float(word)for word in words)
		# Sort the list and print the number at its midpoint
		numbers.sort()
		midpoint = len(numbers) // 2
		print("The median is", end = " ")
		if len(numbers) % 2 == 1:
			print(numbers[midpoint])
		else:
			print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
	except IOError as e:
		print(e) 
	except ValueError as ve:
		print(ve) 	