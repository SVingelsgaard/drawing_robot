#draws a circle
import time
import math
class Circle():
    def __init__(self):
        #internal attributes
        self.circleAngle = 0

    def circleGraph(self, radius, xOffset, yOffset, speed):
        try:
            time.sleep((speed/360)-0.02)
        except:
            print("Too short time!")
        state = False
        x = ((math.cos(math.radians(self.circleAngle))) * radius + xOffset) #X
        y = ((math.sin(math.radians(self.circleAngle))) * radius + yOffset) #Y
        self.circleAngle += 1

        if self.circleAngle >= 360:
            state = True
            self.circleAngle = 0
        return [x,y,state]
