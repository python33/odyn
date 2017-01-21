from numpy import array as v
from OpenGL.GL import glBegin, glEnd, glVertex3fv, GL_TRIANGLES, glColor3fv
from numpy import array as v

from game.base import GameObject
from game.base.components import BaseMesh


class PlaneMesh(BaseMesh):
    vertices = [
        v([-1.0,  0.0, -1.0]),
        v([ 1.0,  0.0, -1.0]),
        v([ 1.0,  0.0,  1.0]),
        v([-1.0,  0.0,  1.0]),
    ]

    render_path = [
        0, 1, 2,
        3, 0, 2
    ]


class Plane(GameObject):
    def pre_init(self):
        self.components.append(PlaneMesh(self))
        super(Plane, self).pre_init()

