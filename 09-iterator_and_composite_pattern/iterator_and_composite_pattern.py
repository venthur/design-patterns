#!/usr/bin/env python


class MenuComponent(object):

    def add(self, menucomponent):
        raise Exception()

    def remove(self, menucomponent):
        raise Exception()

    def getChild(self, i):
        raise Exception()

    def getName(self):
        raise Exception()

    def getDescription(self):
        raise Exception()

    def getPrice(self):
        raise Exception()

    def isVegetarian(self):
        raise Exception()

    def pprint(self):
        raise Exception()

    def __iter__(self):
        raise Exception()


class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def isVegetarian(self):
        return self.vegetarian

    def pprint(self):
        print ' ' + self.getName(),
        if self.isVegetarian():
            print '(v)',
        print ', ' + str(self.getPrice())
        print '   -- ' + self.getDescription()

    def __iter__(self):
        return NullIterator()


class Menu(MenuComponent):

    def __init__(self, name, description):
        self.menuComponents = []
        self.name = name
        self.description = description
        self.iterator = None

    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent):
        self.menuComponents.remove(menuComponent)

    def getChild(self, i):
        return self.menuComponents[i]

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def pprint(self):
        print '\n' + self.getName() + ', ' + self.getDescription()
        print '--------------------------'
        # iterator
        for i in self.menuComponents:
            i.pprint()

    def __iter__(self):
        if self.iterator is None:
            self.iterator = CompositeIterator(iter(self.menuComponents))
        return self.iterator


class CompositeIterator(object):

    def __init__(self, iterator):
        self.stack = []
        self.stack.append(iterator)

    def __iter__(self):
        return self

    # This is not quite the same iterator as in the book, because (a) the
    # python lists do not support the same iterator interface they require and
    # (b) python's iterators don't have a `next` method
    def next(self):
        while len(self.stack) > 0:
            iterator = self.stack[-1]
            try:
                item = iterator.next()
            except StopIteration:
                self.stack.pop()
                continue
            if isinstance(item, MenuItem):
                return item
            elif isinstance(item, Menu):
                self.stack.append(iter(item))
                return self.next()
            else:
                raise RuntimeError()
        raise StopIteration()


class NullIterator(object):

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration()


class Waitress(object):

    def __init__(self, allMenus):
        self.allMenus = allMenus

    def printMenu(self):
        self.allMenus.pprint()

    def printVegetarianMenu(self):
        print '\nVEGETARIAN MENU'
        print '----------------'
        for i in self.allMenus:
            if i.isVegetarian():
                i.pprint()



if __name__ == '__main__':
    pc = Menu('PANCAKE HOUSE MENU', 'Breakfast')
    dm = Menu('DINER MENU', 'Lunch')
    cm = Menu('CAFE MENU', 'Dinner')
    dm2 = Menu('DESSERT MENU', 'Dessert of course!')

    allMenus = Menu('ALL MENUS', 'All menus combined')
    allMenus.add(pc)
    allMenus.add(dm)
    allMenus.add(cm)

    dm.add(MenuItem('Pasta', 'Spaghetti with Marinara Sauce, and a slice of sourdough bread', True, 3.89))
    dm.add(MenuItem('BLT', 'Bacon with lettuce & tomato on whole wheat', False, 2.99))
    dm.add(dm2)

    dm2.add(MenuItem('Apple Pie', 'Apple pie with a flakey crust, topped with vanilla icecream', True, 1.59))

    waitress = Waitress(allMenus)
    waitress.printMenu()
    waitress.printVegetarianMenu()

