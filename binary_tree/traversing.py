#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 22:10


class TreeNode(object):
    # 定义树结构
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


def preorder_traverse(tree):
    # 遍历顺序：根->左->右
    if tree is None:
        return
    print(tree.root)
    preorder_traverse(tree.left)
    preorder_traverse(tree.right)


def inorder_traverse(tree):
    # 遍历顺序：左->根->右
    if tree is None:
        return
    inorder_traverse(tree.left)
    print(tree.root)
    inorder_traverse(tree.right)


def postorder_treverse(tree):
    # 遍历顺序：左->右->根
    if tree is None:
        return
    postorder_treverse(tree.left)
    postorder_treverse(tree.right)
    print(tree.root)


if __name__ == '__main__':
    node = TreeNode("A",
                    TreeNode("B",
                             TreeNode("D"),
                             TreeNode("E")
                             ),
                    TreeNode("C",
                             TreeNode("F"),
                             TreeNode("G")
                             )
                    )
    preorder_traverse(node)
    inorder_traverse(node)
    postorder_treverse(node)