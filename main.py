import subprocess
from tkinter import *
import TelemetryFunctions as telemetry
import sys
import subprocess

#TODO: Button click should make live changes of the lighting

game = ""

# Action when LMU button is clicked
def clickedACC():

    lbl.configure(text="Telemetry is being read for ACC! Enjoy your ride")

    # make buttons disappear, and center text
    btnACC.destroy()
    btnLMU.destroy()
    lbl.pack(expand=True)

    global game
    game = "ACC"

    telemetry.colortest(game)

# Action when LMU button is clicked
def clickedLMU():

    lbl.configure(text="Telemetry is being read for LMU! Enjoy your ride")

    # make buttons disappear, and center text
    btnACC.destroy()
    btnLMU.destroy()
    lbl.pack(expand=True)

    global game
    game = "LMU"

    telemetry.colortest(game)

# Restart button that restarts the entire GUI, and stops the current telemetry reading
def restart():
    root.destroy()
    python = sys.executable
    subprocess.Popen([python, __file__])

def main():

    # Create root window
    global root
    root = Tk()

    # Root window title and dimensions
    root.title("Telemetry to OpenRGB")
    root.geometry('450x120')  # Adjusted height for spacing

    # Configure grid to center content
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # Add label
    global lbl
    lbl = Label(root, text="Pick the game you want to read telemetry from:", font=("Arial", 12))
    lbl.grid(column=0, row=0, columnspan=2, pady=10)


    # Need to change things around for this to work:
    # def clickedReset():
    #
    #     btnACC.configure(state="active")
    #     btnLMU.configure(state="active")
    #
    #     lbl.configure(text="Telemetry is no longer being read")

    # Buttons
    global btnACC
    global btnLMU
    global btnRestart

    btnACC = Button(root, text="ACC", fg="white", bg="red", width=10, command=clickedACC)
    btnACC.grid(column=0, row=1, pady=10)

    btnLMU = Button(root, text="LMU", fg="white", bg="blue", width=10, command=clickedLMU)
    btnLMU.grid(column=1, row=1, pady=10)

    btnRestart = Button(root, text="⟳", font=("Arial", 12), command=restart)
    btnRestart.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    # Run the application
    root.mainloop()



main()