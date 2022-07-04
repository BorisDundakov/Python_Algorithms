# !5 = 5*4*3*2*1
# !5 = 5*4!

def recursive_factorial(num):
    if num == 0:
        return 1
    return num * recursive_factorial(num - 1)


number = int(input())

print(recursive_factorial(number))
