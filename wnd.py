import cyglfw3 as glfw
from base import BaseApplication
from primitives import Box, Plane
from numpy import array as v


class App(BaseApplication):
    def init(self):
        self.scene.add_child(Box())
        self.scene.add_child(Plane(scale=v([5,5,5])))

        super(App, self).init()

App().run()
