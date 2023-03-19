def add(*args):
    return sum(args)

print(add(10,20,30,70,80,90))

def calculate(n, **kwargs):

    n += kwargs['add']
    n *= kwargs['multiply']
    return n
print(calculate(2, add=5, multiply=10))

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make='Nissan')
print(f'{my_car.make}, {my_car.model}')