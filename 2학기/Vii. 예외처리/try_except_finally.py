f = open("file.txt", "w")

try :
    f.write("Hello world!\n")
    f.write("100")
except TypeError:
    print("타입 예외 발생(숫자형 100은 쓸 수 없습니다.")
finally :
    print("예외 여부와 상관없이 무조건 실행")
    f.close()