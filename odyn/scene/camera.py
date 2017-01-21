from numpy import array as v
from OpenGL.GLU import gluPerspective, gluLookAt
from OpenGL.GL import glMatrixMode, glLoadIdentity, GL_MODELVIEW, GL_PROJECTION
from cyglfw3 import SetWindowSizeCallback, GetWindowSize


class Camera(object):
    fov = 45.0
    z_near = 0.1
    z_far = 1000.0
    
    def __init__(self, window, eye=v([5., 5., 5.]), look_at=v([0.0,0.0,0.0]), up=v([0., 1., 0.])):
        self._window = window
        self.eye = eye
        self.look_at = look_at
        self.up = up

        # Calculate aspect ratio based on window size
        width, height = GetWindowSize(window)
        self.resize(window, width, height)

        # Set resize callback
        SetWindowSizeCallback(window, self.resize)

    def resize(self, wnd, width, height):
        self.aspect_ratio = float(width)/float(height)

    def update_projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fov, self.aspect_ratio, self.z_near, self.z_far)

    def update_model_view(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            self.eye[0], self.eye[1], self.eye[2],
            self.look_at[0], self.look_at[1], self.look_at[2],
            self.up[0], self.up[1], self.up[2]
        )

    def onRender(self):
        self.update_projection()
        self.update_model_view()
