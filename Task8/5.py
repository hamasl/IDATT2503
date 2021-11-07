alphabet = "abcdefghijklmnopqrstuvwxyzæøå"


def char_to_int(char):
    for i in range(len(alphabet)):
        if char == alphabet[i]: return i
    return -1


def str_to_int_array(string):
    int_array = []
    for char in string:
        int_array.append(char_to_int(char))
    return int_array


def int_array_to_str(int_array):
    string = ""
    for i in int_array:
        string += alphabet[i]
    return string


def autokey_encrypt(inp: [int], key: [int]) -> [int]:
    out = []
    key_vals = [key]
    for i in range(len(inp)):
        out.append((inp[i] + key_vals[i]) % len(alphabet))
        key_vals.append(inp[i])
    return out


def autokey_decrypt(inp: [int], key: [int]) -> [int]:
    out = []
    key_vals = [key]
    for i in range(len(inp)):
        out.append((inp[i] - key_vals[i]) % len(alphabet))
        key_vals.append(out[i])
    return out


if __name__ == "__main__":
    # Task a
    print("Task a:")
    m = "goddag"
    k = 17
    c_as_ints = autokey_encrypt(str_to_int_array(m), k)
    print(f"Cipher as int values: {c_as_ints}")
    print(f"Cipher as string: {int_array_to_str(c_as_ints).upper()}")

    print("\n\nTask b:")
    c = "23 08 23 12 21 02 04 03 17 13 19"
    c = c.split(" ")
    c = [int(val) for val in c]
    k = 5
    m_as_ints = autokey_decrypt(c, k)
    print(f"Message as int values: {m_as_ints}")
    print(f"Message as string: {int_array_to_str(m_as_ints)}")

