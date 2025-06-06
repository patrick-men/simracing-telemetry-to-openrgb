from tkinter import *
import TelemetryFunctions as tf

#TODO: Button click should make live changes of the lighting

game = ""

def main():

    # Create root window
    root = Tk()

    # Root window title and dimensions
    root.title("Telemetry to OpenRGB")
    root.geometry('450x120')  # Adjusted height for spacing

    # Configure grid to center content
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # Add label
    lbl = Label(root, text="Pick the game you want to read telemetry from:", font=("Arial", 12))
    lbl.grid(column=0, row=0, columnspan=2, pady=10)

    # Functions for button clicks
    def clickedACC():
        global game

        lbl.configure(text="Telemetry is being read for ACC")
        game = "ACC"

        tf.colortest()


    def clickedLMU():
        global game

        lbl.configure(text="Telemetry is being read for LMU")
        game = "LMU"


    # Buttons
    btnACC = Button(root, text="ACC", fg="white", bg="red", width=10, command=clickedACC)
    btnACC.grid(column=0, row=1, pady=10)

    btnLMU = Button(root, text="LMU", fg="white", bg="blue", width=10, command=clickedLMU)
    btnLMU.grid(column=1, row=1, pady=10)

    # Run the application
    root.mainloop()



main()