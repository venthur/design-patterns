#!/usr/bin/env python


class Duck(object):

    def quack(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):

    def quack(self):
        print 'Quack'

    def fly(self):
        print "I'm flying."


class Turkey(object):

    def gobble(self):
        pass

    def fly(self):
        pass


class WildTurkey(Turkey):

    def gobble(self):
        print 'Gobble gobble.'

    def fly(self):
        print "I'm flying a short distance"


class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


if __name__ == '__main__':
    md = MallardDuck()
    wt = WildTurkey()
    ta = TurkeyAdapter(wt)

    print 'The turkey says...'
    wt.gobble()
    wt.fly()

    print 'The duck says...'
    md.quack()
    md.fly()

    print 'The TurkeyAdapter says...'
    ta.quack()
    ta.fly()

