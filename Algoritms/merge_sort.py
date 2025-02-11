# merge
# wpierw muszę podzielić listę na 2 przedziały rekurencyjnie
# potem posortować
# scalić


def merge_sort(left_list, right_list):
    i, j = 0, 0
    sorted_list = []

    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            sorted_list.append(left_list[i])
            i += 1
        else:
            sorted_list.append(right_list[j])
            j += 1


    return sorted_list


def merge_sort_recursive(list):
    length = len(list)
    if length <= 1:
        return list

    left = []
    right = []

    for i in range(length):
        if i < length/2:
            left.append(list[i])

        if i >= length/2:
            right.append(list[i])

    sorted_left = merge_sort_recursive(left)
    sorted_right = merge_sort_recursive(right)
    return merge_sort(sorted_left, sorted_right)


lista = [3,6,3,4,8,1,4,2,1,5]




