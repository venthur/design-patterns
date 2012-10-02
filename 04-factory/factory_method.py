#!/usr/bin/env python


class PizzaStore(object):

    def createPizza(self, type):
        pass

    def orderPizza(self, type):
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class Pizza(object):

    def __init__(self):
        self.name = ''
        self.dough = ''
        self.sauce = ''
        self.toppings = []

    def prepare(self):
        print 'Preparing', self.name
        print 'Tossing dough...'
        print 'Adding sauce...'
        print 'Adding toppings...'
        for i in self.toppings:
            print '   ', i

    def bake(self):
        print 'Bake for 25 minutes at 350.'

    def cut(self):
        print 'Cutting the pizza in diagonal slices.'

    def box(self):
        print 'Place pizza in official PizzaStore box.'

    def getName(self):
        return self.name



class NYStyleCheesePizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append('Grated Reggiano Cheese')


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozarella Cheese')

    def cut(self):
        print 'Cutting the pizza into square slices.'


class NYPizzaStore(PizzaStore):

    def createPizza(self, type):
        if type == 'cheese':
            pizza = NYStyleCheesePizza()
        return pizza


class ChicagoStore(PizzaStore):

    def createPizza(self, type):
        if type == 'cheese':
            pizza = ChicagoStyleCheesePizza()
        return pizza


if __name__ == '__main__':
    nystore = NYPizzaStore()
    chicagostore = ChicagoStore()

    pizza = nystore.orderPizza('cheese')
    pizza = chicagostore.orderPizza('cheese')

