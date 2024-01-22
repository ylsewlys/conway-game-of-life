<!--
    Async Learning Task: Cellular Automata
    Name: Wesly Samson
    Section: S11
-->
# John Conway's Game of Life in Python

The implemented code represents John Conway's Game of Life cellular automata in a simple 25x47 two dimensional array using Python and its TKinter GUI library. This is only used for simulation purposes and serves as a partial fullfilment for a major elective subject in DLSU titled "Complex Systems".

## How to Use

- Run the program (GameOfLife.py) by opening the terminal and running the command "python GameOfLife.py". This may differ depending on your operating system or the current directory of your running terminal. Alternatively, you can use any IDEs with integrated compilers (such as Visual Studio Code) and simply run the code.
- Once the program has loaded, you can click on the cells or boxes inside the 2D array to start adding/removing cells and initialize the starting state of the game.
- Once finished, click the start button to initiate the simulation. Note that once the simulation has started, you cannot edit the current array until you stop the simulation.
- Click the ">" button to go to the next state of the simulation and increment the time frame.
- Click the stop button to reset and restart the game.
- Click exit to quit the program.

## Possible TKinter GUI Elements Conflict with Different Operating Systems
When the program runs on a different operating system, there is a possibility of TKinter GUI elements not showing up or working properly despite having no issues on another operating system such as Windows. For instance, the border of each cells in the array show up properly on Windows; however, they don't show up at all on Mac. The visuals and positioning of the buttons may also differ, which may lead to inconsistent misclicks. Since this program was made on a Windows x64 operating system, I did not have the chance to fix the issues of the GUI elements on another operating system since I only have a Windows device available for use.
