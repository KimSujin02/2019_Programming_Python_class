#p239
import pickle
class Person:
    def __init__(self,name, age):
      self.name = name
      self.age = age

    def __str__(self):
        return ("이름 :"+self.name+"\n나이 : "+str(self.age))

p = Person("장원이",18)

f = open("person_data.bin","wb")
pickle.dump(p ,f)  #p객체를 f파일로 내맘속에 저장
f.close()
#영어로는 시리얼 라이즈 라고 함.  메모리 상태를 일렬로 나열해주는게 피클



#Load
#p247쪽 이요
f = open("person_data.bin","rb")
person1 = pickle.load(f)
f.close()
print(person1)
#person1로 객체가 훅 들어옴


#save object list  p240
p1 = Person("이은상",18)
p2 = Person("김재환",24)
p3 = Person("박지민",25)
people = [p1,p2,p3]
f = open("people_data.bin","wb")
pickle.dump(people,f)
f.close()

#Load object list p247
f = open("people_data.bin","rb")
peo = pickle.load(f)
f.close()
#print(peo)
for p in peo:
    print(p)

sum = 0
for p in peo:
    sum += p.age
print(sum)