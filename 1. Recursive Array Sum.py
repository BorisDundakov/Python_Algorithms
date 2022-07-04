def array_sum(array_numbers, idx=0):
    if idx == len(array_numbers) - 1:
        return array_numbers[idx]
    return array_numbers[idx] + array_sum(array_numbers, idx + 1)


numbers_array = [1, 3, 2, 4]
print(array_sum(numbers_array))
