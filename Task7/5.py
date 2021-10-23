alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def char_to_int(char):
    for i in range(len(alphabet)):
        if char == alphabet[i]: return i
    return -1

def vigenere_encrypt(m, k):
    mes = m.replace(" ", "").lower()
    str = ""
    for i in range(len(mes)):
        str += alphabet[(char_to_int(mes[i]) + char_to_int(k[i % len(k)])) % len(alphabet)]
    return str.upper()

def vigenere_decrypt(c, k):
    ciph = c.replace(" ", "").lower()
    str = ""
    for i in range(len(ciph)):
        str += alphabet[(char_to_int(ciph[i]) - char_to_int(k[i % len(k)])) % len(alphabet)]
    return str.lower()

if __name__ == '__main__':
    #Task a
    print("Task a:")
    m = "Snart helg"
    k = "torsk"
    print(f"Message m: {m}")
    print(f"Key k: {k}")
    print(f"Cipher c = {vigenere_encrypt(m, k)}")

    print("\n\nTask b:")
    c = "QZQOBVCAFFKSDC"
    k = "brus"
    print(f"Cipher c: {c}")
    print(f"Key k: {k}")
    print(f"Message m = {vigenere_decrypt(c, k)}")
