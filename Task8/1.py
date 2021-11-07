alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def find_divisors(num: int) -> [int]:
    out = []
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            out.append(i)
    return out


def char_to_int(char):
    for i in range(len(alphabet)):
        if char == alphabet[i]: return i
    return -1

def vigenere_decrypt(c, k):
    ciph = c.replace(" ", "").lower()
    str = ""
    for i in range(len(ciph)):
        str += alphabet[(char_to_int(ciph[i]) - char_to_int(k[i % len(k)])) % len(alphabet)]
    return str.lower()

def print_decrypted(cipher, key):
    print(f"\n\nkey: {k}")
    print(f"message: {vigenere_decrypt(cipher, k)}")

if __name__ == '__main__':
    # Task a
    print("Task a:")
    print(f"Divisors of 72: {find_divisors(72)} are possible key lengths.")

    # Task b
    print("\n\nTask b:")
    c = "LPÆLZJWKKBGYÅMFGWÆÆYYMBKVÆRYAÆFOFJGOMDDZIVGFÆØRXMYYRLZQÆIBXYÅÆYGKHSKLING"
    k = "g"
    print_decrypted(c, k)

    k = "ng"
    print_decrypted(c, k)

    k="rg"
    print_decrypted(c, k)

    k = "ing"
    print_decrypted(c, k)

    k = "ring"
    print_decrypted(c, k)

    k = "mng"
    print_decrypted(c, k)

    k = "ling"
    print_decrypted(c, k)

    k = "ping"
    print_decrypted(c, k)

    k = "skling"
    print_decrypted(c, k)

    k = "elskling"
    print_decrypted(c, k)

    k = "wkling"
    print_decrypted(c, k)

    """
    k = "khskling"
    print_decrypted(c, k)

    k = "ohskling"
    print_decrypted(c, k)

    k = "gkhskling"
    print_decrypted(c, k)

    k = "kkhskling"
    print_decrypted(c, k)

    k = "åæygkhskling"
    print_decrypted(c, k)

    k = "dæygkhskling"
    print_decrypted(c, k)

    k = "qæibxyåæygkhskling"
    print_decrypted(c, k)

    k = "uæibxyåæygkhskling"
    print_decrypted(c, k)

    k = "myyrlzqæibxyåæygkhskling"
    print_decrypted(c, k)

    k = "qyyrlzqæibxyåæygkhskling"
    print_decrypted(c, k)

    k = "mddzivgfæørxmyyrlzqæibxyåæygkhskling"
    print_decrypted(c, k)

    k = "qddzivgfæørxmyyrlzqæibxyåæygkhskling"
    print_decrypted(c, k)
    """
