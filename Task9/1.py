def hash_method(val):
    hashed = val ** 2 % (2 ** 8)
    return (hashed >> 2) & 0b001111


def append_bitstring(x, y, block_size):
    return (x << block_size) + y


def simple_hmac(x, k, ipad, opad, func):
    k_opad = k ^ opad
    k_ipad = k ^ ipad
    inner_hashed = hash_method(append_bitstring(k_ipad, x, 4))
    return hash_method(append_bitstring(k_opad, inner_hashed, 4))

if __name__ == '__main__':
    print("Task a:")
    print("{:04b}".format(simple_hmac(0b0110, 0b1001, 0b0011, 0b0101, hash_method)))
    print("\nTask b:")
    print("{:04b}".format(simple_hmac(0b0111, 0b1001, 0b0011, 0b0101, hash_method)))

