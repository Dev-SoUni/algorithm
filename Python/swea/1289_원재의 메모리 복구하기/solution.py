import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    memory = list(map(int, input()))
    memory_len = len(memory)
    recovery_memory = [0 for _ in range(memory_len)]
    count = 0

    for idx in range(memory_len):
        if memory[idx] != recovery_memory[idx]:
            count += 1
            for re in range(idx, memory_len):
                recovery_memory[re] = memory[idx]

    print(f"#{test_case} {count}")
