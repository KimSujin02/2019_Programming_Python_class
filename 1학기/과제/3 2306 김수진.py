tel1 = {"이름":"도경수", "전화번호":"010-1234-5678"}
tel2 = {"이름":"이수진", "전화번호":"010-8765-4321"}
tel3 = {"이름":"김수진", "전화번호":"010-8902-9135"}

phonebooks = []
phonebooks.append(tel1)
phonebooks.append(tel2)
phonebooks.append(tel3)
print(phonebooks)

input_name = input("이름을 입력하세요. : ")

count = 0
for phonebook in phonebooks:
    if input_name in phonebook["이름"]:
        print("{}님의 전화번호는 {} 입니다.".format(phonebook["이름"], phonebook["전화번호"]))
        count += 1
    
if count == 0:
    print("{}님의 전화번호는 없습니다.".format(input_name))