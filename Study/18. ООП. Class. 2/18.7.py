class Phone:
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def call(self):
        if self.is_on:
            print('Making cal...')
    # Метод, который выводит короткую сводку по классу Phone
    def info(self):
        print(f'Class name: {Phone.__name__}')
        print(f'If phone is ON: {self.is_on}')

class MobilePhone(Phone):
    def __init__(self):
        super().__init__()
        self.battery = 0

    def info(self):
        print(f'Class name: {MobilePhone.__name__}')
        print(f'If phone is ON: {self.is_on}')
        print(f'Battery level: {self.battery}')

def show_polymorphism():
    for a in [Phone, MobilePhone]:
        print('-------')
        object = a()
        object.info()

show_polymorphism()
my_mobile_phone = MobilePhone
print(dir(my_mobile_phone))