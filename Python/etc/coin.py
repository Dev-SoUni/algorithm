# 동전 문제
#
# 지불해야 하는 값이 4720원 일 때 1원, 50원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.
#   - 가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
#   - 탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면 됨

def solution(cost):
    coin_kind = [500, 100, 50, 10]

    coin = {
        500: 0,
        100: 0,
        50: 0,
        10: 0
    }

    for it in coin_kind:
        coin[it] = cost // it
        cost %= it

    print(coin)



solution(4720)
