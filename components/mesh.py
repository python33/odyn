from numpy import array as v
from OpenGL.GL import glBegin, glEnd, glVertex3fv, GL_TRIANGLES, glColor3fv

from .base import BaseComponent


class BaseMesh(BaseComponent):
    verticies = []
    render_path = []
    
    def onRender(self):
        glBegin(GL_TRIANGLES)
        for i in self.render_path:
            glVertex3fv(self.vertices[i])
        glEnd()
