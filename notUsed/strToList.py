# --*-- coding: utf-8 --*--


def strToList(LikeListString):
    listFromString = list(LikeListString)
    # print(listFromString)
    finArr = []
    fin1 = []
    allArrs = []
    arr = []
    for i in range(1,len(listFromString)-1):
        if listFromString[i] != '[':
            if (listFromString[i] != ']'):
                arr.append(listFromString[i])
            else:
                allArrs.append(arr)
                arr = []
        else:
            continue
    for i in range(len(allArrs)):
        if allArrs[i][0] == ',':
            allArrs[i] = allArrs[i][2:]
    for i in range(len(allArrs)):
        allArrs[i] = "".join(allArrs[i]).split(', ')
    for i in range(len(allArrs)):
    	for j in range(len(allArrs[i])):
    		fin1.append(int(allArrs[i][j]))
    	finArr.append(fin1)
    	fin1 = []
    return finArr

if __name__ == '__main__':
    limit_police = '[[225, 0, 5, 22, 23], [270, 1, 2, 3, 4], [158, 6, 21], [90, 7, 20], [45, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]'
    print(strToList(limit_police))
