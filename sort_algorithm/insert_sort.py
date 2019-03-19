# coding:utf-8

# 插入排序
# 时间复杂度 n*n
# 插入排序是在一个已经有序的小序列的基础上，一次插入一个元素。有序的小序列只有1个元素，就是第一个元素
# 插入后的元素都向后移位


def insert_sort(test_list):
    for i in range(len(test_list)):
        j = i
        value = test_list[i]
        while j >= 0:
            if test_list[j] > value:    #找到了此时位置，后面元素向后移位
                test_list[j + 1] = test_list[j]
                test_list[j] = value
            j -= 1
    return test_list


a = [1, 2, 3, 10, 5, 9]
insert_sort(a)

