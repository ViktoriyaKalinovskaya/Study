# class Car:
#     default_color = 'Grey'
#     default_weight = 5000
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#     def turn_on(self):
#         print('Автомобиль заведен')
#     def turn_off(self):
#         print('Автомобиль заглушен')
#     def info(self):
#         print(self.color, self.type, self.year)
# car_obj_1 = Car('blue', 'BMW', 1999)
# car_obj_2 = Car('red', 'BMW2', 2003)
# car_obj_2.turn_on()
# car_obj_2.turn_off()
# car_obj_1.info()
# car_obj_2.info()

class Car:
    def __init__(self, year, type_car, color):
        self.year = year
        self.type_car = type_car
        self.color = color
    def func_z(self): print('Автомобиль заведен')
    def func_vk(self): print('Автомобиль заглушен')
    def func_year(self): print('Год машины', self.year)
    def func_type(self): print(self.type_car)
    def func_color(self): print(self.color)
year = input('Введите год автомобиля ')
type_car = input('Ведите тип автомобиля ')
color = input('Введите цвет автомобиля ')
car = Car(year, type_car, color)
# car.func_year()
