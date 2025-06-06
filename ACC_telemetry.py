from pyaccsharedmemory import accSharedMemory

#TODO: Create func that returns flag values
#TODO: Cleanup

# initialize sm var
sm = None

def init():
    global sm
    sm = accSharedMemory().read_shared_memory()


def getMaxRPM(sm):
    MaxRPM = sm.Static.max_rpm
    return MaxRPM

def getCurrentRPM():
    currentRPM = sm.Physics.rpm
    return currentRPM

if (sm is not None):
    print("Physics:")
    print(f"Pad life: {sm.Physics.pad_life}")

    print("Graphics:")
    print(f"Strategy tyre set: {sm.Graphics.penalty.name}")

    print("Static: ")
    print(f"Max RPM: {sm.Static.max_rpm}")

    flag=sm.Graphics.flag

    print(flag.value)

def accClose():
    sm.close()