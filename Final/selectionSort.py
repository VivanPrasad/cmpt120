
def selectionSort(searchList):
    for n in range(len(searchList)):
        min = n
        for x in range(n+1,len(searchList)):
            if searchList[x] < searchList[n]:
                min = x
        searchList[min],searchList[n] = searchList[n],searchList[min]
lst = list(range(100,1,-3))
print(lst)
selectionSort(lst)
print(lst)