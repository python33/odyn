class BaseObject(object):
    enabled = True

    def init(self):
        """ Do not override this method. Use OnInit instead.  """
        self.onInit()

    def ready(self):
        """ Do not override this method. Use OnReady instead.  """
        self.onReady()

    def render(self):
        """ Do not override this method. Use OnRender instead.  """
        if self.enabled:
            self.onRender()

    def update(self, timer):
        """ Do not override this method. Use OnUpdate instead.  """
        if self.enabled:
            self.onUpdate(timer)

    def onInit(self):
        """
        Component initialization callback.
        """
        pass

    def onReady(self):
        """
        Ready callback calls when all components initialized.
        """
        pass

    def onUpdate(self, timer):
        """
        Update callback. Component logic should be done here.

        Arguments:
            timer :obj:base.Timer Timer object
        """
        pass

    def onRender(self):
        """
        Render callbac. Calls every frame.
        """
        pass
