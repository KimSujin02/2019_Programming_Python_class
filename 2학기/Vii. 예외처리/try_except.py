l = [1, 2, 3]

try :
    print(l[2])
    print(l[3]) #이 문장만 에러가 나기 때문네 except발생됨. IndexError: list index out of range
except IndexError:
    print("리스트의 요소에 접근하지 못했습니다.")

# print(l[2])
# print(l[3]) #IndexError: list index out of range