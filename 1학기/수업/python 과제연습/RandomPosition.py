import random

max = int(input("몇 번까지 있습니까? : "))
student_number = list(range(max+1))
student_number.remove(0)    #0번은 제외한다.
exclude_list = []

while(True):
    n = input("제외할 번호 : ")
    if n == "4":
        break
    exclude_list.append(int(n))

for n in exclude_list:
    if n in student_number:
        student_number.remove(n)

random.shuffle(student_number)
print("자리\t번호")
for i, value in enumerate(student_number):
    print("{}\t{}".format(i+1, value))