from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
import random, time

cli = OpenRGBClient()

coolers = cli.get_devices_by_name('Lian Li Uni Hub - SL V2 v0.5')[0]

red = RGBColor(255, 0, 0)
green = RGBColor(0, 255, 0)
blue = RGBColor(0, 0, 255)
yellow = RGBColor(255, 255, 0)
black = RGBColor(0, 0, 0)

def switch(color):
        match color:
            case 1:
                coolers.set_color(red)
            case 2:
                coolers.set_color(green)
            case 3:
                coolers.set_color(blue)
            case 4:
                coolers.set_color(yellow)
            case 5:
                coolers.set_color(black)
            case _:
                print("Invalid input")


for i in range(10):
    color = random.randint(1,5)
    switch(color)
    time.sleep(2)