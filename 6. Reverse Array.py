

def reverse_array(arr, left_index=0):
    if left_index == len(arr)//2:
        return
    right_index = len(arr) - 1 - left_index
    arr[right_index], arr[left_index] = arr[left_index], arr[right_index]
    reverse_array(arr, left_index + 1)


array = [el for el in input().split()]

reverse_array(array)

print(*array)
