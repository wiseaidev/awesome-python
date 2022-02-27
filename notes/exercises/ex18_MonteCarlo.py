# MIT License
# Copyright (c) 2022 Mahmoud Harmouch

# Pi extimation
# Great explanation: https://brilliant.org/wiki/monte-carlo/

import random, math

def pi_montecarlo(a, b, n):
    return 4 * (b -a ) * sum(math.sqrt(1 - random.uniform(a, b)**2) 
        for i in range(n)) / n
if __name__ == "__main__":
    n = int(input("Enter the number of iterations: "))
    print('|' + '-'*98 + '|')
    print(f"|{'n':<24}|{'approximation':^24}|{'absolute error':^24}|{'relative error':^23}|")
    print('|' + '-'*98+ '|')
    for i in range(1,n):
        n = 10 ** i
        approx = pi_montecarlo( 0, 1, n)
        error = math.pi - approx
        print(f'|{n:<24}|{approx:^24}|{error:^24}|{abs(error)/math.pi:^23}|')
