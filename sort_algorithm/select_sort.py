def select_sort(list):
    for i in range(len(list)):
        least = list[i]
        j = i+1
        while j< len(list):
            if least > list[j]:
                temp = least
                least = list[j]
                list[j] = temp
            j += 1
        list[i] = least
    print(list[::])
a = [1, 4, 2, 7, 3]
select_sort(a)