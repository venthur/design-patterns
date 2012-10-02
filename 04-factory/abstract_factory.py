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
        self.veggies = []
        self.cheese = ''
        self.pepperoni = ''
        self.clam = ''

    def prepare(self):
        pass

    def bake(self):
        print 'Bake for 25 minutes at 350.'

    def cut(self):
        print 'Cutting the pizza in diagonal slices.'

    def box(self):
        print 'Place pizza in official PizzaStore box.'

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


class PizzaIngredientFactory(object):

    def createDough(self):
        pass

    def createSauce(self):
        pass

    def createCheese(self):
        pass

    def createVeggies(self):
        pass

    def createPepperoni(self):
        pass

    def createClams(self):
        pass


class ThinCrustDough(object): pass
class MarinaraSauce(object): pass
class Garlic(object): pass
class Onion(object): pass
class Mushroom(object): pass
class RedPepper(object): pass
class SlicedPepperoni(object): pass
class FreshClams(object): pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createVeggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FreshClams()


class CheesePizza(Pizza):

    def __init__(self, ingredientFactory):
        Pizza.__init__(self)
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print 'Preparing', self.name
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()




class NYPizzaStore(PizzaStore):

    def __init__(self):
        PizzaStore.__init__(self)
        self.pizza = None
        self.ingredientFactory = NYPizzaIngredientFactory()

    def createPizza(self, type):
        if type == 'cheese':
            pizza = CheesePizza(self.ingredientFactory)
            pizza.setName('New York Style Cheese Pizza')
        return pizza



if __name__ == '__main__':
    nystore = NYPizzaStore()

    pizza = nystore.orderPizza('cheese')

