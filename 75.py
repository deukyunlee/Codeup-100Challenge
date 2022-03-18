#정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자. 

import sys

n = int(sys.stdin.readline().rstrip())
num=0
while n>=num:
    print(num)
    num+=1