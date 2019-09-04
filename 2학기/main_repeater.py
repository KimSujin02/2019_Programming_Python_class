# p153 main_repeater1.py
# import repeater
# from repeater import repeat, once
# from repeater import *
import repeater as re

s = input("반복할 문자를 입력하세요: ")
n = input("반복 횟수를 입력하세요: ")
# repeater.repeat(s, int(n))
# repeater.repeat(s)
# repeater.once(s)
re.repeat(s, int(n))
re.repeat(s)
re.once(s)