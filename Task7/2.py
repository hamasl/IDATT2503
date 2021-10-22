def modulo_multiplication_table(n):
    res = []
    for i in range(1, n):
        row = []
        for j in range(1, n):
            row.append((i*j)%n)
        res.append(row)
    return res

def get_table_header(n):
    str = "{:<8}".format(" ")
    for i in range(1, n):
        str += "{:<8}".format(i)
    return str

def get_table_row(row, row_num):
    str = "{:<8}".format(row_num)
    for i in row:
        str += "{:<8}".format(i)
    return str

def get_multiplicative_inverse_entries(tab):
    table = []
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] == 1:
                table.append((i+1, j+1))
    return table

def perform_task(n):
    print(f"a*b%{n} multiplication table:\n")
    print(get_table_header(n))
    tab = modulo_multiplication_table(n)
    for i in range(len(tab)):
        print(get_table_row(tab[i], i + 1))
    return tab

def brute_force_multaplicative_inverse(n, a):
    for b in range(n):
        if (a*b)%n == 1:
            return b
    return None

if __name__ == "__main__":
    # Task a
    print("\n\nTask a:")
    tab = perform_task(12)

    # Task b
    print("\n\nTask b:")
    print(f"Entries with multiplicative inverses {get_multiplicative_inverse_entries(tab)}")

    # Task c
    print("\n\nTask c: ")
    tab = perform_task(11)
    print(f"\n\nEntries with multiplicative inverses {get_multiplicative_inverse_entries(tab)}")

    # Task d
    n = 29
    a = 11
    print("\n\nTask d:")
    print(f"{brute_force_multaplicative_inverse(n,a)} is the multiplicative inverse for {a} modulo {n}")