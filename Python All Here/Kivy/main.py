from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# class Login(BoxLayout):
#     # def __init__(self, **kwargs):
#     #     super(Login, self).__init__(**kwargs)
#     #     self.orientation = 'vertical'
#     #     self.__InsertItems()

#     # def __InsertItemsManualy(self):
#     #     self.add_widget(Label(text="Login"))
#     #     self.add_widget(TextInput(multiline=False))

class FirstLayout(BoxLayout):
    pass


class AppBuilder(App):
    def build(self):
        return FirstLayout()
    

if __name__ == "__main__":
    AppBuilder().run()