from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class MainWidget(GridLayout):
    mytext = 'hello'

    def count(self):
        self.mytext = 'hey'


class TheLabelApp(App):
    pass


TheLabelApp().run()
