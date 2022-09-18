# Linear search
vec = [5, 11, 2, -1, -2, 0, 11]

def linear_search(list, value):
    for i in range(0, len(list), 1):
        if (list[i] == value):
            return i
    return None



# Binary search
vec = [-2, -1, 0, 2, 5, 11, 11]

def binary_search(list, value):
    def limits(min, max):
        mid = (min + max) // 2
        if (min > max):
            return None
        elif (list[mid] < value):
            return limits(mid+1, max)
        elif (list[mid] > value):
            return limits(min, mid-1)
        else:
            return mid
    return limits(0, len(list)-1)



# Selection sort
vec = [5, 11, 2, -1, -2, 0, 11]

def selection_sort(list):
    temp = list.copy()
    list_sorted = []
    while(len(temp) != 0):
        index_min = 0
        for i in range(0, len(temp), 1):
            if temp[i] < temp[index_min]:
                index_min = i
        list_sorted.append(temp[index_min])
        temp.pop(index_min)
    return list_sorted

def selection_sort2(list):
    for i in range(0, len(list), 1):
        min = list[i]
        for j in range(i+1, len(list), 1):
            if (list[j] < list[i]):
                min = list[j]
                list[j] = list[i]
                list[i] = min
    return list

# Merge sort

# Helper function to sort two list into one sorted list
def sort(list1, list2):
    temp = list1 + list2
    i = 0
    j = len(list1)
    list_sorted = []
    while (i != len(list1) and j != len(temp)):
        if (temp[i] <= temp[j]):
            list_sorted.append(temp[i])
            i += 1
        else:
            list_sorted.append(temp[j])
            j += 1
    if (i != len(list1)):
        list_sorted = list_sorted + temp[i:len(list1)]
    else:
        list_sorted = list_sorted + temp[j:len(temp)]
    return list_sorted

def merge_sort(list):
    if (len(list) <= 1):
        return list
    else:
        mid = len(list) // 2
        lista = list[0:mid]
        listb = list[mid:len(list)]
        return sort(merge_sort(lista), merge_sort(listb))