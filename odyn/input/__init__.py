from odyn.components import BaseComponent
from .keyboard import Keyboard


class Input(BaseComponent):
    def __init__(self, window, game_object, **kwargs):
        self.window = window
        self.keyboard = Keyboard(window)
        super(Input, self).__init__(game_object, **kwargs)
    
