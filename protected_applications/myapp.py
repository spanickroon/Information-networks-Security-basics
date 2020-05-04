from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import hashlib
import pymongo

import constants as cnst

Window.size = (700, 500)
Window.title = 'kek'


class ProductKeyScreen(Screen):

    def check_key(self):
        text = self.text_input_product_key.text

        if hashlib.sha256(text.encode('UTF-8')).hexdigest() == cnst.KEY:
            print('kek')
            return True
        return False


class LoginScreen(Screen):
    pass


class AppScreen(Screen):
    pass


class UserManagementScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


scr = Builder.load_file('myapp.kv')


class IsobApp(App):

    def build(self):
        return scr


IsobApp().run()
