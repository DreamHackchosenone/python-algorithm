#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 22:46

# 快排
# 时间复杂度 n*logn
# 通过一趟排序将待排记录分割成独立的两部分，其中一部分的关键字均比另一部份的关键字小
# 再分别对这两部分继续进行排序

# 50 10 90 30 70 40 80 60 20
# 第一趟排序
# 20 10 90 30 70 40 80 60 50
# 20 10 50 30 40 70 80 60 90
# 20 10 40 30 50 70 80 60 90


def quick_sort(test_list, left, right):
    # 快速排序
    if left >= right:
        return test_list
    key = test_list[left]
    low = left
    high = right
    while left < right:
        while left < right and test_list[right] >= key:
            right -= 1
        test_list[left] = test_list[right]
        while left < right and test_list[left] <= key:
            left += 1
        test_list[right] = test_list[left]
    test_list[right] = key
    quick_sort(test_list, low, left - 1)
    quick_sort(test_list, left + 1, high)
    return test_list
