"""
Decrypts a given text file and prints the result. 
The other input is rotation value.
"""
if __name__ == "__main__":
	try:
		code = input("Enter you cipher message: ").strip()
		shift = int(input("Enter the rotation value: ").strip())
		plaintext = ''
		for char in code:
			ord_val = ord(char)
			isCaps = bool( ord('A') <= ord_val <= ord('Z') )
			if isCaps:
				ord_val = ord(char.lower()) # or  ord_val -= ord('A') - ord('a')
			ord_val -= ord('a')
			ord_val = ( ord_val - shift + 26 ) % 26
			ord_val += ord('a')
			if( isCaps ):
				ord_val = ord(chr(ord_val).upper()) # or ord_val += ord('A') - ord('a')
			plaintext += chr(ord_val)
		print("Your plaintext message was: ",plaintext)
	except ValueError as ve:
		print(ve)
