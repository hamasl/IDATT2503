def extended_euclidean_algorithm(a, b):
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0 // b0
    r = a0 - q * b0
    while r > 0:
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0 // b0
        r = a0 - q * b0
    r = b0
    return r, s, t


def square_and_multiply(x: int, c: int, n: int):
    z = 1
    for i in range(len(bin(c)) - 1, -1, -1):
        z = z ** 2 % n
        if ((c >> i) & 1) == 1:
            z = (z * x) % n
    return z


if __name__ == '__main__':
    print("Task d:")
    phi_n = 1120
    e = 3
    res = extended_euclidean_algorithm(phi_n, e)
    d = res[2] % phi_n
    print(f"Extended euclidean algorithm with phi_n: {phi_n} and e: {e} =  {res}")
    print(f"d is {d}")

    print("\n\nTask e:")
    n = 1207
    orig_m = 42
    cipher = square_and_multiply(orig_m, e, n)
    message = square_and_multiply(cipher, d, n)
    print(f"Original message: {orig_m}")
    print(f"Cipher computed by square and multiply (({orig_m}**{e})%{n}): {cipher}")
    print(f"Message computed by square and multiply (({cipher}**{d})%{n}): {message}")
