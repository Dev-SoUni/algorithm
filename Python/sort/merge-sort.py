
def split(data):
    if len(data) <= 1:
        return data

    div = int(len(data)/2)
    left = data[:div]
    right = data[div:]

    return merge(split(left), split(right))

def merge(left, right):
    sorted = list()
    left_index, right_index = 0, 0

    while left_index < len(left) or right_index < len(right):
        if left_index == len(left):
            sorted = sorted + right[right_index:]
            break
        elif right_index == len(right):
            sorted = sorted + left[left_index:]
            break
        elif left[left_index] < right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1

    return sorted


data_list = [49, 97, 53, 5, 33, 65, 62, 51]
result = split(data_list)
print(result)