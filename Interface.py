import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.popup import Popup
from extracting_reviews import trailers


class MyGrid(Widget):
    """
    ...
    """

    def btn(self):

        show_popup()

    def btn2(self):
        show_popup2()

    def btn3(self):
        show_popup3()
    #
    def image_appear(self):
        self.ids.my_image1.source = "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F44%2F2016%2F06%2F03%2F3755319.jpg"
        self.ids.my_image2.source = "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F44%2F2016%2F06%2F03%2F3755319.jpg"
        self.ids.my_image3.source = "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F44%2F2016%2F06%2F03%2F3755319.jpg"


class P(FloatLayout):
    def ytube(self):
        show_trailer()

    def text1(self):
        description()

    def review1(self):
        reviews_1()


class P2(FloatLayout):
    def ytube2(self):
        show_trailer2()

    def text2(self):
        description2()

    def review2(self):
        reviews_2()


class P3(FloatLayout):
    def ytube3(self):
        show_trailer3()

    def text3(self):
        description3()

    def review3(self):
        reviews_3()


class Top3(App):
    def build(self):
        Window.size = (700, 600)
        return MyGrid()


def show_popup():
    """
    ...
    """
    show = P()
    popup_window = Popup(title="Movie 1", content=show, size_hint=(None, None), size=(550, 600))

    popup_window.open()


def show_popup2():
    """
    ...
    """
    show = P2()
    popup_window = Popup(title="Movie 2", content=show, size_hint=(None, None), size=(550, 600))

    popup_window.open()


def show_popup3():
    """
    ...
    """
    show = P3()
    popup_window = Popup(title="Movie 3", content=show, size_hint=(None, None), size=(550, 600))

    popup_window.open()


def show_trailer():
    trailers('Wonder Woman')


def show_trailer2():
    trailers('Dark Tower')


def show_trailer3():
    trailers('Avatar')


def description():
    print("this is a story about....")


def description2():
    print("this is a story about....")


def description3():
    print("this is a story about....")


def reviews_1():
    print("Reviews for movie 1")


def reviews_2():
    print("Reviews for movie 2")


def reviews_3():
    print("Reviews for movie 3")

def show_image():
    return "'http://mysite.com/test.png'"


if __name__ == '__main__':
    Top3().run()
