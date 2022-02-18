# class Car: # название класса всегда с большой буквы
#     color = 'Grey'
#     def turn_on(self):
#         pass
#     def ride(self):
#         pass
# car_object = Car() # создание объекта класса
# print(dir(Car))

class Car:
    # Статитеские поля (переменные класса)
    default_color = 'Grey'
    default_weight = 5000
    def __init__(self, color, model):
        # Динамические поля (переменные объекта)
        self.color = color
        self.model = model
    def turn_on(self):
        pass
    def info(self):
        print(self.color, self.model)
car_obj_1 = Car('blue', 'BMW')
car_obj_2 = Car('red', 'BMW2')
car_obj_2.turn_on()
print(car_obj_1.color)
print(car_obj_1.model)
car_obj_1.info()
car_obj_2.info()
# car_obj_1.default_color='red'
# print(car_obj_1.default_color)
