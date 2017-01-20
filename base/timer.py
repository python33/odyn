import time

class Timer(object):
    def __init__(self):
        self.tick = time.time()
        self.last_tick = time.time()

    def update(self):
        self.last_tick = self.tick
        self.tick = time.time()

    @property
    def delta(self):
        return self.tick - self.last_tick

