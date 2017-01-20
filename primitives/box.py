from numpy import array as v
from OpenGL.GL import glBegin, glEnd, glVertex3fv, GL_TRIANGLES, glColor3fv

from base import GameObject
from base.components import BaseMesh

class BoxMesh(BaseMesh):
    vertices = [
        v([-1,-1,-1]), v([1,-1,-1]),  v([1,1,-1]), v([-1,1,-1]),
        v([-1,-1, 1]), v([1,-1, 1]),  v([1,1, 1]), v([-1,1, 1])
    ]
    render_path = [
        0, 1, 2, # front
        0, 2, 3,
        3, 2, 7, # top
        7, 2, 6,
        2, 1, 5, # right
        2, 5, 6,
        4, 7, 6, # back
        6, 5, 4,
        4, 3, 7, # left
        4, 0, 3,
        4, 1, 0, # bottom
        4, 5, 1,
    ]
    

class Box(GameObject):
    def pre_init(self):
        self.components.append(BoxMesh())
        super(Box, self).pre_init()
