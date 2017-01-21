from OpenGL.GL import glClearDepth, glClearColor, glDepthFunc, glClear, glEnable, glFrontFace, GL_DEPTH_TEST, GL_LEQUAL, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_CW, GL_CULL_FACE
from cyglfw3 import GetTime

from .node import Node
from .camera import Camera
from odyn.input import Input


class Timer(object):
    def __init__(self):
        self.tick = GetTime()
        self.last_tick = self.tick
        self.delta = 0

    def update(self):
        self.last_tick = self.tick
        self.tick = GetTime()
        self.delta = self.tick - self.last_tick

    def __repr__(self):
        return "<Timer lt: {}; t: {}; d: {}>".format(self.last_tick, self.tick, self.delta)


class Scene(Node):
    def __init__(self, window):
        self.timer = Timer()
        self.window = window
        super(Scene, self).__init__()

    def onInit(self):
        glEnable(GL_DEPTH_TEST)
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)

        glEnable(GL_CULL_FACE)
        glFrontFace(GL_CW)

        self.cam = Camera(self.window)
        self.timer = Timer()

        # Register Input component
        self.components.append(Input(self.window, self))

    def onRender(self):
        glClearColor(1.0, 0.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        self.cam.onRender()

    def update(self):
        self.timer.update()
        super(Scene, self).update(self.timer)
