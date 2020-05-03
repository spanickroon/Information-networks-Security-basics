from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (700, 500)
Window.title = 'kek'


class ProductKeyScreen(Screen):
    pass


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
