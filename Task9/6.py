def factor_n(n, num_of_tries):
    """
    Factors n into p and q.
    :param num_of_tries: The number of d-values to be tested.
    :param n: p*q
    :return: q and p, where q > p > 2
    """
    for d in range(num_of_tries):
        s = int((n + d ** 2) ** (1 / 2))
        q = s + d
        p = s - d
        if p * q == n:
            return p, q
    return -1, -1


if __name__ == '__main__':
    print("Task d:")
    n_e = 152416580095517
    p,q = factor_n(n_e, 10)
    print(f"Factorizing n = {n_e}:")
    print(f"p = {p}")
    print(f"q = {q}")
