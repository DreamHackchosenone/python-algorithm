# coding:utf-8

# 冒泡排序
# 时间复杂度 n*n
# 两两比较相邻记录的关键字，如果反序则交换，知道没有反序的记录为止


def bubble_sort(test_list):
    for i in range(len(test_list) - 1):
        j = i + 1
        while j < len(test_list):
            if test_list[i] > test_list[j]:
                test_list[i], test_list[j] = test_list[j], test_list[i]
            j += 1
    return test_list


a = [1, 4, 5, 3]
bubble_sort(a)

