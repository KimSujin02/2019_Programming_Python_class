
#00

numbers = [ 1, 5, -2, 0, 6 ]
print(numbers, "중 가장 큰 값은 : ", max(numbers))
print(numbers, "중 가장 작은 값은 : ", min(numbers))
print(numbers, "합계는 : ", sum(numbers))
print("2의 10승은", pow(2,10))

#01

pi = 3.14152
print(pi, "의 소수점 1자리 반올림은 : ", round(pi))
print(pi, "의 소수점 1자리 반올림은 : ", round(pi, 0))
print(pi, "의 소수점 2자리 반올림은 : ", round(pi, 1))
print(pi, "의 소수점 3자리 반올림은 : ", round(pi, 2))
print(pi, "의 소수점 4자리 반올림은 : ", round(pi, 3))
print(round(2.55, 0)) #3.0
print(round(2.55, 1)) #2.5
print(round(2.55, 2)) #2.55

#02

user_name = input("이름은? : ")
user_age = input("나이는? : ")
print(user_name + "님!, 나이는 " + str(user_age) + "세 군요!")
say = "{0}님!, 나이는 {1}세 군요! {1}세라니 놀라워요!"
print(say.format(user_name, user_age))

#03

pi = "3.14159"
print("문자열 출력 : ", pi)
print("실수 변환 출력 : ", float(pi))
print(float(pi))
year = "2019"
print("올해 년도는 : ", year)
print("100년 뒤는 : ", int(year)+100, "년 입니다.")
print("숫자를 문자열로 변환하려면 str을 이용합니다")
print("올해는 " + str(year) + "년 입니다.")

#04

list = [ 'b', 'c', 'a', 'd', ]
list.reverse()
print("리스트 항목 순서 뒤집기", list)
list.sort()
print("리스트 항목 정렬하기", list)
list.sort(reverse=True)
print("리스트 항목 역정렬하기", list)
for index, value in enumerate(list) :
    print("인덱스", index, "위치와 같은 ", value)

#05

#str = "나는 문자열" 변수명에 사용하면 안된다.
#print(str)
#n = 3
#print(str(n)) #오류 발생

#사용자 정의 함수
def input(s):
    print(s)

input("현재의 input()함수는 사용자 정의 함수입니다.")

