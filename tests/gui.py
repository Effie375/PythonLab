import PySimpleGUI as sg

sg.theme("Black")  # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text("Enter the frist path"),sg.InputText()],
            [sg.Text("Enter the second path"), sg.InputText()],
            [sg.Button("Save"), sg.Button("Plot")] ]

# Create the Window
window = sg.Window('CFS', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Save" or event == "Plot": # if user closes window or clicks cancel
        break
    print("Please enter a path.", values[0])

window.close()
