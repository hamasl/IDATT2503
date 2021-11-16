def shanks_algorithm(p, alpha, beta):
    m = int(p ** (1 / 2)) + 1
    dictionary = {}
    for j in range(m):
        dictionary[(alpha ** (m * j)) % p] = j
    for i in range(m):
        if (val := (beta * pow(alpha, -i, p) % p)) in dictionary:
            return m, i, dictionary[val]

    return None


if __name__ == '__main__':
    m_ans, i_ans, j_ans = shanks_algorithm(41, 6, 3)
    print("Shanks algorithm:")
    print(f"a is m*j+i = {m_ans}*{j_ans}+{i_ans} = {m_ans * j_ans + i_ans}")
