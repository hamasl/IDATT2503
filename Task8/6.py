def get_hash(x):
    """
    Gets hash from x**2 then using the numbers from position 10**6, 10**5 and 10**4
    :param x:
    :return:
    """
    return int(str(x ** 2)[-7:-4])


if __name__ == '__main__':
    freq = [0] * 1000
    for i in range(100_000, 1_000_000):
        freq[get_hash(i)] += 1
    freq_sum = sum(freq)
    rel_freq = [0] * 1000
    for i in range(1000):
        rel_freq[i] = freq[i] / freq_sum
        hash_val = "{0:0=3d}".format(i)
        print(f"Hash value: {hash_val}, has relative frequency of {rel_freq[i]}")
    rel_freq_min = min(rel_freq)
    rel_freq_max = max(rel_freq)
    print(f"Max relative frequency is {rel_freq_max}")
    print(f"Min relative frequency is {rel_freq_min}")
    print(f"Diff between max and min frequency {rel_freq_max - rel_freq_min}")
