def binary_search(arr, target):
    # write your binary search code here
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid+1
        if target < arr[mid]:
            right = mid - 1
    return -1

nums = [1, 3, 5, 7, 9, 11, 15]
target = 7

print(binary_search(nums, target))