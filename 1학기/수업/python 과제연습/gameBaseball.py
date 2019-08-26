#야구게임
# make 정답
# 사용자 입력받자
# strike, ball 판정
# 정답 길이와 strike가 같다면 끝

#def make_answer():
#    l = list(range(10))
#    l.remove(0)
#    random.shuffle(l)
#    # answer = "".join(str(ch) for ch in l[:3])
#    answer = l[:3]

#    return answer

# def play(input_string):
#    strike = 0
#   ball = 0
#    for i, number in enumerate(answer):
#        search_index = input_string.find(str(number))
#        if search_index == -1:
#            continue
#        elif search_index == i:
#            strike += 1
#        else:
#            ball += 1
#        
#    return strike, ball  

#answer = make_answer()
#print("Play Ball!!!")
#while(True):
#    input_string = input()
#    (strike, ball) = play(input_string)
#    print("strike: {}\tball: {}".format(strike, ball))
#    if len(input_string) == strike:
#        print("정답입니다.")
#        break

import random
        random.sample(l)
        l[:3]
        a = ""
        for i in l[:3] :
            a+=str(i)

    ' '. join(str(i) for i in l[:3])

        computer = str(random.randrange(100, 999!))
        while True : 
            player = input ("숫자 세자리를 입력하시오 : ")
            strike = 0
            ball = 0
            for i in range(lan(computer)) :
                for i in range(lan(player)) :
                    if computer[i] == player[j] :
                        if i ==j :
                            strike +=1
                        else :
                            ball += 1

            if computer == player :
                print("HIT")
                break  