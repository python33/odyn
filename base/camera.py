from numpy import array as v
from OpenGL.GLU import gluPerspective, gluLookAt
from OpenGL.GL import glMatrixMode, glLoadIdentity, GL_MODELVIEW, GL_PROJECTION

from .gameobject import GameObject


class Camera(GameObject):
    fov = 45.0
    aspect_ratio = 1.4
    z_near = 0.1
    z_far = 1000.0
    
    def __init__(self, look_at=v([0.0,0.0,0.0]), **kwargs):
        self.look_at = look_at
        kwargs['pos'] = kwargs.get('pos', None) or v([5., 5., 5.])
        super(Camera, self).__init__(**kwargs)

    def resize(self, width, height):
        self.aspect_ratio = width/height
        self.update_projection()

    def update_projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fov, self.aspect_ratio, self.z_near, self.z_far)

    def update_model_view(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            self.transform.position[0], self.transform.position[1], self.transform.position[2],
            self.look_at[0], self.look_at[1], self.look_at[2],
            0.0, 1.0, 0.0
        )

    def render(self):
        self.update_projection()
        self.update_model_view()
