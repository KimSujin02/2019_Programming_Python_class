
#N자리수의 각 자리 숫자 합
#예: 331 => 7, 10 => 1
number_string = input("각 자리 합계를 구할 숫자를 입력하세요 : ")
sum = 0
for ch in number_string: #ch에 넘스트링을 한글자씩 넣는다.
    sum += int(ch)

print(sum)