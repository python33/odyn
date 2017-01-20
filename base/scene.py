from OpenGL.GL import glClearDepth, glClearColor, glDepthFunc, glClear, glEnable, glFrontFace, GL_DEPTH_TEST, GL_LEQUAL, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_CW, GL_CULL_FACE
from .timer import Timer
from .gameobject import GameObject
from .camera import Camera

class Scene(GameObject):
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

        glEnable(GL_DEPTH_TEST)
        glClearDepth(1.0)
        glDepthFunc(GL_LEQUAL)

        glEnable(GL_CULL_FACE)
        glFrontFace(GL_CW)

        self.cam = Camera()
        self.timer = Timer()

    def render(self):
        glClearColor(1.0, 0.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        self.cam.render()

        super(Scene, self).render()

    def _update(self, timer):
        timer.update()
        self.cam.update(timer)

    def update(self):
        super(Scene, self).update(self.timer)
