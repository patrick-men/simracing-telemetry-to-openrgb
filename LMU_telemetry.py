from templates.sharedMemoryAPI  import SimInfoAPI
from templates.rF2data import *
from TelemetryFunctions import *
import struct

global maxRPM
global currentRPM
global flag # will match values from ACC, see flagLight() in TelemetryFunctions.py

def lmuTelemetry():
    sim = SimInfoAPI()

    if sim.isRF2running():
        if sim.isSharedMemoryAvailable():

            while True:

                # Get telemetry info for player
                telemetry = sim.playersVehicleTelemetry()
                currentRPM = telemetry.mEngineRPM
                maxRPM = telemetry.mEngineMaxRPM


                # Get all relevant flag info // there aren't as many flags that can be read from telemetry as there are in ACC
                scoring = sim.Rf2Scor.mScoringInfo
                vehicleScoring = sim.playersVehicleScoring()
                noFlag = scoring.mYellowFlagState
                greenOrYellowFlag = scoring.mGamePhase
                greenOrBlueFlag = vehicleScoring.mFlag

                sectorYellowFlag = list(scoring.mSectorFlag)
                # find where the "1" is in the list, this indicates the yellow flag's sector - e.g. [11, 11, 1] > yellow flag in sector 3
                # if there are no flags, there is no "1" in the list, thus the "if" statement
                if 1 in sectorYellowFlag:
                    pos = sectorYellowFlag.index(1)
                else:
                    pos = ""
                playerCurrentSector = telemetry.mCurrentSector

                if noFlag == 0: # no flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L70
                   flag = 0
                if greenOrYellowFlag == 5: # green flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L62
                    flag = 7
                elif greenOrYellowFlag == 6: # full course yellow flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L63
                    flag = 2
                elif greenOrYellowFlag == 0: # green flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L120
                    flag = 7
                elif greenOrYellowFlag == 6: # blue flag: https://github.com/TonyWhitley/pyRfactor2SharedMemory/blob/32261e05d4103104d0da8fa0dffcebd441d2cef9/rF2data.py#L121
                    flag = 1
                elif 1 in sectorYellowFlag: # yellow flag if in the same sector as the player
                    if pos == playerCurrentSector:
                        print("hehehe")
                        flag = 2
                else:
                    flag = 0

                print(flag)

                flagLight(flag)
                shiftLight(currentRPM, maxRPM)

                time.sleep(0.1)

lmuTelemetry()