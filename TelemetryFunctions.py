#### This file contains general funcs to handle telemetry data. The telemetry itself comes from another file ####

from unittest import case
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

import random, time

#TODO: Cleanup the different functions
#TODO: Implement the telemetry logic

# initialize the openRGB client
cli = OpenRGBClient()

############################################################################
## You can use print(cli.devices) to get a list of all available devices  ##
## For simplicity's sake I just hardcoded mine                            ##
############################################################################

# will be used to signal flags
flagDevice = cli.get_devices_by_name('Lian Li Uni Hub - SL V2 v0.5')[0]
# will be used as a shift light
shiftDevice = cli.get_devices_by_name('Roccat Vulcan Pro TKL')[0]

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
        flagDevice.set_color(black)
        time.sleep(1)
        flagDevice.set_color(white)
        time.sleep(1)


def rpmRatioCalc(currentRPM, maxRPM):
    rpmRatio = (currentRPM / maxRPM) * 100
    return rpmRatio

# function for shift light. Based on rpm Ratio, the light changes - similar to GT cars' shift light, though with "vague", generic ratios

def shiftLight(currentRPM, maxRPM):
    rpmRatio = rpmRatioCalc(currentRPM, maxRPM)
    match rpmRatio:
        case 0:
            shiftDevice.set_color(black)
        case _ if 0 < rpmRatio <= 80:
            shiftDevice.set_color(green)
        case _ if 80 < rpmRatio <= 88:
            shiftDevice.set_color(yellow)
        case _ if 88 < rpmRatio <= 100:
            shiftDevice.set_color(red)
        case _:
            shiftDevice.set_color(black)

# flag value definitions: https://github.com/rrennoir/PyAccSharedMemory?tab=readme-ov-file#acc_flag_type
def flagLight(flag):
        match flag:
            case 0: # no flag
                flagDevice.set_color(neutral)
            case 1: # blue flag
                flagDevice.set_color(blue)
            case 2: # yellow flag
                flagDevice.set_color(yellow)
            case 3: # black flag
                flagDevice.set_color(black)
            case 4: # white flag
                flagDevice.set_color(white)
            case 5: # checkered flag
                checkered()
            case 6: # according to doc this is "penalty flag" - TBD which color fits best
                flagDevice.set_color(neutral)
            case 7: # green flag
                flagDevice.set_color(green)
            case 8: # orange flag
                flagDevice.set_color(orange)
            case _: # catching possible errors, or non-relevant output when e.g. in menu
                flagDevice.set_color(neutral)
