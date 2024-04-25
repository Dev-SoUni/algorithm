

def qsort(data_list):
    if len(data_list) <= 1:
        return data_list

    pivot = data_list[0]
    left = list()
    right = list()

    for i in range(1, len(data_list)):
        if(pivot <= data_list[i]):
            right.append(data_list[i])
        else:
            left.append(data_list[i])

    return qsort(left) + [pivot] + qsort(right)

data_list = [11, 8, 4, 1, 2, 5, 7]
result = qsort(data_list)
print(result)