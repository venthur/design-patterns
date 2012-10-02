#!/usr/bin/env python


class Command(object):

    def execute(self):
        pass

    def undo(self):
        pass


class NullCommand(Command):

    def execute(self):
        print 'Null.'

    def undo(self):
        print 'Undo Null.'


class Remote(object):

    def __init__(self):
        self.onCommands = [NullCommand() for i in range(7)]
        self.offCommands = [NullCommand() for i in range(7)]
        self.undoCommand = NullCommand()

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onPushed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoPushed(self):
        self.undoCommand.undo()


class LightOffCommand(Command):

    def execute(self):
        print 'Light off.'

    def undo(self):
        print 'Light on.'


class LightOnCommand(Command):

    def execute(self):
        print 'Light on.'

    def undo(self):
        print 'Light off.'


class CeillingFan(object):

    def __init__(self):
        self.speed = 0

    def high(self):
        print 'Fan - high'
        self.speed = 10

    def medium(self):
        print 'Fan - medium'
        self.speed = 7

    def low(self):
        print 'Fan - low'
        self.speed = 4

    def off(self):
        print 'Fan - off'
        self.speed = 0


class CeillingFanHighCommand(Command):

    def __init__(self, ceillingFan):
        self.ceillingFan = ceillingFan

    def execute(self):
        self.prevSpeed = self.ceillingFan.speed
        self.ceillingFan.high()

    def undo(self):
        if self.prevSpeed == 0:
            self.ceillingFan.off()
        elif self.prevSpeed == 4:
            self.ceillingFan.low()
        elif self.prevSpeed == 7:
            self.ceillingFan.medium()
        elif self.prevSpeed == 10:
            self.ceillingFan.high()


class CeillingFanLowCommand(Command):

    def __init__(self, ceillingFan):
        self.ceillingFan = ceillingFan

    def execute(self):
        self.prevSpeed = self.ceillingFan.speed
        self.ceillingFan.low()

    def undo(self):
        if self.prevSpeed == 0:
            self.ceillingFan.off()
        elif self.prevSpeed == 4:
            self.ceillingFan.low()
        elif self.prevSpeed == 7:
            self.ceillingFan.medium()
        elif self.prevSpeed == 10:
            self.ceillingFan.high()


class MacroCommand(Command):

    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for i in self.commands:
            i.execute()

    def undo(self):
        for i in self.commands:
            i.undo()


if __name__ == '__main__':
    remote = Remote()

    ceillingFan = CeillingFan()

    lightOnCommand = LightOnCommand()
    lightOffCommand = LightOffCommand()

    ceillingFanHighCommand = CeillingFanHighCommand(ceillingFan)
    ceillingFanLowCommand = CeillingFanLowCommand(ceillingFan)
    partyOnCommand = MacroCommand([ceillingFanHighCommand, lightOnCommand])
    partyOffCommand = MacroCommand([ceillingFanLowCommand, lightOffCommand])

    remote.setCommand(0, lightOnCommand, lightOffCommand)
    remote.setCommand(1, ceillingFanHighCommand, ceillingFanLowCommand)
    remote.setCommand(2, partyOnCommand, partyOffCommand)

    for i in range(7):
        print '---------'
        print 'Slot', i
        remote.onPushed(i)
        remote.offPushed(i)
        remote.undoPushed()
