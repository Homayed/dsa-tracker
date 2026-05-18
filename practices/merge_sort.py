def merge(left, right):
    # your merge two sorted lists logic here
    lst = []
    i = 0
    j = 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            lst.append(left[i])
            i = i + 1
        else:
            lst.append(right[j])
            j = j + 1
    lst.extend(left[i:])
    lst.extend(right[j:])
    return lst


def merge_sort(arr):
    # base case
    if len(arr)<=1:
        return arr
    # find middle
    mid = len(arr)//2
    # split left and right
    arr_left = arr[:mid]
    arr_right = arr[mid:]
    # recursively sort left
    sorted_left = merge_sort(arr_left)
    # recursively sort right
    sorted_right = merge_sort(arr_right)
    # merge sorted left and right
    return merge(sorted_left,sorted_right)



nums = [5, 2, 4, 6, 1, 3]

print("Before:", nums)
print("After:", merge_sort(nums))