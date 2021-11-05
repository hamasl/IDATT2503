
def a(z, i):
    return (z[i-4] + z[i-3] + z[i-2] + z[i-1])%2

def b(z, i):
    return (z[i-4] + z[i-1])%2

def do_task(z0, f, k):
    z = z0.copy()
    for i in range(4, k):
        z.append(f(z,i))
    print(z0 in z[4:-1])
    print(z)

if __name__ == '__main__':
    z1 = [1,0,0,0]
    z2 = [0,0,1,1]
    z3 = [1,1,1,1]
    print("Task a 1:")
    do_task(z1, a, 15)
    print("\nTask a 2:")
    do_task(z2, a, 15)
    print("\nTask a 3:")
    do_task(z3, a, 15)


    print("\nTask b 1:")
    do_task(z1, b, 20)

    print("\nTask b 2:")
    do_task(z2, b, 20)

    print("\nTask b 3:")
    do_task(z3, b, 20)
