import wx
import requests
from io import BytesIO
from PIL import Image

###
#
#  PRIMEIRO PROJETO USANDO O WXPYTHON, UM HELLO WORLD SIMPLES E BEM COMPLICADO T-T
#
##


class getImageBytes:
    def GetImage(url):
        try:
            data = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}).content
            load = Image.open(BytesIO(data))
            return wx.Bitmap(wx.ImageFromBuffer(load.width, load.height, load.tobytes()).Rescale(351, 240))
        
        except Exception as e:
            print(e)
            return False


class App(wx.App):
    def OnInit(self):
        Home = FrameIMSTR()
        Home.Centre()
        Home.Show()

        return True
    
    
class FrameIMSTR(wx.Frame):
    def __init__(self):
        super().__init__(None, title="IMString", style=wx.DEFAULT_FRAME_STYLE & ~(wx.MAXIMIZE_BOX | wx.RESIZE_BORDER), size=(600, 300))

        self.__MakePanels()
        self.__MakeWidgets()
        self.__RenderWidgets()
        self.__DefineBinds()
        

    def __MakePanels(self):
        self.MainPanel = wx.Panel(self)
        self.MainGrid = wx.GridBagSizer(5, 4)
        self.MainPanel.SetSizer(self.MainGrid)

        self.EntryPanel = wx.Panel(self.MainPanel)
        self.EntryPanelGrid = wx.BoxSizer(wx.VERTICAL)   
        self.EntryPanel.SetSizer(self.EntryPanelGrid)
        
    
    def __MakeWidgets(self):
        #####      Layout      #####
        ## |         | |  Text   |
        ## |  IMAGE  | |   __    |
        ## |         | | Search  |
        ## |     Status Bar      |

        self.PreviewImage = wx.StaticBitmap(self.MainPanel, bitmap=wx.Bitmap("recursos/image_placeholder.jpg", wx.BITMAP_TYPE_JPEG))        
        self.ImageName = wx.StaticText(self.EntryPanel, label='Here Is Your Url Image Preview\nPress Enter After Insert Your URL', style=wx.TE_CENTER)
        self.InputImageURL = wx.TextCtrl(self.EntryPanel, style=wx.TE_PROCESS_ENTER, size=(150, 20))
    
    def __RenderWidgets(self):
        self.MainGrid.Add(self.PreviewImage, pos=(0, 0), flag=wx.EXPAND | wx.ALL, border=10)
        
        self.EntryPanelGrid.AddStretchSpacer()
        self.EntryPanelGrid.Add(self.ImageName, 1, flag=wx.EXPAND)
        self.EntryPanelGrid.Add(self.InputImageURL, 0, flag=wx.ALIGN_CENTER)
        self.EntryPanelGrid.AddStretchSpacer()
        self.EntryPanelGrid.AddStretchSpacer()
        
        self.MainGrid.Add(self.EntryPanel, pos=(0, 2), flag=wx.EXPAND)
        self.Layout()

    def __DefineBinds(self):
        def Enter_InputImageURL(Event):
            self.InputImageURL.Enable(False)
            InputImageURLValue = self.InputImageURL.GetValue()

            bitmap = getImageBytes.GetImage(InputImageURLValue if len(InputImageURLValue) != 0 else "https://static.dicio.com.br/upload/an/im/animal-com-a-og.jpg")
            if bitmap != False:
                self.PreviewImage.SetBitmap(bitmap)
                self.InputImageURL.SetValue("")

            wx.CallLater(100, __InputImageURLActive)
            

        def __InputImageURLActive():
            self.InputImageURL.Enable(True)
            self.InputImageURL.SetFocus()

        self.InputImageURL.Bind(wx.EVT_TEXT_ENTER, Enter_InputImageURL)

if __name__ == "__main__":
    App().MainLoop()