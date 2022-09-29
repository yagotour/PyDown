import wx
from wx.adv import TaskBarIcon as TaskBarIcon


class MyTaskBarIcon(TaskBarIcon):
    def __init__(self, frame):
        TaskBarIcon.__init__(self)

        self.frame = frame

        self.SetIcon(wx.Icon('./icono.png', wx.BITMAP_TYPE_PNG), 'Task bar icon')

        # ------------

        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=1)
        self.Bind(wx.EVT_MENU, self.OnTaskBarDeactivate, id=2)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=3)

    # -----------------------------------------------------------------------

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(1, 'Show')
        menu.Append(2, 'Hide')
        menu.Append(3, 'Close')

        return menu

    def OnTaskBarClose(self, event):
        self.frame.Close()

    def OnTaskBarActivate(self, event):
        if not self.frame.IsShown():
            self.frame.Show()

    def OnTaskBarDeactivate(self, event):
        if self.frame.IsShown():
            self.frame.Hide()


# ---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (-1, -1), (290, 280))

        self.SetIcon(wx.Icon('./icono.png', wx.BITMAP_TYPE_PNG))
        self.SetSize((350, 250))

        # ------------

        self.tskic = MyTaskBarIcon(self)

        # ------------

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # ------------

        self.Centre()

    # -----------------------------------------------------------------------

    def OnClose(self, event):
        self.tskic.Destroy()
        self.Destroy()


# ---------------------------------------------------------------------------

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'wx.adv - TaskBarIcon')
        frame.Show(True)
        self.SetTopWindow(frame)

        return True


# ---------------------------------------------------------------------------

app = MyApp(0)
app.MainLoop()
