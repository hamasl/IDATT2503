def decrypt(inp: [[]]) -> []:
    print("Hei")


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


if __name__ == '__main__':
    key = "67 71 35 c4 ff da e5 ff 1c 54 e1 fd 7f 2e 88 b7"

    # Task a
    m = "24 59 66 0c 99 da 9b 00 d6 55 fd 20 e9 ff 46 95"

    # Task b
    c = "26 FA 83 E7 2D CD 5D B8 C4 DC EB 12 70 CF D16 1E"
    print(hex_to_byte_list(key))
    print(byte_list_to_hex(hex_to_byte_list(key)))
