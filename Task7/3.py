alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def f(x):
    return (11*x-5)%len(alphabet)


def f_inverse(y):
    return 8*(y-24)%len(alphabet)

if __name__ == '__main__':
    # Task a
    print("Task a:")
    for i in range(len(alphabet)):
        res = f(i)
        print(f"f({alphabet[i]}) = f({i}) = {res} = {alphabet[res]}")

    print("\n\nTask c:")
    for i in range(len(alphabet)):
        res = f_inverse(i)
        print(f"f_inverse({alphabet[i]}) = f_inverse({i}) = {res} = {alphabet[res]}")

