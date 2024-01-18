from tkinter import *
from tkinter import colorchooser


stateArray = [[0] * 47 for _ in range(25)] # 2D Cell Array

timeFrame = 0 # time frame; default = 0

shapes = [] # 2D Array for shape labels


isSimulationStarted = True  # Status on whether the 2D CA Game of Life simulation has started or not


ROW = 25
COL = 47


# Functions

def handleState(event):
    shape = event.widget

    info = shape.grid_info()
    row, col = info['row'], info['column']
    

    if(stateArray[row][col] == 0):
        stateArray[row][col] = 1
        shape.configure(bg='#ffffff')
    elif(stateArray[row][col] == 1):
        stateArray[row][col] = 0
        shape.configure(bg='#111111')

    print(f"Clicked shape at row={row}, column={col}. Value: " + str(stateArray[row][col]))


def updateSimulationScreen():
    for row in range(ROW):
        for col in range(COL):
            if(stateArray[row][col] == 1):
                shapes[row][col].configure(bg='#ffffff')
            else:
                shapes[row][col].configure(bg='#111111')


def isCellOnEdge(row, col):
    if(row == 0 or row == ROW - 1 or col == 0 or col == COL - 1):
        return True
    else:
        return False

def incrementTimeFrame():
    global timeFrame
    timeFrame = timeFrame + 1
    timeFrameLabelVariable.set(timeFrame)



def toggleStopButton():
    global isSimulationStarted
    global stateArray

    if(isSimulationStarted):
        stopButton.config(state=NORMAL)
        stateArray = [[0] * 47 for _ in range(25)]
        isSimulationStarted = False
        updateSimulationScreen()
    else:
        stopButton.config(state=DISABLED)




# GUI
mainWindow = Tk()

# Initialize Dimensions and Title
mainWindow.geometry("800x800")
mainWindow.title("John Conway's Game of Life")

# Initialize Menu Window Configuration
icon = PhotoImage(file='CAlogo.png')
mainWindow.iconphoto(True, icon)
mainWindow.resizable(False, False)
mainWindow.config(
    background="#111111"
)

# Initialize time frame label
timeFrameLabelVariable = IntVar()
timeFrameLabelVariable.set(timeFrame)

# Create title
titleLabel = Label(mainWindow, 
              text="Game of Life", 
              font=('Cascadia Code Regular', 32),
              fg='#ffffff', 
              bg='#111111')
titleLabel.pack()

# Create Screen
screenFrame = Frame(mainWindow, height=575, width=705)
screenFrame.grid_propagate(False)
screenFrame.pack()

for row in range(ROW):
    row_shapes = []
    for col in range(COL):
        if(stateArray[row][col] == 0):
            shape = Label(screenFrame, bg='#111111', width=1, height=1, highlightthickness=1, highlightcolor='#ffffff', highlightbackground='#ffffff')
        else:
            shape = Label(screenFrame, bg='#ffffff', width=1, height=1, highlightthickness=1, highlightcolor='#ffffff', highlightbackground='#ffffff')

        shape.bind("<Button-1>", handleState)
        shape.grid(row=row, column=col)
        row_shapes.append(shape)

    shapes.append(row_shapes)



navFrame = Frame(mainWindow, bg='#111111')
navFrame.place(relx=0.5, anchor=CENTER, y=700)


startButton = Button(navFrame,
                     text="Start",
                     font=('Cascadia Code SemiLight', 18),
                     fg='#ffffff',
                     bg='#111111',
                    activeforeground='#ffffff',
                    activebackground='#3c3c3c',
                    padx=25)

startButton.grid(row=0, column=0, padx=(0, 10))

stopButton = Button(navFrame,
                     text="Stop",
                     font=('Cascadia Code SemiLight', 18),
                     fg='#ffffff',
                     bg='#111111',
                    activeforeground='#ffffff',
                    activebackground='#3c3c3c',
                    padx=25,
                    command=toggleStopButton,
                    state = NORMAL if isSimulationStarted else DISABLED)

stopButton.grid(row=0, column=1, padx=(10, 10))

exitButton = Button(navFrame,
                text='Exit',
                command=quit,
                font=('Cascadia Code SemiLight', 18),
                fg='#ffffff',
                bg='#111111',
                activeforeground='#ff5252',
                activebackground='#3c3c3c',
                padx=25)
exitButton.grid(row=0, column=2, padx=(10, 0))

incTimeFrameButton = Button(navFrame,
                text='>',
                font=('Cascadia Code SemiLight', 18),
                fg='#ffffff',
                bg='#111111',
                activeforeground='#ffffff',
                activebackground='#3c3c3c',
                padx=10,
                command=incrementTimeFrame)
incTimeFrameButton.grid(row=0, column=3, padx=(50, 10))


timeFrameLabel = Label(navFrame, 
              textvariable=timeFrameLabelVariable, 
              font=('Cascadia Code Regular', 18),
              fg='#ffffff', 
              bg='#111111')
timeFrameLabel.grid(row=0, column=4, padx=(10, 40))

mainWindow.mainloop()