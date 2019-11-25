#2306 김수진
#프로젝트 이름 : Whats in my closet?
# 주의 사항
# 최초로 실행할 때는 옷 저장하기를 먼저하고 계절별로 옷보기를 해야한다.
# 처음엔 파일에 아무 데이터도 없기 때문에 "ㅇㅇ 옷장에 아무것도 없습니다."라고 뜬다.
# 계절 선택은 한글로 계절을 입력해도 되고 영어로 입력해도 된다.

# 파일 입출력을 통해 옷장안에 옷이 저장되고 해당 계절 옷장에 저장된 옷들을 확인할 수 있는 프로그램이다.

from builtins import print

#최초에만 실행되는 출력문
print("안녕하세요 What's in my closet 프로그램입니다")

while True :
    answer1 = input("1. 계절별로 옷 보기\n2. 옷 저장하기\n3. 프로그램종료\n선택 : ")

    if answer1 == "1":
        print("어떤 계절의 옷을 선택하겠습니까?")
        a = input("선택 : ")

        if a == "봄" or a == "spring":
            try :
                f = open("봄.txt", 'r', encoding="utf8")
                data = f.read()
                print("=== 봄 옷장 결과입니다 ===")
                print(data)
                f.close()
            except FileNotFoundError :
                print("봄 옷장에 아무것도 없습니다")

        if a == "여름" or a == "summer":
            try :
                f = open("여름.txt", 'r', encoding="utf8")
                data = f.read()
                print("=== 여름 옷장 결과입니다 ===")
                print(data)
                f.close()
            except FileNotFoundError :
                print("여름 옷장에 아무것도 없습니다")

        if a == "가을" or a == "autumn":
            try :
                f = open("가을.txt", 'r', encoding="utf8")
                data = f.read()
                print("=== 가을 옷장 결과입니다 ===")
                print(data)
                f.close()
            except FileNotFoundError :
                print("가을 옷장에 아무것도 없습니다.")

        if a == "겨울" or a == "winter":
            try :
                f = open("겨울.txt", 'r', encoding="utf8")
                data = f.read()
                print("=== 겨울 옷장 결과입니다 ===")
                print(data)
                f.close()
            except FileNotFoundError :
                print("겨울 옷장에 아무것도 없습니다.")

    if answer1 == "2":
        print("계절을 선택해주세요.")
        a = input("선택 : ")
        if a == "봄" or a == "spring":
            a = input("봄을 선택하셨습니다.\n어떤 옷을 저장하실 건가요? : ")
            f = open("봄.txt", 'a', encoding="utf8")
            data = a + "\n"
            f.write(data)
            f.close()
            print("저장 되었습니다.")

        if a == "여름" or a == "summer":
            a = input("여름을 선택하셨습니다.\n어떤 옷을 저장하실 건가요? : ")
            f = open("여름.txt", 'a', encoding="utf8")
            data = a + "\n"
            f.write(data)
            f.close()
            print("저장 되었습니다.")

        if a == "가을" or a == "autumn":
            a = input("가을을 선택하셨습니다.\n어떤 옷을 저장하실 건가요? : ")
            f = open("가을.txt", 'a', encoding="utf8")
            data = a + "\n"
            f.write(data)
            f.close()
            print("저장 되었습니다.")

        if a == "겨울" or a == "winter":
            a = input("겨울을 선택하셨습니다.\n어떤 옷을 저장하실 건가요? : ")
            f = open("겨울.txt", 'a', encoding="utf8")
            data = a + "\n"
            f.write(data)
            f.close()
            print("저장 되었습니다.")

    if answer1 == "3":
        print("프로그램을 종료합니다.")
        break