def insertion_sort(arr):
    # your insertion sort code here
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i>-1 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i -1
        arr[i+1] = key
    return arr


nums = [5, 2, 4, 6, 1, 3]

print("Before:", nums)
print("After:", insertion_sort(nums))