def throughArr(fillArr, j):
    if (fillArr[j][0] != -1):
        print(fillArr[j][1])
    else:
        j += 1
        throughArr(fillArr, j)

if __name__ == '__main__':
    arr = [[-1, "a"], [-1, "b"], [1, "c"], [-1, "d"], [-1, "e"], [-1, "f"], [0, "g"]]
    throughArr(arr, 0)
