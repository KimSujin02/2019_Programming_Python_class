import os
data = os.listdir("c:\\")      # .: 현재 디렉터리, ..:상위 디렛터리
#  #따옴표안에 역슬래시는 \하나만쓰면 안보임
# \n : 엔터
# \\ : \
# \' : '
# \" : "
print(data)
for d in data:
    print(d)
    print("is directory?: "+str(os.path.isfile(d)))
    print("is file?: "+str(os.path.isfile(d)))