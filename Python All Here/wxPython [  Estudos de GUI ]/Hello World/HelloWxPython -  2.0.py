import wx



class HomeWorldFrame(wx.Frame):
    def __init__(self, FLG_title):
        super().__init__(None, title=FLG_title)

        self.MainPanel = wx.Panel(self)
        
        texto = wx.StaticText(self.MainPanel, label="Hello wx")
        
        BoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer.Add(texto, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.MainPanel.SetSizer(BoxSizer)

        self.MakeMenuBar()
        self.MakeStatusBar()



    def MakeMenuBar(self):
        MenuBar = wx.MenuBar()

        Hello_World = wx.Menu()
        Hello_World.Append(wx.ID_ABOUT, "Hello World", "é um Hello World melhorado...")
        
        MenuBar.Append(Hello_World, "cc")

        self.SetMenuBar(MenuBar)

    def MakeStatusBar(self):

        self.CreateStatusBar()
        self.SetStatusText("hello world 2.0, aprendendo com a documentação de fato.")



if __name__ == "__main__":
    app = wx.App()

    frame = HomeWorldFrame("hello world 2.0")
    frame.Show()

    app.MainLoop()