import cyglfw3 as glfw 


class Keyboard(object):
    def __init__(self, window):
        self._window = window

    def get_key_down(self, key):
        key_code = "KEY_{}".format(key.upper())

        if hasattr(glfw, key_code):
            return glfw.PRESS == glfw.GetKey(self._window, getattr(glfw, key_code))

        return False
