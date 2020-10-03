"""
Encrypts an input message(lowercase only) and prints the result. 
The other input is rotation value.
"""
if __name__ == "__main__":
	plainText = input("Enter a message : ").strip().lower()
	rot_val = int(input("Enter the rotation value : "))%26
	cipher = ""
	for char in plainText:
		ordvalue = ord(char)
		cipherValue = ordvalue + rot_val
		'''
		| ord('a')--------ordvalue----------------ord('z') | -----ordvalue + rot_val----- ord('A')|
		'''
		if cipherValue > ord('z'):
			cipherValue = ord('a') + rot_val - (ord('z') - ordvalue + 1)
		cipher += chr(cipherValue)
	print("The cipher message is : ",cipher)
