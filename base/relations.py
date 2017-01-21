from sets import Set
from .object import BaseObject


class ChildParent(BaseObject):
    def __init__(self):
        self.children = Set()
        self.parent = None

    def set_parent(self, parent):
        parent.add_child(self)

    def add_child(self, child):
        if child.parent:
            child.parent.remove_child(child)

        child.parent = self
        self.children.add(child)

    def remove_child(self, child):
        if child.parent == self:
            child.parent = None
            self.children.discard(child)

