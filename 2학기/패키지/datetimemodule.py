from datetime import datetime

print('현재 날짜 시각 객체 얻기')
today = datetime.now()
print('today = datetime.now() : ', today)

print('연, 월, 일 : ', today.year, today.month, today.day)

print('시, 분, 초 : ', today.hour, today.minute, today.second)

print('요일 : ', today.weekday())

print('특정 날짜 시각 객체 만들기')
day = datetime(2019, 1, 1, 0, 0, 0)
print('day = datetime(2019, 1, 1,0, 0, 0) : ', day)

print('2019년부터 지나온 시간 구하기')
print('today - day : ', today - day)



#내가 태어난 날 무슨 요일일까?
birthday = datetime(2002, 10, 14, 0, 0, 0)
print()
print('내 생일 확인 : ', birthday)
print('내가 태어난 요일 : ', '월화수목금토일'[birthday.weekday()], '요일')

#나는 며칠 살았을까?
print('나는 며칠 살았을까 : ', today - birthday)

#올해 크리스마스 며칠 남았을까?
christmas = datetime(2019, 12, 25, 0, 0, 0)
print('올해 크리스 마스는 며칠 남았을까 : ', christmas - today)