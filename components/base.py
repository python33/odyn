from odyn.base import BaseObject


class BaseComponent(BaseObject):
    def __init__(self, game_object):
        self.game_object = game_object

    def get_component(self, name):
        return self.game_object.get_component(name)

    @property
    def transform(self):
        return self.game_object.transform

    @property
    def material(self):
        return self.game_object.material
