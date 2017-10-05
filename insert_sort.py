# coding:utf-8
def insert_sort(lists, value):
    # 插入排序
    lists.append(value)
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    print(lists)
a = [1, 2, 5, 8, 9]
insert_sort(a, 4)
