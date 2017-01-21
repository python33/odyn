class BaseComponent(object):
    def __init__(self, game_object, is_visible=True):
        self.game_object = game_object
        self.is_visible = is_visible

    def show(self):
        self.is_visible = True

    def hide(self):
        self.is_visible = False

    def pre_init(self):
        pass

    def init(self):
        """
        Component initialization callback.
        """
        pass

    def post_init(self):
        pass

    def update(self, timer):
        """
        Compoent update callback.

        Arguments:
            timer :obj:base.Timer Timer object
        """
        pass

    def render(self):
        pass
