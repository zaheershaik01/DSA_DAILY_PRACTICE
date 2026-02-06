def linear_search(lst, target):
    size = len(lst)
    for index in range(0, len(lst)):
        if (lst[index] == target):
            return index
    return -1


lst = [1, 4, 5, 77, 5, 21, 99]
target = 99
result = linear_search(lst, target)

print(result)