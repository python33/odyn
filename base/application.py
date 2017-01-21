import cyglfw3 as glfw

from .scene import Scene


class ApplicationException(Exception):
    pass


class BaseApplication(object):
    def __init__(self, width=800, height=600, title='GLFW Window'):
        self.__initGLFW()
        self.window = self.__createWindow(width, height, title)
        self.scene = Scene(self.window)

    def __initGLFW(self):
        if not glfw.Init():
            raise ApplicationException('Failed to initiazlize GLFW')

    def __createWindow(self, width, height, title):
        glfw.WindowHint(glfw.CLIENT_API, glfw.OPENGL_API)
        glfw.WindowHint(glfw.CONTEXT_VERSION_MAJOR, 2)
        glfw.WindowHint(glfw.CONTEXT_VERSION_MINOR, 1)

        window = glfw.CreateWindow(width, height, title)

        if not window:
            glfw.Terminate()
            raise ApplicationException('Failed to create GLFW Window')

        glfw.MakeContextCurrent(window)

        return window

    def init(self):
        self.scene.pre_init()
        self.scene.init()
        self.scene.post_init()

    def run(self):
        self.init()

        while not glfw.WindowShouldClose(self.window):
            self.scene.update()
            self.scene.render()
            glfw.SwapBuffers(self.window)
            glfw.PollEvents()
    
        glfw.Terminate()
