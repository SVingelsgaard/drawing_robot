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

class LegOne(Image):
    pass

class LegTwo(Image):
    pass

class LegThree(Image):
    pass

kv = Builder.load_file("graphics.kv")

class GUI(App):
    #system variables here
    setCYCLETIME = 0.02 #sec

    #other variable here

    #continus cycle
    def cycle(self, readCYCLETIME):
        #L3Rot = root.ids.leg
        #print(self.root.ids.mScreen.ids.legThree.ids)
        pass
    #runns cycle
    def runApp(self):
        Clock.schedule_interval(self.cycle, self.setCYCLETIME)

    #runs myApp(graphics)
    def build(self):
        return kv

#runs program and cycle
if __name__ == '__main__':
    GUI().run()
