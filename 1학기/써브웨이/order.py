from sandwich import Sandwich
class Order(Sandwich):
    _menus = ["비엘티", "미트볼", "이탈리안비엠티", "터키"]
    def __init__(self):
        self.order_menu = []

    def show_menu(self):
        print("0 : 비엘티")
        print("1 : 미트볼")
        print("2 : 이탈리안 비엘티")
        print("3 : 터키")

    def sum_price(self):
        sum = 0
        for sandwich in self.order_menu:
            sum += self.price

        return sum

    def order_sandwich(self):
        while True:
            self.show_menu()
            order = input("메뉴를 선택해주세요. (ENTER : 계산/종료)")
            if order == "":
                break
            self.name = Order._menus[int(order)]
            self.order()

            self.order_menu.append(self.name)

        # 주문 결과 출력
        print("------------------------- 주문 내역 -------------------------")
        total = Sandwich(self.name) #네임은 메뉴이름이다. 오더에서 받은 네임을 샌드위치 __init__에 적용한다.
        print(total)

o = Order()
o.order_sandwich()