from string import Template

class MyTemplate(Template):
    delimiter = '#'


def Main():
    cart = []
    cart.append(dict(item='Coke', price=8, qty=2))
    cart.append(dict(item='Cake', price=4, qty=3))
    t = MyTemplate('#qty x #item= #price')
    total = 0
    print('Cart: ')
    for data in cart:
        print(t.substitute(data))
        total += data['price']
    print('Total: ' + str(total))

if __name__ == '__main__':
    Main()