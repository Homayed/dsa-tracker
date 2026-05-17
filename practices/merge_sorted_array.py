def merge(left, right):
    # write your merge logic here
    lst = []
    i = 0
    j = 0
    while len(left)>i and len(right)>j:
        if left[i]<right[j]:
            lst.append(left[i])
            i = i+1
        else:
            lst.append(right[j])
            j = j+1
    lst.extend(left[i:])
    lst.extend(right[j:])
    return lst

left = [2, 4, 6]
right = [1, 3, 5]

print(merge(left, right))