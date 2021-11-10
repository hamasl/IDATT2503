def cbc_mac(x, blocks, encrypt_func):
    # 0b0 is IV
    y = [0b0]
    for i in range(blocks):
        y.append(encrypt_func(y[i] ^ x[i]))
    return y[blocks]


def caesar(val):
    return (val + 3) % 2 ** 4


def print_bin_list(bin_list):
    for binary in bin_list:
        print("{:04b}".format(binary), end=" ")


if __name__ == '__main__':
    x = [0b1101, 0b1111, 0b1010, 0b0001]
    x_marked = [0b0010, 0b1100, 0b0001, 0b1111]
    print("CBC-Mac for:", end=" ")
    print_bin_list(x)
    print("\nIs:", end=" ")
    print("{:04b}".format(cbc_mac(x, 4, caesar)))

    print("\n\nCBC-Mac for:", end=" ")
    print_bin_list(x_marked)
    print("\nIs:", end=" ")
    print("{:04b}".format(cbc_mac(x_marked, 4, caesar)))
