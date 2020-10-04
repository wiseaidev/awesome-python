# https://pypi.org/project/mod/
from mod import Mod
def isprime1(number):
	# fast
	return number > 1 if number <=  3 else len([x for x in range(2, int(number**0.5) + 1) if number % x == 0]) == 0

def isprime2(number):
	# Fermat's Little Theorem
	# https://brilliant.org/wiki/fermats-little-theorem/
	# slow
	return number > 1 if number <=  3 else len([b for b in range(2,number) if b**(number) != Mod(b,number)]) == 0 

def arecoprime(a, b):
	return False if len([i for i in range(2, min(a, b) + 1) 
		if a % i == 0 and b % i == 0]) != 0 else True

def coprimes(number):
	return (i for i in range(2, number + 1) if arecoprime(i,number))

if __name__ == "__main__":
	try:
		number = int(input("Enter you number: "))
		print(f"coprimes with {number} are: {list(coprimes(number))} ",end="\n\n")
		primes0 = []
		primes1 = []
		for i in range(1,number + 1):
			if isprime1(i):
				primes0.append(i)
			#if isprime2(i):
			#	primes1.append(i)
		print(f"Primes of numbers lower than {number} are: {primes1}")
		#assert len(primes1) == len(primes0)
		assert arecoprime(11, 23)
		assert not arecoprime(9, 12)
	except ValueError as e:
		print(e)