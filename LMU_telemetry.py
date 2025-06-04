from sharedMemoryAPI import SimInfoAPI  # Replace 'your_module' with your filename or package

def main():
    sim = SimInfoAPI()

    if sim.isRF2running():
        print("rFactor 2 is running")
        print(sim.versionCheckMsg)

        if sim.isSharedMemoryAvailable():
            print("Shared memory is available")

            # Get player info
            player_name = sim.driverName()
            print("Player:", player_name)

            # Get telemetry info for player
            telemetry = sim.playersVehicleTelemetry()
            print("Gear:", telemetry.mGear)
            print("Clutch:", telemetry.mUnfilteredClutch)
            print("RPM:", telemetry.mEngineRPM)

            # Get scoring info
            scoring = sim.playersVehicleScoring()
            print("Vehicle Name:", scoring.mVehicleName)

            # Check if track loaded
            if sim.isTrackLoaded():
                print("Track is loaded")

    else:
        print("rFactor 2 is not running")

if __name__ == "__main__":
    main()
