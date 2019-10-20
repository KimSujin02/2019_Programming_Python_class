class Drink:
    _cups = ["레귤러", "점보"]
    _ices = ["0%", "50%", "100%", "150%"]
    _sugars = ["0%", "50%", "100%", "150%"]

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0
        self.ice = 2
        self.sugar = 2

    def set_cup(self):
        self.cup = input("컵을 선택하세요.(0: 레귤러, 1: 점보) ")
        if self.cup == "":
            self.cup = 0
        else:
            self.cup = int(self.cup)

        if self.cup==1:     #점보면 500원 추가
            self.price += 500

    def set_ice(self):
        self.ice = input("얼음량을 선택하세요.(0: 0%, 1: 50%, 2:100%, 3:150%) ")
        if self.ice == "":
            self.ice = 2
        else:
            self.ice = int(self.ice)

    def set_sugar(self):
        self.sugar = input("당도를 선택하세요.(0: 0%, 1: 50%, 2:100%, 3:150%) ")
        if self.sugar == "":
            self.sugar = 2
        else:
            self.sugar = int(self.sugar)

    def __str__(self):
        return "이름:"+self.name+"\t가격:"+str(self.price)+"원\t컵:"+Drink._cups[self.cup]+"\t얼음량:"+Drink._ices[self.ice]+"\t당도:"+Drink._sugars[self.sugar]

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

class Coffee(Drink):
    pass

class Bubbletea(Drink):
    _pearls = ["타피오카", "코코", "젤리", "알로에"]

    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl = 0

    def set_pearl(self):
        self.pearl = input("펄을 선택하세요.(0: 타피오카, 1: 코코, 2:젤리, 3:알로에) ")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)
    
    def __str__(self):
        return super().__str__() + "\t펄:" + self._pearls[self.pearl]

    def order(self):
        super().order()
        self.set_pearl()

class Order:
    _drinks = [Coffee("아메리카노", 1800), Bubbletea("딸기쉐이크", 3000)]
    def __init__(self):
        self.order_menu = []

    def show_menu(self):
        menu = "0: 아메리카노\t1500원\n1: 딸기쉐이크\t3000원"
        print(menu)

    def sum_price(self):
        sum = 0
        for drink in self.order_menu:
            sum += drink.price

        return sum

    def order_drink(self):
        while True:
            self.show_menu()
            order = input("원하는 음료를 선택하세요.")
            if order == "":
                break
            drink = Order._drinks[int(order)]
            drink.order()

            self.order_menu.append(drink)

        # 주문 결과 출력하자
        for d in self.order_menu:
            print(d)
        print("합계: "+str(self.sum_price())+"원")


            
o = Order()
o.order_drink()
# d1 = Drink("우하하", 1500)
# print(d1)

# b1 = Bubbletea("딸기 쉐이크", 3000)
# print(b1)