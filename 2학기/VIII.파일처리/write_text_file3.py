fi = open("test.ama", "w", encoding="utf-8")
fi.write("아이스아메리카노\t2800\t0\t1%\t1%\n")
fi.write("민트초코버블티\t2500\t0\t1%\t1%\t0\n")
fi.write("리치스파클링\t2800\t0\t1%\t1%\t1\n")
fi.close()

fi = open("test.ama", "r", encoding="utf8")
sum = 0
while True:
    data = fi.readline()
    if not data:
        break
    l = data.split() # 화이트스페이스로 분리 (띄어쓰기, \t, \n)
    sum += int(l[1])
fi.close()
print("구매 총 금액 :", sum)