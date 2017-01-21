from numpy import array as v

from odyn.components import Transform, Material
from odyn.base.relations import ChildParent


class Node(ChildParent):
    def __init__(self, **kwargs):
        self.transform = Transform(self, **kwargs)
        self.material = Material(self)
        self.components = []
        super(Node, self).__init__()

    def add_component(self, cls):
        self.components.append(cls(self))

    def get_component(self, name):
        for c in self.components:
            if c.__class__.__name__ == name:
                return c

            if self.parent:
                return self.parent.get_component(name)

            return None

    def init(self):
        self.onInit()

        for c in self.components: c.init()
        for o in self.children: o.init()

    def ready(self):
        self.onReady()

        for c in self.components: c.ready()
        for o in self.children: o.ready()


    def render(self):
        """
        Render event callback
        """
        if not self.enabled: return

        self.transform.apply()
        self.material.apply()

        self.onRender()

        for c in self.components: c.render()
        for o in self.children: o.render()

        self.transform.restore()

    def update(self, timer):
        """
        Update event callback

        Arguments:
            timer :obj:base.Timer - timer object
        """

        self.onUpdate(timer)

        for c in self.components: c.update(timer)
        for o in self.children: o.update(timer)

    def __repr__(self):
        return "<{} p: {}; r: {}; s: {}>".format(
            self.__class__.__name__,
            self.transform.position,
            self.transform.rotation,
            self.transform.scale
        )
