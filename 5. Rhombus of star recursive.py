def generate_rombus(number):
    if number == 0:
        return
    print(number * "*")
    generate_rombus(number - 1)
    print(number * "*")


num = int(input())
generate_rombus(num)
