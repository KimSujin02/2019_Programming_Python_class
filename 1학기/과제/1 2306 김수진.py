majors = [ ["뉴미디어소프트웨어", "뉴미디어웹솔루션", "뉴미디어디자인"], #1학년
["뉴미디어소프트웨어", "뉴미디어웹솔루션", "뉴미디어디자인"], #2학년
["인터랙티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"] ] #3학년

student_number = input("학번을 입력하세요 : ")

grade = student_number[0]
classroom = student_number[1]
number = student_number[2:]
number = str(int(number))

major = majors[int(grade)-1][(int(classroom)-1)//2]

print("{}학년 {}과 {}반 {}번입니다.".format(grade, major, classroom, number))