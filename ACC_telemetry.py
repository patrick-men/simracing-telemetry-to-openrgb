from pyaccsharedmemory import accSharedMemory
from TelemetryFunctions import *

def accTelemetry():
    sm = accSharedMemory().read_shared_memory()

    while True:
        flag=sm.Graphics.flag.value
        currentRPM = sm.Physics.rpm
        maxRPM = sm.Static.max_rpm # Static data *PER* car - kept in while-loop to update automatically if car is changed

        flagLight(flag)
        shiftLight(currentRPM, maxRPM)

        print("Max RPM:",maxRPM)

        print("current RPM:", currentRPM)

        time.sleep(0.1)

        accTelemetry().close()