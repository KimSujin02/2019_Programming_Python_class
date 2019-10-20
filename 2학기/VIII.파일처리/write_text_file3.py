fi = open("test.ama","w",encoding="UTF-8")
fi.write("아이스아메리카노\t2800\t0\t2\t1\t1\n")
fi.write("오레오쉐이크\t\t3500\t1\t1\t3\t3\n")
fi.write("딸기코코넛\t\t3800\t1\t0\t3\t3\n")
fi.close()

fi = open("test.ama","r",encoding="utf8")
sum = 0
while True:
    data = fi.readline()
    if not data:
        break               #읽어온 값이 없으면 멈추ㅓ라
    l = data.split()        #화이트 스페이스(띄어쓰기,\t,\n등)
    sum += int(l[1])

fi.close()
print("주문한 총금액 : "+str(sum)+"원")

# l = data.split("\t")  \t로 쪼개고 list에 한 항목씩 들어가게
    # print(l[1]+"원")
# print(data, end="")  #end="" 은 \n대체함