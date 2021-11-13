def shanks_algorithm(p, alpha, beta):
    m = int(p ** (1 / 2)) + 1
    dictionary = {}
    for j in range(m):
        dictionary[(alpha ** (m * j))%p] = j
    print(dictionary)
    for i in range(m):
        if (val := beta * pow(alpha, -i, p)) in dictionary:
            return m, i, dictionary[val]

    return None


if __name__ == '__main__':
    print(shanks_algorithm(41, 6, 3))
