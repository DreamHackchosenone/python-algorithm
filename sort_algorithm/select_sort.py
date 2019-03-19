# coding:utf-8

# 选择排序
# 时间复杂度 n*n
# 每次选择最大的放在最后


def select_sort(test_list):
    for i in range(len(test_list)):
        least = test_list[i]
        j = i + 1
        while j < len(test_list):
            if least > test_list[j]:
                least, test_list[j] = test_list[j], least
            j += 1
            test_list[i] = least
    return test_list


a = [1, 4, 2, 7, 3]
print(select_sort(a))


