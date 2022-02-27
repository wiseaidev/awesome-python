# MIT License
# Copyright (c) 2022 Mahmoud Harmouch
"""
Decrypts an encrypted message(lowercase only) and prints its plaintext result. 
The other input is rotation value.
"""
if __name__ == "__main__":
	cipher = input("Enter an encrypted message : ").strip().lower()
	rot_val = int(input("Enter the rotation value : "))%26
	plainText = ""
	for char in cipher:
		ordvalue = ord(char)
		plainValue = ordvalue - rot_val
		'''
		| ord('a')--------ordvalue----------------ord('z') | -----ordvalue + rot_val----- |
		'''
		if plainValue < ord('a'):
			plainValue = ord('z') - rot_val + (ord('a') - ordvalue + 1)
		plainText += chr(plainValue)
	print("The original message is : ",plainText)
