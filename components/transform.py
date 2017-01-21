from OpenGL.GL import glPushMatrix, glTranslatef, glScalef, glRotatef, glPopMatrix
from numpy import array as v

from .base import BaseComponent


class Transform(BaseComponent):
    def __init__(self, game_object):
        self.position = v([0., 0., 0.])
        self.rotation = v([0., 0., 0.])
        self.scale = v([1., 1., 1.])

        super(Transform, self).__init__(game_object)

    def apply(self):
        """
        Applies position, rotation and scale transformations to current matrix.
        """
        # Save matrix state
        glPushMatrix()

        # Apply translations
        glTranslatef(self.position[0], self.position[1], self.position[2])

        # Apply scale transformation
        glScalef(self.scale[0], self.scale[1], self.scale[2])

        # Apply rotations
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)

    def restore(self):
        """
        Restores current matrix to previous state.
        """
        # Restore matrix
        glPopMatrix()
