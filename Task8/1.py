def find_divisors(num: int) -> [int]:
    out = []
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            out.append(i)
    return out


if __name__ == '__main__':
    # Task a
    print("Task a:")
    print(f"Divisors of 72: {find_divisors(72)} are possible key lengths.")

    # Task b
    print("\n\nTask b:")
    m = "LPÆLZJWKKBGYÅMFGWÆÆYYMBKVÆRYAÆFOFJGOMDDZIVGFÆØRXMYYRLZQÆIBXYÅÆYGKHSKLING"
    print(len(m))
