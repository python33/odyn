from numpy import array as v

from base.components import Transform, Material
from base.relations import ChildParent


class GameObject(ChildParent):
    def __init__(self, pos=v([0.0, 0.0, 0.0]), rot=v([0.0, 0.0, 0.0]), scale=v([1.0, 1.0, 1.0])):
        self.transform = Transform(pos, rot, scale)
        self.material = Material()
        self.components = []
        super(GameObject, self).__init__()

    def pre_init(self):
        for c in self.components:
            c.pre_init()

        for o in self.children:
            o.pre_init()

    def init(self):
        """
        Initialziation callback
        """
        for c in self.components:
            c.init()

        for o in self.children:
            o.init()

    def post_init(self):
        for c in self.components:
            c.post_init()

        for o in self.children:
            o.post_init()


    def render(self):
        """
        Render event callback
        """
        self.transform.apply()
        self.material.apply()

        for c in self.components:
            if c.is_visible:
                c.render()

        for o in self.children:
            o.render()

        self.transform.restore()

    def update(self, timer):
        """
        Update event callback

        Arguments:
            timer :obj:base.Timer - timer object
        """

        for c in self.components:
            c.update(timer)

        for o in self.children:
            o.update(timer)
