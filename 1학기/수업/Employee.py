# #p.200

# class Person :
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age

#     def eat(self, food) :
#         print(self.name + "가" + food + "를 먹습니다.")

#     def __str__(self) :
#         return self.name + "는 " + str(self.age) + "살 입니다."

# class Employee(Person) :
#     def __init__(self, name, age, salary) :
#         super().__init__(name, age)
#         self.salary

#     def work(self) :
#         print("열심히 일을 합시다.")

#     def set_salaty(self) :
#         print("급료를 받습니다.")
#         return self.salary

# e = Employee("수진, 18, 500")
# print(e)
# e.eat("고기")
# e.work()
# r = e.get_salary()
# print("급료는 " + str(r) + "만 원입니다.")