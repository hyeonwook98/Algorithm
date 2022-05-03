from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    report_to_from = defaultdict(set) #id를 신고한 목록
    report_from_to = defaultdict(set) #id가 신고한 목록
    
    for i in report:
        report_sender, report_receive = i.split(' ')
        report_to_from[report_receive].add(report_sender)
        report_from_to[report_sender].add(report_receive)
        
    for id in id_list:
        cnt=0
        for j in report_from_to[id]:
            if len(report_to_from[j])>=k:
                cnt+=1
        answer.append(cnt)
    
    return answer
