from numpy import array as v
from OpenGL.GL import glColor3fv


class Material(object):
    def __init__(self, color=v([1.0, 1.0, 1.0])):
        self.color = color

    def apply(self):
        glColor3fv(self.color)


    
