import numpy as np


def pollard_p_minus_one(n, b):
    a = 2
    for i in range(2, b + 1):
        a = (a ** i) % n
    if 1 < (F := np.gcd(a - 1, n)) < n:
        return F
    return None


def pollard_p_minus_one_guess_b(n, max):
    for i in range(max):
        ans = pollard_p_minus_one(n, i)
        if ans is not None:
            return ans
    return None


if __name__ == '__main__':
    print("Task a:")
    n_a = 1829
    ans_a = pollard_p_minus_one(n_a, 5)
    print(f"ans: {ans_a}")
    print(f"n/ans: {n_a / ans_a}")

    print("\n\nTask c:")
    n_c = 6319
    ans_c = pollard_p_minus_one_guess_b(n_c, 12)
    print(f"ans: {ans_c}")
    print(f"n/ans: {n_c / ans_c}")
