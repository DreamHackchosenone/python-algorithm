#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 17:24
# python模拟实现栈


class Stack(object):
    """
    栈是限定仅在表尾进行插入和删除操作的线性表
    """

    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def clear(self):
        self.items == []

    def length(self):
        return len(self.items)

    def get_top(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0
