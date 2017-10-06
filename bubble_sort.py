# coding:utf-8
def bubble_sort(list):
    for i in range(len(list) - 1):
        j = i+1
        while j < len(list):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
    print(list[::])
a = [1, 4, 5, 3]
bubble_sort(a)
