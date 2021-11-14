def rsa_encrypt(m, e, n):
    return (m ** e) % n


def rsa_decrypt(c, d, n):
    return (c ** d) % n


def rsa_sign(x, a, n):
    return rsa_decrypt(x, a, n)


def rsa_verify(x, y, b, n):
    """
    Verifies an rsa signature
    :param x: The message value to be compared with (Could be the message itself or a hash of the message (recommended))
    :param y: The signature attached to the message.
    :param b: Part of the public key of the message sender.
    :param n: Part of the public key of the message sender.
    :return: True/False
    """
    return x == rsa_encrypt(y, b, n)


if __name__ == '__main__':
    # Bob's keys
    n_b = 23 * 19
    a_b = 61
    b_b = 13

    # Verify messages from Bob
    print("Task 1:")
    m_1 = (78, 394)
    m_2 = (123, 289)
    print(f"m_1 is valid: {rsa_verify(m_1[0], m_1[1], b_b, n_b)}")
    print(f"m_2 is valid: {rsa_verify(m_2[0], m_2[1], b_b, n_b)}")

    # Sending message from Alice to Bob
    print("\nTask 4:")
    # Alice's keys
    n_a = 17 * 43
    a_a = 19
    b_a = 283
    message = 109
    # Signing with Alice's private key
    sign_val = rsa_sign(message, a_a, n_a)
    # Encrypting message and signing with Bob's public key
    cipher = (rsa_encrypt(message, b_b, n_b), rsa_encrypt(sign_val, b_b, n_b))
    print(f"Signed and encrypted message: {cipher}")