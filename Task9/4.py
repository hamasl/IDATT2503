import numpy as np


def pollard_p_minus_one_unknown_a(n, b):
    for i in range(2, n):
        a = i ** (np.math.factorial(b)) % n
        if (F := np.gcd(a - 1, n)) > 1:
            return F


if __name__ == '__main__':
    print("Task a:")
    n_a = 1829
    ans = pollard_p_minus_one_unknown_a(n_a, 5)
    print(f"ans: {ans}")
    print(f"n/ans: {n_a / ans}")
