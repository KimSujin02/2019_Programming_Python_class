# import random
# # def rolling_dice() : #dice는 주사위라는 뜻,, 따라서 rollingdice=주사위를 굴리다
# #     n = random.randint(1, 6) #1 <= n <= 6 랜덤수, 1~6사이의 정수중에 하나를 뽑는다.
# #    print("6면 주사위 굴린 결과 : ", n)

# # def rolling_dice2(pip) :
# #    m = random.randint(1, pip)
# #    print(pip, "면 주사위 굴린 결과 : ", m)

# def rolling_dice2(pip, repeat) :
#     for r in range(1, repeat+1):
#         n = random.randint(1, pip)
#         print(pip, "면 주사위 굴린 결과", r, " : ", n)

# rolling_dice2(6, 1)
# rolling_dice2(6, 2)
# rolling_dice2(12, 0)
# rolling_dice2(20, 3)


# # def를 메소드 처럼 씀

# #rolling_dice()
# #rolling_dice()
# #rolling_dice()

# #p109
# def star() :
#     print("*"*5)

# star()
# star()
# star()

# #p113
# print("♡")
# print("♡", "♪")
# print("♡", "♪", "♣")
# print("♡", "♪", "♣", "♠")
# print("♡", "♪", "♣", "♠", "★")
# print()

# #p114
# def p( *args ) :
#     str = ""
#     for a in args:
#         str += str + " " + a
#     print(str)
# p("♡")
# p("♡", "♪")
# p("♡", "♪", "♣", "♠")
# print()

# def p1( space, space_num, *args ) :
#     str = args[0]
#     for i in range(1, len(args)):
#         str = str + (space * space_num) + args[i]
#     print(str)

# p1(",", 3, "♡", "♪")
# p1("☆", 2, "♡", "♪", "♣")
# p1("_", 3, "♡", "♪", "♣", "♠")

# #p115
# def star2( ch, *nums ) :
#     for i in range(len(nums)) :
#         print(ch * nums[1])
# star2("♬", 3)
# star2("♡", 1, 2, 3)

# #p116
# def fn(a, b, c, d, e) :
#     print(a, b, c, d, e)

# fn (1, 2, 3, 4, 5)
# fn (10, 20, 30, 40, 50)
# fn (5, 6, 7, 8, 9)
# fn (a=1, b=2, c=3, d=4, e=5)
# fn (e=5, d=4, c=3, b=2, a=1)
# fn (1, 2, c=3, e=5, d=4)
# #fn (d=4, e=5, 1, 2, 3) 에러가 난다 p117

# #ㅔ118
# # ***__***
# # ***__***
# # ***__***

# #star 함수 정의
# def star3(mark, repeat, space, space_repeat, line=3) :
#         for _ in range(line) :
#                 string = (mark * repeat) + (space * space_repeat) + (mark * repeat)
#                 print(string)

# star3("*", 3, "_", 2)

# #p119
# def hello(msg="안녕하세요"):
#         print(msg + "1")

# hello("하이")
# hello("hi")
# hello()

# #p120
# def hello2(name, msg="안녕하세요"):
#         print(name + "님, " + msg + "!")

# hello2("김수진", "오랜만이예요")
# hello2("도경수")
# #hello2() 기본값이 없기 때문에 오류가 난다. name 인자 없음.

# def fn(a, b=[]):
#         b.append(a)
#         print(b)

# fn(3)
# fn(5)
# fn(10)

# #p123 혼자해보기
# def gugudan(dan=2):
#         print(dan, "단 입니다.")
#         for i in range(1, 9, 1):
#                 print(dan, "x", i, " = ", (dan * i))

# print()
# gugudan(3) # 3단 출력
# print()
# print("-----------------------")
# print()
# gugudan(2) # 2단 출력
# print()
# print("-----------------------")
# print()
# gugudan()  # 2단 출력
# print()

# #p125
# def sum(*numbers) :
#         sum_value = 0
#         for number in numbers :
#                 sum_value =  sum_value + number
#         return sum_value

# result = sum(1,3)
# print("1 + 3 =", result)
# print("1 + 3 + 5 + 7 =", sum(1, 3, 5, 7))

# #p126
# def min(*numbers) :
#         min_value = numbers[0]
#         for number in numbers :
#                 if min_value < number :
#                         min_value = number
#         return min_value

# print("min(3, 6, -2) = ", min(3, 6, -2))

# def max(*numbers) :
#         max_value =  numbers[0]
#         for number in numbers :
#                 if max_value > number :
#                         max_value = number
#         return max_value

# print("max(8, 1, -1, 12) = ", max(8, 1, -1, 12))

# def multi_num (multi, start, end) :
#         result = []
#         for n in range(start, end):
#                 if n % multi == 0:
#                         result.append(n)
#         return result

# print("multi_num(17, 1, 200) = ", multi_num(17, 1, 200))
# print("multi_num(3, 1, 100) = ", multi_num(3, 1,100))

# #p128

# def min_max(*args) :
#         min_value = args[0]
#         max_value = args[0]
#         for a in args :
#                 if min_value > a :
#                         min_value = a
#                 if max_value < a :
#                         max_value = a
#         return min_value, max_value

# min, max = min_max(52, -3, 23, 89, -21)
# print("최솟값 : ", min, "최댓값 : ", max)
