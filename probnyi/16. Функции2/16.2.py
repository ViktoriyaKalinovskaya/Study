# def first_test():
#     print('Test function 1')
# def second_test():
#     print('Test function 2')
# def simple_decore(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#     return  wrapper
# # первый способ вызова декоратора
# first_test_wrapped = simple_decore(first_test)
# second_test_wrapped = simple_decore(second_test)
# first_test_wrapped()
# second_test_wrapped()
# # второй способ вызова декоратора
# @simple_decore
# def first_test():
#     print('Test function 1')
# first_test()

def param_transfer(fn):
    def wrapper(arg):
        print('Start function: ' + str(fn.__name__) + '(), with param: ' + str(arg))
        fn(arg)
    return  wrapper
@param_transfer
def print_sqrt(num):
    print(num ** 0.5)
print_sqrt(4)
