from inputs import *
from controllables import *
from sensors import *
from scriptruntime import *
from ports import *
from color import *
from math import tau
from time import sleep


def main():
    print('template script attached to ' + MicroController.self().name())

    drive()
    stop()
    color()
    
    sleep(10.7)
    stop()
    sleep(1)
    opentrapdoors()
    stop()

def drive():
    DCMotor(0).spin(.5)
    DCMotor(1).spin(.5)
    DCMotor(2).spin(.5)
    DCMotor(3).spin(.5)


def stop():
    DCMotor(0).spin(0)
    DCMotor(1).spin(0)
    DCMotor(2).spin(0)
    DCMotor(3).spin(0)

def opentrapdoors():
    ServoMotor(4).spin_to_degrees(-90)
    ServoMotor(5).spin_to_degrees(-90)

def color():

    color_sensor = ColorSensor(6)
    color = color_sensor.color()

    print(color)

    while True:
                if "farbe_weiss"                       





if __name__ == "__main__":
    main()

