def mergeSort(list):
    #base case
    if len(list) == 1:
        return list
    
    #split list
    list1 = list[:len(list)//2]
    list2 = list[len(list)//2:]
    
    #inductive step
    mlist1 = mergeSort(list1)
    mlist2 = mergeSort(list2)

    return merge(mlist1,mlist2)

def merge(a,b):
    merged_list = []
    ind_a = 0
    ind_b = 0
    while ind_a < len(a) and ind_b < len(b):
        if a[ind_a] < b[ind_b]:
            merged_list.append(a[ind_a])
            ind_a += 1
        else:
            merged_list.append(b[ind_b])
            ind_b += 1
    merged_list += a[ind_a:]
    merged_list += b[ind_b:]
    return merged_list

array = [4, 2, 3, 8, 8, 43, 6,1, 0]
ar = mergeSort(array)
print(ar)