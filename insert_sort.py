# coding:utf-8
def insert_sort(list):
    # 插入排序
    for i in range(len(list)):
        j = i
        value = list[i]

        while j >= 0:
            if list[j] > value:
                list[j + 1] = list[j]
                list[j] = value
            j -= 1

    print(list[::])

a = [1, 2, 3, 10, 5, 9]
insert_sort(a)
