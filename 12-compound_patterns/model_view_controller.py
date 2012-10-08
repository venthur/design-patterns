#!/usr/bin/env python


from threading import Thread
import time

###############################################################################
# Model
###############################################################################

class BeatModelInterface(object):

    def initialize(self):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def setBPM(self, bmp):
        pass

    def getBPM(self):
        pass

    def registerBeatObserver(self, o):
        pass

    def removeBeatObserver(self, o):
        pass

    def registerBPMObserver(self, o):
        pass

    def removeBPMObserver(self, o):
        pass

    def notifyBeatObservers(self):
        pass

    def notifyBPMObservers(self):
        pass


class BeatModel(BeatModelInterface):

    # pp 538
    def __init__(self):
        self.sequencer = Sequencer(self)
        self.beatObservers = []
        self.bpmObservers = []
        self.bpm = 90

    def initialize(self):
        pass

    def on(self):
        self.sequencer.start()
        self.setBPM(90)

    def off(self):
        self.setBPM(0)
        self.sequencer.stop()
        self.sequencer.join()

    def setBPM(self, bpm):
        self.bpm = bpm
        self.sequencer.setTempoInBPM(self.getBPM())
        self.notifyBPMObservers()

    def getBPM(self):
        return self.bpm

    def registerBPMObserver(self, o):
        self.bpmObservers.append(o)

    def removeBPMObserver(self, o):
        self.bpmObservers.remove(o)

    def notifyBPMObservers(self):
        for i in self.bpmObservers:
            i.updateBPM()

    def registerBeatObserver(self, o):
        self.beatObservers.append(o)

    def removeBeatObserver(self, o):
        self.beatObservers.remove(o)

    def notifyBeatObservers(self):
        for i in self.beatObservers:
            i.updateBeat()

    def beatEvent(self):
        self.notifyBeatObservers()


class Sequencer(Thread):

    def __init__(self, beatModel):
        Thread.__init__(self)
        self.beatModel = beatModel
        self.bpm = 0

    def run(self):
        self.running = True
        while self.running:
            self.beatModel.beatEvent()
            time.sleep(60. / self.bpm)

    def setTempoInBPM(self, bpm):
        self.bpm = bpm

    def stop(self):
        self.running = False


###############################################################################
# View
###############################################################################

#class DJView(BeatObserver, BPMObserver):
class DJView(object):

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model
        model.registerBPMObserver(self)
        model.registerBeatObserver(self)


    def createView(self):
        pass

    def updateBPM(self):
        bpm = self.model.getBPM()
        if bpm == 0:
            print 'Offline'
        else:
            print 'Current BPM: %d' % self.model.getBPM()

    def updateBeat(self):
        print 'Beat'

###############################################################################
# Controller
###############################################################################

class ControllerInterface(object):

    def start(self):
        pass

    def stop(self):
        pass

    def increaseBPM(self):
        pass

    def decreaseBPM(self):
        pass

    def setBPM(self, bpm):
        pass


class BeatController(ControllerInterface):

    def __init__(self, model):
        self.model = model
        self.view = DJView(self, self.model)
        self.view.createView()
        # and more...
        self.model.initialize()

    def start(self):
        self.model.on()

    def stop(self):
        self.model.off()

    def increaseBPM(self):
        bpm = self.model.getBPM()
        self.model.setBPM(bpm + 1)

    def decreaseBPM(self):
        bpm = self.model.getBPM()
        self.model.setBPM(bpm - 1)

    def setBPM(self, bpm):
        self.model.setBPM(bpm)


if __name__ ==  '__main__':
    model = BeatModel()
    controller = BeatController(model)

    print 'Starting Controller...'
    controller.start()
    time.sleep(5)
    print 'Stopping Controller...'
    controller.stop()

