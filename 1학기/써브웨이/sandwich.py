class Sandwich:
    _size = ["15cm", "30cm"]
    _bread = ["화이트", "하티", "파마산 오레가노", "위트", "허니오트", "플랫"]
    _topping = ["더블업", "쉬림프", "에그마요", "오믈렛", "아보카도", "베이컨", "페퍼로니", "더블치즈", "없음"]
    _sauce = ["슈레드 치즈", "렌치드레싱", "마요네즈", "스위트 어니언", "허니머스타드", "스위트 칠리", "핫 칠리", "없음"]
    price = 0

    def __init__(self, name):
        self.name = name #오더에서 받게 될 메뉴 이름
        self.price = 4900 #기본 금액이다. 15cm기준
        self.size = 0
        self.bread = 2
        self.topping = 2
        self.sauce= 1

    def show_bread(self) :
        print("0 : 화이트")
        print("1 : 하티")
        print("2 : 파마산 오레가노")
        print("3 : 위트")
        print("4 : 허니오트")
        print("5 : 플랫")

    def show_topping(self) :
        print("0 : 더블업 (1700원 추가)")
        print("1 : 쉬립프 (1700원 추가)")
        print("2 : 에그마요 (1500원 추가)")
        print("3 : 오믈렛 (1100원 추가)")
        print("4 : 아보카도 (1100원 추가)")
        print("5 : 베이컨 (900원 추가)")
        print("6 : 페퍼로니 (800원 추가)")
        print("7 : 더블치즈 (800원 추가)")
        print("8 : 없음 (0원 추가)")

    def show_sauce(self) :
        print("0 : 슈레드 치즈")
        print("1 : 렌치드레싱")
        print("2 : 마요네즈")
        print("3 : 스위트 어니언")
        print("4 : 허니머스타드")
        print("5 : 스위트 칠리")
        print("6 : 핫 칠리")
        print("7 : 없음")


    def set_size(self):
        print("0 : 15cm")
        print("1 : 30cm")
        self.size = input("사이즈를 선택하세요. (ENTER : 15cm)")
        if self.size == "":
            self.size = 0
        if self.size == 1:
            self.price += 3800
        else:
            self.size  = int(self.size)


    def set_bread(self):
        self.show_bread()
        self.bread = input("빵을 선택해주세요. (ENTER : 화이트)")
        if self.bread == "":
            self.bread = 0
        else:
            self.bread = int(self.bread)

    def set_topping(self):
        self.show_topping()

        self.topping = input("토핑을 선택해주세요. (ENTER : 없음)")
        if self.topping == "":
            self.topping = 8

        elif self.topping == 0 :
            self.price += 1700

        elif self.topping == 1 :
            self.price += 1700
        
        elif self.topping == 2 :
            self.price += 1500
        
        elif self.topping == 3 :
            self.price += 1100
        
        elif self.topping == 4 :
            self.price += 1100
        
        elif self.topping == 5 :
            self.price += 900

        elif self.topping == 6 :
            self.price += 900

        elif self.topping == 7 :
            self.price += 800

        else :
            self.topping = int(self.topping)
            
    def set_sauce(self):
        self.show_sauce()
        self.sauce = input("소스를 선택해주세요 (ENTER : 없음)")
        if self.sauce == "":
            self.sauce = 7
        else:
            self.sauce = int(self.sauce)

    def __str__(self) :
        return "이름 : " + self.name + "\t사이즈 : " + Sandwich._size[self.size] + "\t빵 : " + Sandwich._bread[self.bread] + "\t토핑 : " + Sandwich._topping[self.topping] + "\t소스 : " + Sandwich._sauce[self.sauce] + "\t가격 : " + str(self.price) + "원입니다."

    def order(self):
        self.set_size()
        self.set_bread()
        self.set_topping()
        self.set_sauce()