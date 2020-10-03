# simple interest formula is I1 = P x R x T.
# compound interest formula is I2 = P(1 + R/n) ^ nT.
"""
	Program: invest.py
	Author: Harmouch

	1. The inputs are
	starting investment amount. (principal)
	number of years.
	interest rate (an integer percent)

	2. The report is displayed in tabular form with a header.

	3. Computations and outputs:
	for each year
	compute the interest and add it to the investment
	print a formatted row of results for that year

	4. The ending investment and interest earned are also
	displayed.
"""
import sys
if __name__ == "__main__":
	try:
		p_initial = float(input("[*] Enter the initial capital: ")) # principal = ... $
		R = float(input("[*] Enter the rate ( between 0 and 1 ): "))# the interest rate is ...%
		T = int(input("[*] Enter the number of years: ")) # the term is ... years.
		n = int(input("[*] Enter the number of compound in a year: "))  
	except ValueError:
		sys.exit("Please provide valid input!")
	# Display the header.
	print(f"{'Year': <5} {'Initial Capital': <20} {'Compound Interest': <20} {'Simple Interest': <20} {'Ending balance': <20}")
	p_compound = 0
	for year in range(1,T+1):
		p_compound = p_initial * (1 + R/n) ** (n*year)
		p_simple = p_initial * R * year
		print(f"{year:<5} {p_initial:<20} {p_compound - p_initial:<20.2f} {p_simple:<20.2f} {p_compound:<20.2f}")
	# Display the totals for the period
	print(f"Ending balance: {p_compound:<10.2f}$")
	print(f"Total interest earned: {p_compound - p_initial:<10.2f}$")
