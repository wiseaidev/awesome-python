# MIT License
# Copyright (c) 2022 Mahmoud Harmouch
"""
File: base10tobaseX.py
Converts a decimal integer to a string of digits of baseX.
"""
if __name__ == "__main__":
	try:
		newBasexNumber = ''
		decimal = int(input("Please enter your decimal integer: "))
		baseX = int(input("Please enter baseX(>=2): "))
		if decimal == 0 or baseX <=1:
			print("0")
		else:
			print(f"{'Quotient': <15}{'Remainder': ^15}{'New_Number': >20}")
			while decimal > 0:
				quotient,remainder = divmod(decimal,baseX)
				decimal = quotient
				newBasexNumber = str(remainder) + newBasexNumber
				print(f"{decimal: <15}{remainder: ^15}{newBasexNumber: >20}")

		print(f"Your number representation in base[{baseX}] : {newBasexNumber}")
	except ValueError:
		print("Please enter a valid integer!!!")
	except Exception:
		print("unexpected error occured!!!")
