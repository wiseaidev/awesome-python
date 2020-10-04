def isPerfect(number):
	"""using generator expressions"""
	return sum((divisor for divisor in range(1, number) if number % divisor == 0)) == number

def divisors(number):
	"""using generator functions to return a divisor"""
	for divisor in range(1,number):
		if number % divisor == 0:
			yield divisor

def perfect_list(number):
	return [i for i in range(2, number) if isPerfect(i)]

def sum_(number):
	divisors = list(divisor for divisor in range(1,number) if number % divisor == 0)
	if sum(divisors) == number:
		print('{} = '.format(number) + ' + '.join(str(divisor) for divisor in divisors))

if __name__ == "__main__":
	try:
		number_ = int(input("Enter your number: "))
		for number in perfect_list(number_):
			divisors = list(divisor for divisor in range(1,number) if number % divisor == 0)
			if sum(divisors) == number:
				print('{} = '.format(number) + ' + '.join(str(divisor) for divisor in divisors))
	except ValueError as e:
		print(e)