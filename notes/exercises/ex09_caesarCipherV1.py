# MIT License
# Copyright (c) 2022 Mahmoud Harmouch
"""
Encrypts an input message and prints its cipher result. 
The other input is rotation value.
"""
if __name__ == "__main__":
	try:
		plaintext = input("Enter you text message: ").strip()
		shift = int(input("Enter the rotation value: ").strip())
		code = ''
		for char in plaintext:
			ord_val = ord(char)
			isCaps = bool( ord('A') <= ord_val <= ord('Z') )
			if isCaps:
				ord_val = ord(char.lower()) # or  ord_val -= ord('A') - ord('a')
			ord_val -= ord('a')
			ord_val = ( ord_val + shift + 26 ) % 26
			ord_val += ord('a')
			if( isCaps ):
				ord_val = ord(chr(ord_val).upper()) # or ord_val += ord('A') - ord('a')
			code += chr(ord_val)
		print(code)
	except ValueError as ve:
		print(ve)

