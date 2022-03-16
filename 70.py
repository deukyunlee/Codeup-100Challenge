# 월이 입력될 때 계절 이름이 출력되도록 해보자. 

# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall 

import sys

s = int(sys.stdin.readline().rstrip())

if s == 12 or s == 1 or s == 2:
    print("winter")

elif s == 3 or s == 4 or s == 5:
    print("spring")

elif s == 6 or s == 7 or s == 8:
    print("summer")

elif s == 9 or s == 10 or s == 11:
    print("fall")