def nested_loops(array, idx=0):
    if idx >= len(array):
        print(*array)
        return
    for num in range(1, len(array) + 1):
        array[idx] = num
        nested_loops(array, idx + 1)


n = int(input())
arr = [None] * n
nested_loops(arr)
