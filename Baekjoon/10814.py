n_members = int(input())

member_list = []
for _ in range(n_members):
    (x,y) = input().split()
    member_list.append((int(x),y))


sorted_list = sorted(member_list,key=lambda x: x[0])

for i in sorted_list:
    print(i[0], i[1])    
