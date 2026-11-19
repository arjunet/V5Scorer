from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from ScreenView.HomeScreen.home import HomeScreen

# Build the app
class MainApp(MDApp):
    def build(self):
        # Set dark mode
        Window.clearcolor = (0.078, 0.071, 0.094, 1)
        self.theme_cls.theme_style = "Dark"

        # Screen Manager
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='Home'))
        self.sm.current = "Home"
        return self.sm

# Run  
if __name__ == "__main__":
    MainApp().run()