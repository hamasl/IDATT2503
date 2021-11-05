def encrypt_simple_aes_128(inp: [int], key: [int]) -> [int]:
    keyed_inp = add_round_key(inp, key)
    print(keyed_inp)
    byte_matrix = [[-1] * 4 for _ in range(4)]
    for i in range(len(inp)):
        byte_matrix[i % 4][i // 4] = keyed_inp[i]
    print(byte_matrix)


def decrypt_simple_aes_128(inp: [int]) -> [int]:
    print("hei")


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


def add_round_key(inp: [int], round_key: [int]) -> [int]:
    if len(inp) != len(round_key):
        raise Exception("Block and key size must match")
    out = []
    for i in range(len(inp)):
        out.append(inp[i] ^ round_key[i])
    return out


def shift_rows(inp: [[int]]) -> [[int]]:
    out = []
    for i in range(len(inp)):
        new_row = [-1] * len(inp[i])
        for j in range(len(inp[i])):
            new_row[(j - i) % len(inp[i])] = inp[i][j]
        out.append(new_row)
    return out


if __name__ == '__main__':
    key = "67 71 35 c4 ff da e5 ff 1c 54 e1 fd 7f 2e 88 b7"

    # Task a
    m = "24 59 66 0c 99 da 9b 00 d6 55 fd 20 e9 ff 46 95"

    # Task b
    c = "26 FA 83 E7 2D CD 5D B8 C4 DC EB 12 70 CF D16 1E"
    print(hex_to_byte_list(key))
    print(byte_list_to_hex(hex_to_byte_list(key)))

    print(shift_rows([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))

    encrypt_simple_aes_128(hex_to_byte_list(m), hex_to_byte_list(key))
