f = open("file.txt","a",encoding="utf8")    #a:append 이어붙이다  w:  덮어쓰다

f.write("반갑다")
f.write("\n")
f.write("세상아")

f.close()