# cosine and sine approximation without using the factorial function!
# cos(x)= 1 - x**2/2! + x**4/4! - x**6/6! + ..
# sin(x)= x - x**3/3! + x**5/5! - x**7/7! + ..
# as you may notice 2! = 2*1; 4! = 4*3*2*1 = 4*3*(2!);
# 6! = 6*5*(4!); in general p! = p*(p-1)*[(p-2)!] knowing (p-2)!
# Taylor polynomial and Lagrange remainder
# formulas https://www.cusd80.com/cms/lib/AZ01001175/Centricity/Domain/5532/LaGrange_Error_Explanation.pdf
import math

def cosine(x, error):
    p = 0
    c = 0
    appr = 1
    term = 1
    reminder = abs(x - c)
    print(f"{'Iteration':<10}{'term':^25}{'approximation':^25}{'reminder':^25}{'error':^25}")
    while reminder > error:
        p += 2
        term *= - x**2 / (p * (p - 1))
        appr += term
        reminder *= abs(x - c)**2 / (p * (p + 1))
        print(f"{p-1:^10}{term:^25.15}{appr:^25.15}{reminder:^25.15}{error:^25.15}")
    return appr

def sine(x, error):
    p = 1
    c = 0
    appr = x
    term = 1
    reminder = abs(x - c)
    print(f"{'Iteration':<10}{'term':^25}{'approximation':^25}{'reminder':^25}{'error':^25}")
    while reminder > error:
        p += 2
        term *= - x**2 / (p * (p - 1))
        appr += term
        reminder *= abs(x - c)**2 / (p * (p + 1))
        print(f"{p-1:^10}{term:^25.15}{appr:^25.15}{reminder:^25.15}{error:^25.15}")
    return appr

if __name__ == "__main__":
    print("+------------------cosine approximation------------------+")
    try:
        number = int(input("Enter you number to compute the cosine/sine of it : "))
        error = float(input("Enter the error value : "))
        cos_number = cosine(number,error)
        sin_number = sine(number,error)
        print(f"Approximation of cos({number}) is: {cos_number:<30.25f}")
        print(f"cos({number}) using the math.cos built-in function: {math.cos(number):<30.25f}")
        print(f"Approximation of sin({number}) is: {sin_number:<30.25f}")
        print(f"sin({number}) using the math.cos built-in function: {math.sin(number):<30.25f}")
    except ValueError as e:
        print(e)

       

