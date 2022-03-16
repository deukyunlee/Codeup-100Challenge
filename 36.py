# 단어와 반복 횟수를 입력받아 여러 번 출력해보자. 

import sys

a, b = sys.stdin.readline().rstrip().split()

print(a*int(b))