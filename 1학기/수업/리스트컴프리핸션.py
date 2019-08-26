print("array1을 출력")
array1 =[]
for i in range(1, 10+1, 2):
    array1.append(i**2)
    
print(array1)

print("----------------------------------------")

#array1을 출력하는 문을 아래처럼 존나 짧게 할 수 있다. 방법은 어느 방버브로 상관없으나 회사에서 나올 수 있으니 둘 다 알아야 한다.
print ("array2를 출력")
array2 = [i**2 for i in range(1, 10+1, 2)]
print(array2)

print("----------------------------------------")

#array2에 조건문으로 30이상의 것만 출력한다.
print("array3을 출력(30이상의 값만 출력한다.)")
array3 = [i**2 for i in range(1, 10+1, 2) if i**2 > 30]
print("array3 : ", array3)

print("----------------------------------------")

#array3의 조건은 array4의 조건을 단축해서 쓴 것이다. 짧으면 좋긴하지만 아무나 못하는것..
print("array4를 출력")
array4 = []
for i in range(1, 10+1, 2):
    if i**2 > 30:
        array4.append(i**2)
print("array4 : ", array4)