#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 17:57

# 希尔排序
# 时间复杂度 n*logn
# 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
# 随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止


def shell_sort(test_list, gap):
    n = len(test_list)
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if test_list[j] < test_list[j - gap]:
                    test_list[j], test_list[j - gap] = test_list[j - gap], test_list[j]
                else:
                    break
        gap = gap // 2  # gap每次减半
    return test_list


a = [10, 4, 3, 1, 6, 20, 30, 1, 40, 30, 20]
shell_sort(a, 11)
