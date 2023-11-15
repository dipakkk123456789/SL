def greedy_selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == "__main__":
    # Take input from the user
    input_array = list(map(int, input("Enter space-separated numbers: ").split()))

    print("Input Array:", input_array)

    sorted_array = greedy_selection_sort(input_array.copy())
    print("Sorted Array:", sorted_array)
