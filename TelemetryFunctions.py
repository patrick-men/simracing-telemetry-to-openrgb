from unittest import case
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

import random, time

import ACC_telemetry as acc
import LMU_telemetry as lmu

#TODO: Cleanup the different functions
#TODO: Implement the telemetry logic

# initialize the openRGB client
cli = OpenRGBClient()

# You can use print(cli.devices) to get a list of all available devices
##################################
# will be used to signal flags
fans = cli.get_devices_by_name('Lian Li Uni Hub - SL V2 v0.5')[0]
# will be used as a shift light
keyboard = cli.get_devices_by_name('Roccat Vulcan Pro TKL')[0]

# color definitions
neutral = RGBColor(0, 255, 255)
red = RGBColor(255, 0, 0)
green = RGBColor(0, 255, 0)
blue = RGBColor(0, 0, 255)
yellow = RGBColor(255, 255, 0)
orange = RGBColor(255, 128, 0)
black = RGBColor(0, 0, 0)
white = RGBColor(255, 255, 255)

# checkered flag, "blinking black and white"
def checkered():
    for i in range(5):
        fans.set_color(black)
        time.sleep(1)
        fans.set_color(white)
        time.sleep(1)


# function for shift light. Based on rpm Ratio, the light changes - similar to GT cars' shift light, though with "vague", generic ratios
def shiftLight(rpmRatio):
    match rpmRatio:
        case 0:
            return yellow
        case _ if 0 < rpmRatio <= 85:
            return green
        case _ if 85 < rpmRatio <= 93:
            return yellow
        case _ if 93 < rpmRatio <= 100:
            return red
        case _:
            return black

# flag value definitions: https://github.com/rrennoir/PyAccSharedMemory?tab=readme-ov-file#acc_flag_type
def flagLight(flag):
        match flag:
            case 0:
                return neutral
            case 1:
                return blue
            case 2:
                return yellow
            case 3:
                return black
            case 4:
                return white
            case 5:
                return "checkered"
            case 6: # according to doc this is "penalty flag" - TBD which color fits best
                return neutral
            case 7:
                return green
            case 8:
                return orange
            case _:
                print("Invalid input")


def colortest(game):
    if game == "ACC":
        keyboard.set_color(red)

    elif game == "LMU":
        keyboard.set_color(blue)

#keyboard.set_color(orange)
#time.sleep(1)
#keyboard.set_color(neutral)
#checkered()

# acc.init()
# currentRPM = acc.getCurrentRPM()
# print(currentRPM)



# def main():
#   if game=ACC
#     acc.init()
#     acc.getCurrentRPM()
#   else if game=LMU
#     LMU_init()
#
#   while True:
#       getRPM()
#       getMaxRPM()