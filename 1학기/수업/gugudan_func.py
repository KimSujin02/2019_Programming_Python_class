def gugudan(n):
    print(n, "단을 출력합니다.")
    for i in range(1, 9+1):
        print(n, "x", 1, "=", n*i)

if __name__ == '__main__': #자기모듈실행하면 실행되고, 다른데서 import하면 실행 안됨
        gugudan(3)