class Kalkulator:
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
        if self.operation == '+': print(self.plus())
        elif self.operation == '-': print(self.minus())
        elif self.operation == '*': print(self.umnoz())
        elif self.operation == '/':
            try: self.delit()
            except ZeroDivisionError: print('На ноль делить нельзя!')
            else: print(self.delit())
    def plus(self): return self.num1 + self.num2
    def minus(self): return self.num1 - self.num2
    def umnoz(self): return self.num1 * self.num2
    def delit(self): return self.num1 / self.num2
while True:
    num1 = float(input('Введите первое число - '))
    if num1 == '0': break
    num2 = float(input('Введите второе число - '))
    operation = input('Введите знак операции: ')
    kal = Kalkulator(num1, num2, operation)
