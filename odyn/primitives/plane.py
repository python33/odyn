from numpy import array as v
from OpenGL.GL import glBegin, glEnd, glVertex3fv, GL_TRIANGLES, glColor3fv
from numpy import array as v

from odyn.scene.node import Node
from odyn.components import BaseMesh


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


class Plane(Node):
    def init(self):
        self.add_component(PlaneMesh)
        super(Plane, self).init()

