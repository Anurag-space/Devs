def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Taking input from the user
user_input = input("Enter elements separated by space: ")
user_list = [int(x) for x in user_input.split()]

# Sorting the list using insertion sort
insertion_sort(user_list)

# Printing the sorted list
print("Sorted list:", user_list)
