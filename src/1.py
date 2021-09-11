# Array - Reverse the array

def reverse_the_array_iterative(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


def reverse_the_array_recursive(array, start, end):
    if start >= end:
        return
    array[start], array[end] = array[end], array[start]
    reverse_the_array_recursive(array, start + 1, end - 1)


def reverse_the_array_list_slicing(array):
    return array[::-1]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8]

    # reversing via iteration
    arr = A.copy()
    print(reverse_the_array_iterative(arr))

    # reversing via recursion
    arr = A.copy()
    reverse_the_array_recursive(arr, 0, len(arr) - 1)
    print(arr)

    # reversing via list slicing
    arr = A.copy()
    print(reverse_the_array_list_slicing(arr))
