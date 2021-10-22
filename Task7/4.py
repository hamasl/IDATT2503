
alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def char_to_int(char):
    for i in range(len(alphabet)):
        if char == alphabet[i]: return i
    return -1

def str_to_int_array(str):
    int_array = []
    for char in str:
        int_array.append(char_to_int(char))
    return int_array

def decrypt_shift_cipher(c, k):
    res = []
    for i in c:
        res.append((i-k)%len(alphabet))
    return res

def int_array_to_str(int_array):
    str = ""
    for i in int_array:
        str += alphabet[i]
    return str

if __name__ == '__main__':
    cipher = "YÆVFB VBVFR ÅVBV".replace(" ", "").lower()
    cipher_int_array = str_to_int_array(cipher)
    for k in range(len(alphabet)):
        print(f"k: {k}, decrypted text: {int_array_to_str(decrypt_shift_cipher(cipher_int_array, k))}")