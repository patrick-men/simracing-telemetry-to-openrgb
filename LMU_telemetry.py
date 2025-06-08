from templates.sharedMemoryAPI  import SimInfoAPI
from TelemetryFunctions import *

global maxRPM
global currentRPM
global flag # will match values from ACC, see flagLight() in TelemetryFunctions.py

def lmuTelemetry():
    sim = SimInfoAPI()

    if sim.isRF2running():
        if sim.isSharedMemoryAvailable():

            # Get telemetry info for player
            telemetry = sim.playersVehicleTelemetry()
            currentRPM = telemetry.mEngineRPM
            maxRPM = telemetry.mEngineMaxRPM

            # Get all relevant flag info // there aren't as many flags that can be read from telemetry as there are in ACC
            scoring = sim.playersVehicleScoring()
            noFlag = scoring.YellowFlag
            greenOrYellowFlag = scoring.GamePhase()
            greenOrBlueFlag = scoring.PrimaryFlag()

            if noFlag == 0: # no flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L70
                flag = 0
            elif greenOrYellowFlag == 5: # green flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L62
                flag = 7
            elif greenOrYellowFlag == 6: # yellof flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L63
                flag = 2
            elif greenOrYellowFlag == 0: # green flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L120
                flag = 7
            elif greenOrYellowFlag == 6: # blue flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L121
                flag = 1

        flagLight(flag)
        shiftLight(currentRPM, maxRPM)
