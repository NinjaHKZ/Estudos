import customtkinter 
from tkinter import Tk, PhotoImage
from PIL import Image, ImageTk
import json, webbrowser

class FirstWindow:
    def __init__(self, Window):
        self.Window = Window
        
        self._prepare_resources()
        self._design_layout()
        self._ctklabel_draw()
        self._CTkButtons_Entry_draw()
        self._CTkBind_Events()
        self._place_items()        


    def _design_layout(self):
        self.BaseFrame = customtkinter.CTkFrame(
            master=self.Window,
            width=350,
            height=396,
            fg_color='white'
            )

        self.EntryFrame = customtkinter.CTkFrame(
            master=self.Window,
            width=350,
            height=396,
            fg_color='white'
        )

        self.BaseFrame.pack(side="left")
        self.EntryFrame.pack(side="right")



    def _prepare_resources(self):
        self.img = PhotoImage(file="github.png").subsample(2, 2)

        with open("files/font.json", 'r') as r:
            self.FONTS = json.load(r)


    def _ctklabel_draw(self):
        self.label_img = customtkinter.CTkLabel(
            master=self.BaseFrame,
            text='',
            image=self.img
        )

        self.label_loginTitle = customtkinter.CTkLabel(
            master=self.EntryFrame,
            text='Login Screen [ CTk ]',
            font=tuple(self.FONTS['loginFrameTitle'])
        )

        self.label_Login = customtkinter.CTkLabel(
            master=self.EntryFrame,
            text='Login',
            font=tuple(self.FONTS['login'])
        )

        self.label_Password = customtkinter.CTkLabel(
            master=self.EntryFrame,
            text='Password',
            font=tuple(self.FONTS['password'])        
            )
        

    def _CTkButtons_Entry_draw(self):
        self.login_entry = customtkinter.CTkEntry(
            master=self.EntryFrame,
            width=280,
            height=15,
            placeholder_text='Insert your login here...'
        )

        self.password_entry = customtkinter.CTkEntry(
            master=self.EntryFrame,
            width=280,
            height=15,
            placeholder_text="Insert here your password..."
        )

        self.send_button = customtkinter.CTkButton(
            master=self.EntryFrame,
            text="Submit"
        )

    def _CTkBind_Events(self):
        self.send_button.bind("<Button-1>", lambda event: webbrowser.open("https://github.com/NinjaHKZ/Estudos/tree/main/Python All Here/tkinterGui"))

    def _place_items(self):
        self.label_img.place(x=25, y=5)

        self.label_loginTitle.place(x=25, y=5)
        self.label_Login.place(x=25, y=100)
        self.label_Password.place(x=25, y=180)

        self.login_entry.place(x=25, y=130)
        self.password_entry.place(x=25, y=210)

        self.send_button.place(relx=0.45, rely=0.7, anchor='center')

class HWApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self._builder()
        FirstWindow(Window=self)
        self.mainloop()

    def _builder(self):
        self.geometry("700x400")
        self.title("Tk GUI Learning")
        self.resizable(False, False)
        customtkinter.set_appearance_mode("light")

if __name__ == "__main__":

    HWApp()