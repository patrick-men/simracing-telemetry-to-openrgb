from tkinter import *
import sys
import subprocess
from LMU_telemetry import *
from ACC_telemetry import *
import threading # required to avoid tkinter GUI from hanging
from TelemetryFunctions import OpenRGBConfigBackup as backupConfig


#### FUNCTION DEFINITIONS ####

game = ""

# action when LMU button is clicked
def clickedACC():

    lbl.configure(text="Telemetry is being read for ACC! Enjoy your ride")

    # make buttons disappear, and center text
    btnACC.destroy()
    btnLMU.destroy()
    lbl.pack(expand=True)

    # func has to be ran in thread to avoid the tkinter GUI from hanging - daemon=true to ensure it stops when the program does
    threading.Thread(target=accTelemetry, daemon=True).start()

# action when LMU button is clicked
def clickedLMU():

    lbl.configure(text="Telemetry is being read for LMU! Enjoy your ride")

    # make buttons disappear, and center text
    btnACC.destroy()
    btnLMU.destroy()
    lbl.pack(expand=True)

    # func has to be ran in thread to avoid the tkinter GUI from hanging - daemon=true to ensure it stops when the program does
    threading.Thread(target=lmuTelemetry, daemon=True).start()

# restart button that restarts the entire GUI, and stops the current telemetry reading
def restart():
    root.destroy()
    python = sys.executable
    subprocess.Popen([python, __file__])

def main():
    # run profile backup whenever the program is ran
    backupConfig()

    # create root window
    global root
    root = Tk()

    # root window title and dimensions
    root.title("Telemetry to OpenRGB")
    root.geometry('450x150')  # Adjusted height for spacing

    # configure grid to center content
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # add label
    global lbl
    lbl = Label(root, text="Pick the game you want to read telemetry from:", font=("Arial", 12))
    lbl.grid(column=0, row=0, columnspan=2, pady=10)

    # add backup information label
    backupLabel = Label(
        root,
        text="If you don't have a profile of your current OpenRGB \nsettings saved, one's created automatically",
        font=("Arial", 7),
        justify="left",
        anchor="w"
    )
    backupLabel.place(x=5, rely=1.0, anchor='sw')

    # buttons
    global btnACC
    global btnLMU
    global btnRestart

    btnACC = Button(root, text="ACC", fg="white", bg="red", width=10, command=clickedACC)
    btnACC.grid(column=0, row=1, pady=10)

    btnLMU = Button(root, text="LMU", fg="white", bg="blue", width=10, command=clickedLMU)
    btnLMU.grid(column=1, row=1, pady=10)

    btnRestart = Button(root, text="⟳", font=("Arial", 12), command=restart)
    btnRestart.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    # run the GUI
    root.mainloop()

#### MAIN EXECUTION ####

main()