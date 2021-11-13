def is_primitive_element(a, num_of_z):
    for i in range(1, num_of_z):
        if (a ** i) % num_of_z == 1:
            return i == num_of_z - 1
    return False


def do_task_three():
    z = 17
    for i in range(1, z):
        if is_primitive_element(i, z):
            print(f"{i} is a primitive element in Z_{z}")


if __name__ == '__main__':
    print("Task 3:")
    do_task_three()
