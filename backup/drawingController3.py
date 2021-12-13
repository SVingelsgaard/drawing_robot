import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import Label
import math
import matplotlib.pyplot as plt
from kivy.graphics import Line
import time

from functions.circlegraph import Circle

#window settings
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'borderless', '1')

class WindowManager(ScreenManager):
    pass

class StartScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class GraphDrawer(FloatLayout):
    graphList = ListProperty([])

class Base(Image):
    pass

class LegOne(Image):
    angle = NumericProperty(0)
    #pos never changed
    xPos = NumericProperty(-461)
    yPos = NumericProperty(0)

class LegTwo(Image):
    angle = NumericProperty(0)
    xPos = NumericProperty(0)
    yPos = NumericProperty(0)

kv = Builder.load_file("graphics.kv")

class GUI(App):
    #system variables here
    setCYCLETIME = 0.02
    def on_start(self): #variables

        self.controlUnit = 0#driving methode
        #legs
        self.L1 = self.root.get_screen('mainScreen').ids.legOne
        self.L2 = self.root.get_screen('mainScreen').ids.legTwo

        #sliders
        self.L1slider = self.root.get_screen('mainScreen').ids.LegOneSlider
        self.L2slider = self.root.get_screen('mainScreen').ids.LegTwoSlider

        #circle
        self.circleAngle = 0
        self.circleX = 0
        self.circleY = 0

        #drawing algorithm
        self.a = 0 #dictance of origo to andpoint
        self.b = 316 #leg one length
        self.c = 316  #leg two lenght
        self.A = 0 #elbow angle(L2)
        self.B = 0 #origo too endpoint angle
        self.C = 0 #base angle(L1)

        #graph
        self.origoX = 304
        self.origoY = 433
        self.graphDone = False

        #graphin

        self.runTime = 0
        self.graphXrunTime = []
        self.graphL1 = []
        self.graphL2 = []
        self.graphList = self.root.get_screen('mainScreen').ids.graphDrawer.graphList
        #self.graphX = []
        #self.graphY = []


    #continus cycle
    def cycle(self, readCYCLETIME):
        #start delay
        if self.runTime != 0 and self.runTime < .03:
            time.sleep(1)
        #draw graphKd
        if not self.graphDone:
            self.graph()

        #calc angles
        self.drawingAlgorithm()


        #write legs angles
        if self.controlUnit == 0:
            self.L1.angle = self.C #
            self.L2.angle = self.L1.angle - 180 + self.A #L1 angle needs to be added because it is atached to it(same as with the sliders in else statment below). then since the angel is calculated from laying on top of the other leg we need - 180 before we can add the calculated angel.
            self.L1slider.value = self.L1.angle
            self.L2slider.value = - self.L1.angle + self.L2.angle

        else:
            self.L1.angle = self.L1slider.value
            self.L2.angle = self.L1.angle + self.L2slider.value#L1 angle needs to be added because it is atached to it(same as with the sliders in else statment below).

        #Leg two position dependent on leg one angle
        self.L2.xPos = -461 +(math.cos(math.radians(self.L1.angle))*316)#-461 is x distanc to be same point as leg one
        self.L2.yPos = (math.sin(math.radians(self.L1.angle))*316)



        #graph
        self.runTime += readCYCLETIME
        self.graphXrunTime.append(self.runTime)
        self.graphL1.append(self.L1.angle)
        self.graphL2.append(self.L2.angle)

        #drawing endpoint. simpel trig
        self.graphList.append((self.origoX + self.L2.xPos +461) + math.cos(math.radians(self.L2.angle))*self.c) #+461 bc its the center of orbit with we calculate from

        self.graphList.append((self.origoY + self.L2.yPos) + math.sin(math.radians(self.L2.angle))*self.c)


    def ControlUnit(self):
        if self.controlUnit == 1:
            self.controlUnit = 0
        else:
            self.controlUnit = 1
    def graph(self):
        #running cicle-framnsilling
        if self.circleAngle < 360:

            self.circleAngle = self.circleAngle + 1

            #self.circleX = 100+self.circleAngle
            #self.circleY = -200+self.circleAngle

            self.circleX = ((math.cos(math.radians(self.circleAngle)))*200+690) #X
            self.circleY = ((math.sin(math.radians(self.circleAngle)))*200+433) #Y

        else:
            #self.graphDone = True
            #self.showGraph()
            self.circleAngle = 0


    def drawingAlgorithm(self): #one itteration of drawAlg. actually the movment alg. drawing is done in cycle atm
        #finding lengt of a(dictance form origo to andpoint)
        self.a = math.sqrt(((self.circleX-self.origoX)**2) + ((self.circleY-self.origoY)**2))

        #finding angel A for getting right length. force angles: 0 = 136, 180 = 34,2, 90 = 86.7
        self.A = math.degrees(1/2 * math.pi + math.asin((self.a**2 - self.b**2 - self.c**2)/(2 * self.b * self.c))) #hard triginomery.


        #finding angle B (origo to endpoint angle)
        self.B = math.degrees(math.atan((self.circleY-self.origoY) / (self.circleX-self.origoX)))#simpel trigonometry


        #finding angle C (base angle)
        self.C = self.B + (180 - self.A) / 2 #180-A = de 2 siste vinklene i trekanten. /2 får vinkelen mellom L1 og linjen til endepunkt. +B som er vinkelen til endepunktet(horisontal)

    #shows graph
    def showGraph(self):
        #main plot
        fig, (pltB, pltA, pltC) = plt.subplots(3, sharex=False)
        pltB.set(title = 'Angle logging')

        #kp plot
        pltB.grid(True)
        pltB.set(ylabel = 'Base angle')
        pltB.plot(self.graphXrunTime, self.graphL1)

        #ki plot
        pltA.grid(True)
        pltA.set(ylabel = 'Elbow angle')
        pltA.plot(self.graphXrunTime, self.graphL2)

        pltC.grid(True)
        pltC.set(ylabel = 'Elbow angle')
        pltC.plot(self.graphL1, self.graphL2)
        plt.show()


    #runns cycle
    def runApp(self):
        Clock.schedule_interval(self.cycle, self.setCYCLETIME)


    #runs myApp(graphics)
    def build(self):
        return kv

#runs program and cycle
if __name__ == '__main__':
    GUI().run()
