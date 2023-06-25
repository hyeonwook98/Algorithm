def solution(m, musicinfos):
    answer = []
    num = 0
    # 기억한 멜로디 변경하기
    m = m.replace("C#",'c')
    m = m.replace("D#",'d')
    m = m.replace("F#",'f')
    m = m.replace("A#",'a')
    m = m.replace("G#",'g')
        
    for music in musicinfos:
        num += 1
        start_time, end_time, title, info = music.split(',')
        
        info = info.replace("C#",'c')
        info = info.replace("D#",'d')
        info = info.replace("F#",'f')
        info = info.replace("A#",'a')
        info = info.replace("G#",'g')
    
        # 재생 시간 계산하기
        end_h, end_m = end_time.split(':')
        start_h, start_m = start_time.split(':')
        end_time = int(end_h) * 60 + int(end_m)
        start_time = int(start_h) * 60 + int(start_m)
        play_time = end_time - start_time
        
        play_info = ''
        
        loop = play_time // len(info)
        remain = play_time % len(info)
        
        for _ in range(loop):
            play_info += info
        play_info += info[:remain]
        
        if m in play_info:
            answer.append([play_time, num ,title])
            
    if len(answer) == 0:
        return "(None)"
    
    answer.sort(key=lambda x: (-x[0], x[1]))

    return answer[0][2]
