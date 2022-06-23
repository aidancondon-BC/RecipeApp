from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.animation import Animation

from analyze import Analyzer
from user import User

Builder.load_file('interface.kv')

class WelcomePage(Screen):
    pass

class IngredientsPage(Screen):
    pass

class EndPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainWindow(StackLayout):

    alzr = Analyzer()
    usr = User()

    path_to_IP = None
    
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.path_to_IP = self.ids.ingredients.ids

    def implementSearchResults(self):
        self.path_to_IP.searchResults.clear_widgets()
        search = self.path_to_IP.searchBar.text
        if len(search) <= 2: return
        layout = GridLayout(cols=1,rows=10)
        for result in self.alzr.searchForIngredient(search):
            color = 'green' if self.usr.isSelected(result) else 'red'
            cur_button = Button(text=result,
                                background_color=color)
            cur_button.bind(on_press=self.clickIngredient)
            layout.add_widget(cur_button)
        self.path_to_IP.searchResults.add_widget(layout)

    def clickIngredient(self, instance):
        if instance.background_color == [1.0, 0.0, 0.0, 1.0]:
            instance.background_color = 'green'
            self.usr.add_ingredient(instance.text)
        else:
            instance.background_color = 'red'
            self.usr.delete_ingredient(instance.text)
        self.implementSelected()

    def implementSelected(self):
        self.path_to_IP.selected.clear_widgets()
        layout = GridLayout(cols=1,rows=10)
        for ingredient in self.usr.get_ingredients():
            cur_button = Button(text=ingredient,
                                background_color='blue')
            layout.add_widget(cur_button)
        self.path_to_IP.selected.add_widget(layout)

    pass

class myApp(MDApp):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    st = myApp()
    st.run()