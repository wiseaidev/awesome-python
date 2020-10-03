def is_palindrome_v0(string): 
	"""check if the string is palindrome or not.(for loop)
	you need to iterate over the half of the string only"""
	for i in range(int(len(string)/2)):
		if string[i] != string[-1-i]:
			return False
		else:
			continue
	return True

def is_palindrome_v1(string):
	"""check if the string is palindrome or not.(while loop)"""
	i, n = 0, len(string) - 1
	while i < n and string[i] == string[n]:
		i += 1
		n -= 1
	return n <= i

def is_palindrome_v2(string):
	"""check if the string is palindrome or not.
	 if 2 chars are palindrome pop the last item"""
	letters = list(string)
	for letter in letters:
		if letter == letters[-1]:
			letters.pop(-1)
		else:
			return False
	return True

def is_palindrome_v3(string):
	"""check if the string is palindrome or not using the reversed 
	built-in method	and compare the two lists"""
	return list(string) == list(reversed(list(string)))

def is_palindrome_v4(string):
	"""check if the string is palindrome or not while checking if the 
	reversed string begin from index 0""" 
	return string.find(string[::-1]) == 0

def is_palindrome_v5(string):
	"""palindrome recursive version""" 
	if len(string) <= 1:
		return True
	if string[0] != string[-1]:
		return False
	else:
		return is_palindrome_v5(string[1:-1])

def is_palindrome_v6(string):
	"""palindrome: check if the first half of the string equal to the second half""" 
	return True if len(string)<=1 else string[:len(string)//2] == string[-(len(string)//2):][::-1]
# running code
s = "12"
ans0 = is_palindrome_v0(s)
ans1 = is_palindrome_v1(s)
ans2 = is_palindrome_v2(s)
ans3 = is_palindrome_v3(s)
ans4 = is_palindrome_v4(s)
ans5 = is_palindrome_v5(s)
ans6 = is_palindrome_v6(s)
print(ans0, ans1, ans2, ans3, ans4, ans5, ans6)