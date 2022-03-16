# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아 
# 순서대로 붙여 출력하는 프로그램을 작성해보자.

import sys

a, b = sys.stdin.readline().rstrip().split()

print(a+b)