from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import hashlib
from pymongo import MongoClient
import constants as cnst

Window.size = (700, 500)
user_name = ''


class ProductKeyScreen(Screen):

    def check_key(self):
        text = self.text_input_product_key.text

        if hashlib.sha256(text.encode('UTF-8')).hexdigest() == cnst.KEY:
            return True
        return False


class LoginScreen(Screen):

    def login_user(self):
        text_login = self.text_input_login.text
        text_password = self.text_input_password.text

        global collection
        global user_name

        if collection.find_one(
                {
                'user': text_login,
                'password_hash': hashlib.sha256(text_password.encode(
                    'UTF-8')).hexdigest()
                }):
            user_name = text_login
            self.text_input_login.text = ''
            self.text_input_password.text = ''
            return True
        else:
            popup = Popup(
                title='Error',
                content=Label(text='Error Login or Password'),
                size_hint=(0.4, 0.4))
            popup.open()
            return False

    def register_user(self):
        text_login = self.text_input_login.text
        text_password = self.text_input_password.text

        if len(text_login) in range(4, 21)\
                and len(text_password) in range(4, 21):

            global collection
            collection.insert_one(
                {
                    'user': text_login,
                    'password_hash': hashlib.sha256(
                        text_password.encode('UTF-8')).hexdigest(),
                    'role': 'user'
                })
        else:
            popup = Popup(
                title='Error',
                content=Label(text='Error password(4-20)'),
                size_hint=(0.4, 0.4))
            popup.open()

        self.text_input_login.text = ''
        self.text_input_password.text = ''


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


client = MongoClient('localhost', 27017)
db = client.myapp

if 'users' not in db.list_collection_names():
    db.create_collection('users')

collection = db.get_collection('users')

if not collection.find_one({'user': 'root'}):
    collection.insert_one(
        {
            'user': 'root',
            'password_hash': cnst.ROOT,
            'role': 'root'
        })

IsobApp().run()
