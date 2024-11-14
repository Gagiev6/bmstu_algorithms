def check_unique_elements(arr):
    return len(arr) == len(set(arr))
array = [1, 2, 3, 4, 5]
print(check_unique_elements(array))
array_with_duplicates = [1, 2, 3, 4, 4]
print(check_unique_elements(array_with_duplicates))