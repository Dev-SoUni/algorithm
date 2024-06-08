def solution(N):
    count = 0

    for h in range(N+1):
        print(h)
        for m in range(60): # 분
            for s in range(60): # 초
                c = str(h) + str(m) + str(s)
                if c.find("3") >= 0:
                    count += 1

solution(5)

