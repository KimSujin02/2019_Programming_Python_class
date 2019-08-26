#order.py
from coffee import Coffee
from bubbletea import Bubbletea
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