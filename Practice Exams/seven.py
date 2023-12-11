
#Q1

#Critical operations x += y and y+=1000 depend on n
#no constants
# 1 addition, 2 assignments, then another 2n additions (based on n)
#time complexity is O(n)

#Q2 

# Critical operations count = count + 10 depend on n²
# No constants!
# count = count + 10 executes n² times
# O(n²)

#Q3

#after three iterations, [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
#will become [11, 7, 12, 14, 8, 1, 6, 18, 19, 20]
#answer is D

#Q4

#If n is very large, n is linear, so n would be better than nlogn.
#logn itself will scale smaller than n, but since it is multiplied by n, it grows much larger
#nlogn is smaller than n² thankfully....
#binary search is log n, but merge sort is nlog n!

#Q5: Minimum number in list search
'''
#Function 1 of O(n²) time
def min2Search(searchList : list) -> int:
    minNumber = searchList[0]
    for i in range(len(searchList)):
        for j in range(len(searchList)):
            if searchList[i] < searchList[j]:
                if searchList[i] < minNumber:
                    minNumber = searchList[i]
            elif searchList[j] < minNumber:
                minNumber = searchList[i]
    return minNumber
#Function 2 of O(n) time implies using linear search!
def minSearch(searchList:list) -> int:
    minNumber = searchList[0]
    for n in range(len(searchList)):
        if searchList[n] < minNumber:
            minNumber = searchList[n]
    return minNumber
print(minSearch(range(25,1,-3)))

'''