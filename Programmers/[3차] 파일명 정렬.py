def solution(files):
    answer = []
    result = []
    # HEAD, NUMBER, TAIL로 분리하기 이때 HEAD의 알파벳의 경우 모두 대문자로 변경할 것
    for idx, file in enumerate(files):
        head, number, tail = '', '', ''
        
        # HEAD 부분 찾기
        for char_idx, char in enumerate(file):
            if char.isdigit():
                break
            head += char
            
        # NUMBER 부분 찾기
        number_idx = char_idx
        while number_idx < len(file) and file[number_idx].isdigit() and len(number) < 5:
            number += file[number_idx]
            number_idx += 1
                
        # TAIL 부분 찾기
        tail = file[number_idx:]

        # HEAD, NUMBER, TAIL을 answer 배열에 추가
        answer.append([head.upper(), int(number), tail, idx])
    
    answer.sort(key=lambda x:(x[0], x[1]))
    for a in answer:
        idx = a[3]
        result.append(files[idx])
    
    return result
