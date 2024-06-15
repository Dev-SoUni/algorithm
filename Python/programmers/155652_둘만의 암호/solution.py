alpa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def solution(s, skip, index):
    answer = []
    skip = list(skip)

    for it in s:
        text_index = alpa.index(it)
        count = 0

        while count != index:
            text_index += 1
            if text_index > len(alpa) - 1:
                text_index -= len(alpa)
            if alpa[text_index] not in skip:
                count += 1

        answer.append(alpa[text_index])

    answer_text = ""
    for a in answer:
        answer_text += a

    return answer_text