class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    def final_price(self, sk):
        final_price = (100 - sk) / 100 * self._price
        return final_price

class SmallHouse(House):
    default_area = 40
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

class Human:
    default_name = 'Name'
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 5
        self.__house = None

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, earn):
        self.__money += earn
        print(self.__money)

    def buy_house(self, house, diskaund):
        price = house.final_price(diskaund)
        if self.__money >= price:
            self.__make_deal(house, price)
            print('Kupili dom')
        else:
            print('No money')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


Human.default_info()
human = Human('Name', 21)
human.info()
human.earn_money(6)
human.info()
sHouse = SmallHouse(30)
human.buy_house(sHouse, 30)
