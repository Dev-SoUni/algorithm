import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, 11):
    N = input()

    count = 0
    buildings = list(map(int, input().split()))

    for idx in range(2, len(buildings)-2):
        view = buildings[idx]
        left_one_view = buildings[idx-1]
        left_two_view = buildings[idx-2]
        right_one_view = buildings[idx+1]
        right_two_view = buildings[idx+2]

        if view > left_one_view and view > left_two_view and view > right_one_view and view > right_two_view:
            max_view = max(left_one_view, left_two_view, right_one_view, right_two_view)
            count += view - max_view

    print(f"#{test_case} {count}")
