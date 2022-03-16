# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자. 

import sys

y,m,d = sys.stdin.readline().rstrip().split(".")

print(d,m,y,sep="-")