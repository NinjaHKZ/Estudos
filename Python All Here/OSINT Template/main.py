from tkinter import Tk, Frame, Label, PhotoImage
from PIL import Image, ImageTk

class workbench:
    def load_image(image, width, height):
        try:
            ProfilePicture = Image.open(image)
        except FileNotFoundError:
            ProfilePicture = Image.open("NotFoundImage.png")
        

        ProfilePicture.thumbnail((width, height))
        return ImageTk.PhotoImage(ProfilePicture)

class BuildLandPage:
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow

        self._makeFrames()
        self._makeImages()

        self._makeLabels()
    
        self.ProfilePictureFrame.update()

    def _makeFrames(self):
        self.ProfilePictureFrame = Frame(
            master=self.MainWindow, 
            width=232, 
            height=226,
            highlightthickness=2,
            highlightbackground='#A52828'
        )

        self.ProfileInfoFrame = Frame(
            master=self.MainWindow,
            width=395,
            height=226,
            bg="green"
        )

        self.ImageRollFrame = Frame(
            master=self.MainWindow,
            width=694,
            height=181,
            bg="gray"
        )

        self.AboutDescibeFrame = Frame(
            master=self.MainWindow,
            width=694,
            height=200,
            bg="yellow"
        )
        
        self.ProfilePictureFrame.place(x=85, y=27)
        self.ProfileInfoFrame.place(x=384, y=27)
        self.ImageRollFrame.place(x=85, y=284)
        self.AboutDescibeFrame.place(x=85, y=496)

    def _makeLabels(self):
        self.ProfilePictureImage = Label(
            master=self.ProfilePictureFrame,
            image=self.ProfilePicture
        )

        self.ProfilePictureImage.image = self.ProfilePicture

        self.ProfilePictureImage.place(x=0.01, y=0.01)

    def _makeImages(self):
        self.ProfilePicture = workbench.load_image(
            "NotFoundImage.png",
            self.ProfileInfoFrame.winfo_reqwidth()-20,
            self.ProfileInfoFrame.winfo_reqheight()-20
            )


        
class MyAplication(Tk):
    def __init__(self):
        super().__init__()

        self.builder()
        BuildLandPage(self)
        self.mainloop()

    def builder(self):
        self.geometry("863x713")
        self.title("pure tkinter basics")



if __name__ == "__main__":
    MyAplication()