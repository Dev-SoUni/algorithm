def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            continue

        bin_number = '0' + format(number, 'b')
        zero_idx = bin_number.rfind('0')
        bin_number = list(bin_number)
        bin_number[zero_idx] = '1'
        bin_number[zero_idx + 1] = '0'

        bin_number = ''.join(bin_number)
        answer.append(int(bin_number, 2))

    return answer