# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때, 
# 나올 수 있는 모든 경우를 출력해보자.

import sys

l,r = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, l+1):
    for j in range(1, r+1):
        print(i,j)