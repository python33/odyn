from numpy import array as v
from OpenGL.GL import glColor3fv

from .base import BaseComponent


class Material(BaseComponent):
    color = v([1., 1., 1.])

    def apply(self):
        glColor3fv(self.color)

    def onRender(self):
        self.apply()
