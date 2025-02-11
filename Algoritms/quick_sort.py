
def quick_pivot(lista):
    if len(lista) <= 1:
        return lista
    pivot_index = int(len(lista) // 2)
    pivot = lista[pivot_index]

    left_list = [x for x in lista if x < pivot]
    right_list = [x for x in lista if x > pivot]
    middle_list = [x for x in lista if x == pivot]


    end = [quick_pivot(left_list), middle_list, quick_pivot(right_list)]


    return end

def quick_merge(list_of_lists):
    quit_list = []
    for lista in list_of_lists:
        if isinstance(lista, list):
            if not lista:
                continue
            for i in lista:
                if isinstance(i, list):
                    quit_list.extend(quick_merge(i))
                else:
                    quit_list.append(i)
        else:
            quit_list.append(lista)
    return quit_list

lista = [3,3,5,6,6,4,5,6,2,1,12,29,1,13,2,5,15]




