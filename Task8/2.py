RCon = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1B, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00]
]


def hex_to_byte_list(hex_str: str) -> [int]:
    out = []
    inp = hex_str.split(" ")
    for hex_num in inp:
        out.append(int(hex_num, 16))
    return out


def byte_list_to_hex(byte_list: [int]) -> str:
    out = []
    for byte in byte_list:
        out.append(format(byte, "x"))
    return " ".join(out)


def rot_word(inp: []) -> []:
    out = [0] * 4
    for i in range(len(inp)):
        out[(i - 1) % 4] = inp[i]
    return out


def sub_word(inp: []) -> []:
    """
    In this task sub word was defined to be Subword(x) = x
    :param inp: input array
    :return: output array
    """
    return inp.copy()


def xor_lists(a: [], b: []):
    """
    Treats a an b as lists of bytes and x-ors each element
    :param a:
    :param b:
    :return:
    """
    if len(a) != len(b):
        raise Exception("Byte lists needs the same length")
    out = []
    for i in range(len(a)):
        out.append(a[i] ^ b[i])
    return out


def key_expansion(key):
    w = []
    for i in range(4):
        w.append([key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]])
    for i in range(4, 44):
        temp = w[i - 1]
        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            temp = xor_lists(temp, RCon[(i // 4)-1])
        w.append(xor_lists(w[i - 4], temp))
    return w


if __name__ == '__main__':
    key = "2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C"
    words = key_expansion(hex_to_byte_list(key))
    for i in range(6):
        print(f"\n\nw[{i}]:")
        print(f"As byte list: {words[i]}")
        print(f"As hex: {byte_list_to_hex(words[i]).upper()}")
