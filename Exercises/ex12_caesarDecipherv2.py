"""
Decrypts a given text file and prints the result.
The other input is rotation value.
"""
if __name__ == "__main__":
	try:
		f = open("file.txt", 'r')
		shift = int(input("Enter the rotation value: ").strip())
		for i,line in enumerate(f):
			linecode = ''
			for char in line.strip():
				ord_val = ord(char)
				if ord('a') <= ord_val <= ord('z') or ord('A') <= ord_val <= ord('Z') :
					isCaps = bool( ord('A') <= ord_val <= ord('Z') )
					if isCaps:
						ord_val = ord(char.lower()) # or  ord_val -= ord('A') - ord('a')
					ord_val -= ord('a')
					ord_val = ( ord_val - shift + 26 ) % 26
					ord_val += ord('a')
					if( isCaps ):
						ord_val = ord(chr(ord_val).upper()) # or ord_val += ord('A') - ord('a')
					linecode += chr(ord_val)
				else:
					linecode += char
			print(linecode)
		f.close()
	except ValueError as ve:
		print(ve)
	except IOError as e:
		print(e) 