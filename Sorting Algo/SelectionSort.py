def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            if(arr[j] < arr[min_index]):
                min_index = j
            
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

unsorted_list = [5,4,3,2,1]                                  #[12, 25, 11, 34, 90, 22]
sorted_list = selection_sort(unsorted_list)
print("Sorted Elements: ", sorted_list)