def encrypt_elgamal(p, alpha, beta, k, x):
    """
    p, alpha and beta is the public key.
    :param p:
    :param alpha:
    :param beta:
    :param k: Is a randomly chosen integer.
    :param x: Is the message.
    :return: Encrypted message.
    """
    return (alpha ** k) % p, (x * beta ** k) % p


def decrypt_elgamal(c1, c2, p, a):
    return c2 * pow(c1 ** a, -1, p) % p


def do_task_b():
    print(encrypt_elgamal(19, 13, 14, 6, 3))


def do_task_c():
    print(decrypt_elgamal(12, 11, 19, 5))


if __name__ == '__main__':
    print("Task b:")
    do_task_b()
    print("\nTask c:")
    do_task_c()
