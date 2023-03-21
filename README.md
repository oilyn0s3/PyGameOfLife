# PyGameOfLife
A simple script for simulating Conway's Game of Life. It works by creating an N×N grid of cells and simulates the 
evolution of the system over time by applying the rules of Conway’s Game of Life. It then displays the state of the game at each time step 
and provides ways to save the output to a file and also set the initial condition of the system to either a random distribution or a predesigned pattern.

### How it works
The Game of Life is built on a grid of 9x9, every cell here has 8 neighbouring cells. The value of a given cell at a given instant 
of time depends on the state of its neighbors at the previous time step.
Conway’s Game of Life has four rules.
1. If a cell is ON and has fewer than two neighbors that are ON, it turns OFF.
2. If a cell is ON and has either two or three neighbors that are ON, it remains ON.
3. If a cell is ON and has more than three neighbors that are ON, it turns OFF.
4. If a cell is OFF and has exactly three neighbors that are ON, it turns ON.
