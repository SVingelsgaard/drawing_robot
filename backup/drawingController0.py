import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.image import Image

#window settings
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'borderless', '1')

class WindowManager(ScreenManager):
    pass

class StartScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class Base(Image):
    pass

class LegOne(Widget):
    pass

class LegTwo(Widget):
    pass

class LegThree(Widget):
    pass

kv = Builder.load_file("graphics.kv")

class GUI(App):
    #system variables here
    setCYCLETIME = 0.02 #sec

    L2Pos = kv.ids.mScreen.ids.legTwo
    L3Pos = kv.ids.mScreen.ids.legThree

    #continus cycle

    def cycle(self, readCYCLETIME):


        #print(self.root.ids.mScreen.ids.legThree.ids)
        self.L2Pos.x += 1
        self.L2Pos.y += 1

    #runns cycle
    def runApp(self):
        Clock.schedule_interval(self.cycle, self.setCYCLETIME)

    #runs myApp(graphics)
    def build(self):
        return kv

#runs program and cycle
if __name__ == '__main__':
    GUI().run()
