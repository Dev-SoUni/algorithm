
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = map(int, input().split())


def binary_search(num, start, end):
    if start > end:
        return False

    mid = (start+end) // 2

    if n_list[mid] > num:
        return binary_search(num, start, mid-1)
    elif n_list[mid] < num:
        return binary_search(num, mid+1, end)
    else:
        return True


for i in m_list:
    if binary_search(i, 0, n-1):
        print(1)
    else:
        print(0)