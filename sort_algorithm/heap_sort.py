#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:15

# 堆排序
# 时间复杂度 nlogn
# 序列的最大值是堆顶的根节点，与末尾值交换，然后继续构造大顶堆，将最大值放在根节点，反复执行

def get_max_heap(heap, size, root):  # 在堆中做结构调整使得父节点的值大于子节点

    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < size and heap[larger] < heap[left]:  # 保证最大值不会被重新排序
        larger = left
    if right < size and heap[larger] < heap[right]:  # 保证最大值不会被重新排序
        larger = right
    if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger], heap[root] = heap[root], heap[larger]
        get_max_heap(heap, size, larger)


def build_heap(heap):
    # 构造一个堆，将堆中所有数据重新排序
    for index in range(int(len(heap) / 2 - 1), -1, -1):  # 从第一个非叶子节点开始
        get_max_heap(heap, len(heap), index)


def sort(heap):
    build_heap(heap)  # 获得一个大顶堆
    for index in range(len(heap) - 1, -1, -1):
        heap[0], heap[index] = heap[index], heap[0]  # 将最大值调到最后
        get_max_heap(heap, index, 0)  # size递减，保证最大值不会被重新排序
    return heap


print(sort([1, 5, 4, 2, 6, ]))
