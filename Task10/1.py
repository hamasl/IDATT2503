def find_order(a, num_of_z):
    for i in range(1, num_of_z):
        if (a ** i) % num_of_z == 1:
            return i
    return -1


def do_task_one():
    z = 11
    for i in range(1, z):
        print(f"Order of element {i} in Z_{z} is {find_order(i, z)}")


def find_discrete_logarithm(alpha, beta, z):
    for i in range(z):
        if (alpha ** i) % z == beta:
            return i
    return None


def do_task_two():
    print("{:<26}{:<4}".format("", "beta"))
    print("{:<12}".format(""), end="")
    b_range = range(1, 11)
    for i in b_range:
        print(i, end="   ")
    print("")
    print("{:<10}----------------------------------------".format(""))
    for a in range(2, 11):
        print("{:<7}{:<2}|  ".format("" if a != 5 else "alpha", a), end="")
        for b in b_range:
            print(ans if (ans := find_discrete_logarithm(a, b, 11)) is not None else "x", end="   ")
        print("")


if __name__ == '__main__':
    print("Task 1:")
    do_task_one()
    print("\n\nTask 2:\n")
    do_task_two()
