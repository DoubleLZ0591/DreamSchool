def least_subsequence(source, target):
    i, j = 0, 0
    min_sub = 0
    flag = False
    while j < len(target):
        for i in range(len(source)):
            if i < len(source) and j < len(target) and source[i] == target[j]:
                j += 1
                flag = True
        if flag:
            min_sub += 1
            flag = False
        else:
            min_sub = -1
            break
    return min_sub


if __name__ == '__main__':
    source = input("Enter source:\n")
    target = input("Enter target:\n")
    print(least_subsequence(source, target))
