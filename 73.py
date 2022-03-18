# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자. 

import sys

n = int(sys.stdin.readline().rstrip())

while n > 0:
    print(n-1)
    n-=1