n = int(input())
word = input()
num = []

for _ in range(n):
  num.append(int(input()))

stack = [] #알파벳을 만나면 저장

for i in word:
  if 'A' <=i<= 'Z':
    stack.append(num[ord(i)-ord('A')])
  else:
    str2 = stack.pop()
    str1 = stack.pop()

    if i =='+' :
      stack.append(str1+str2)
    elif i == '-' :
      stack.append(str1-str2)
    elif i == '*' :
      stack.append(str1*str2)
    elif i == '/' :
      stack.append(str1/str2)
print('%.2f' %stack[0])
