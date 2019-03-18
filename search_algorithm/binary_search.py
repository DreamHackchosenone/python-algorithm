#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 19:02

## 二分查找
## 时间复杂度nlogn
## 基本思想是:将列表中间位置的元素与目标元素比较，如果两者相等，则查找成功；
# 否则将列表从中间位置分开，分成前、后两个子列表，如果中间位置的元素大于目标元素，
# 则进一步查找前一子列表，否则进一步查找后一子列表。重复以上过程，直到找到满足条件的元素，使查找成功


# 非递归
def binary_search(search_list, target):
    begin = 0
    end = len(search_list) - 1
    while begin < end:
        mid = (begin + end) // 2
        if target < search_list[mid]:
            end = mid
        if target > search_list[mid]:
            begin = mid
        if target == search_list[mid]:
            return mid
    return -1


# 递归
def recursive_binary_search(search_list, target):
    mid = len(search_list) // 2
    if mid == 0:
        return -1
    if target == search_list[mid]:
        return mid
    if target > search_list[mid]:
        search_list = search_list[mid + 1:]
    if target < search_list[mid]:
        search_list = search_list[0:mid - 1]
    # 递归必须增加return，敷奏函数没有返回值，是None
    return recursive_binary_search(search_list, target)


print(recursive_binary_search([1, 2, 3, 4, 5, 6], 2))
