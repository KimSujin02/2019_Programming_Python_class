#학번을 입력받고 학과를 출력한다.
#n=input("학번을 입력하세요 : ")

#if n[0:1] == "3":    
#    if n[1:2] == "1" or n[1:2] == "2":
#        print("인미과 입니다.")
#    elif n[1:2] == "3" or n[1:2] == "4":
#        print("디자인과 입니다.")
#    elif n[1:2] == "5" or n[1:2] == "6":
#        print("솔루션과 입니다.")
#elif n[0:1] == "2" or n[0:1] == "1":
#    if n[1:2] == "1" or n[1:2] == "2":
#        print("소프트웨어과 입니다.")
#    elif n[1:2] == "3" or n[1:2] == "4":
#        print("솔루션과 입니다.")
#    elif n[1:2] == "5" or n[1:2] == "6":
#        print("디자인과 입니다.")

        ## ↓↓↓↓선생님 답안 (내꺼와 달리 일일이 문자를 나누지 않고 나눈것을 변수로 지정해서 헷갈리지 않게 작성하였다.)

        #예시1
        # grade = student_number[0]  <<보기 쉽게 변수를 활용
        # grade = int(grade)  <<<따옴표를 안써도 된다 
        # class = student_number[1]  <<보기 쉽게 변수를 활용
        # class = int(class)

        # if grade == 1 or grade == 2 :  <<grade(맨앞의 문자열)이 1이나 2면
        #   if class == 1 or class == 2 :  <<class(두번째 문자열)이 1이나 2면
        #       print("소프트웨어과 입니다.")
        #   elif class == 3 or class ==4 :
        #       print("솔루션과 입니다.")
        #   elif class == 5 or class == 6 :
        #       print("디자인과 입니다.")

        # if grade == 3 :
        #   if class == 1 or class == 2 :
        #       print("인터렉티브 미디어과 입니다.")
        #   elif class == 3 or class == 4 :
        #       print("디자인과 입니다.")
        #   elif class == 5 or class == 6 :
        #       print("솔루션과 입니다.")


        # 예시2
        # 메이져 = [
        #  ["소프트웨어과", "솔루션과",  "디자인과"]
        #  ["소프트웨어과", "솔루션과",  "디자인과"]
        #  ["인미과", "디자인과",  "솔루션과"]
        #  ]

        # n = input("학번을 입력하세요 : ")

        #  grade = n[0]  #<<보기 쉽게 변수를 활용
        #  grade = int(Grade)  #<<<따옴표를 안써도 된다 
        #  classroom = n[1]  #<<보기 쉽게 변수를 활용
        #  classroom = int(classroom)

        # print(메이져[grade-1][(classroom-1)//2])