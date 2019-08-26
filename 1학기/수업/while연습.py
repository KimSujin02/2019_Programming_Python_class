x = 3
while x < 6 :
    print(x)
    x += 1  #x를 1씩 증가 시킨다. java는 x++로 쓰지만 파이써에서는 그거 안먹힘.
print("---------------")
echo = input("입력 (exit하면 break한다. false면 계속 반복하고 메아리 울림ㅇㅇ) : ")
while True:
    if echo == "exit" :     #if echo != 'exit'
        break
    print(echo)
    echo = input()
