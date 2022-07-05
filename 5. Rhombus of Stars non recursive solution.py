def generate_rombus(number):
    for el in range(1, number):
        print(el * "*")
    for el in range(number, 0, -1):
        print(el * "*")
    return


num = int(input())
generate_rombus(num)
