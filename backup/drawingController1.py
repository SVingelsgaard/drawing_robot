import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.image import Image
from kivy.properties import NumericProperty

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
    angle = NumericProperty(0)

class LegTwo(Image):
    angle = NumericProperty(90)

class LegThree(Widget):
    L3image = Image(id="legThree", source="pics/Leg.png" ''', size=self.size''', pos=(171,0))

kv = Builder.load_file("graphics.kv")

class GUI(App):
    #system variables here
    setCYCLETIME = 0.02 #sec

    LegTwo.angle = 90


    class Leg():
        def __init__(self, pos, angle):
            self.pos = pos
            self.angle = angle

    L1 = Leg(kv.ids.mScreen.ids.legOne, 0)
    L2 = Leg(kv.ids.mScreen.ids.legTwo, kv.ids.mScreen.ids.legTwo.angle)
    #L3Pos = kv.ids.mScreen.ids.legThree

    #continus cycle

    def cycle(self, readCYCLETIME):

        self.L2.pos.x += 1
        self.L2.pos.y += 1
        #LegTwo.angle += 1
        print(self.L2.angle)

    #runns cycle
    def runApp(self):
        Clock.schedule_interval(self.cycle, self.setCYCLETIME)

    #runs myApp(graphics)
    def build(self):
        return kv

#runs program and cycle
if __name__ == '__main__':
    GUI().run()
