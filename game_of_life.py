import sys, argparse
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation


ON = 255
OFF = 0
vals = [ON, OFF]


def randomGrid(N):
    ''' returns a grid of NxN random values'''
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def addGlider(i, j, grid):
    """
    i : rows
    j : columns
    grid : numpy N*N 2D array 
    This function adds a Glider pattern with top left cell 
    at (i, j) 
    """
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider


def update(frameNum, img, grid, N):
    # copying grid as 8 neighbours required for calculation
    # it's doneline by line for every adjescent neighbour
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # 8 neighbour sum using toroidal boundary condition
            # x and y warp around forming a toroidal surface instead of a plain
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                        grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                        grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                        grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
    
            # Conway's Rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


# main function
def main():
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation")
    
    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False) # for definig a custom grid size
    parser.add_argument('--save-file', dest='savefile', required=False) # file name for output video file
    parser.add_argument('--interval', dest='interval', required=False) # update interval for the animation 
    parser.add_argument('--glider', action='store_true', required=False) # to add the glider pattern as the initial input, if omitted the grid would be randomly populated
    parser.add_argument('--gosper', action='store_true', required=False) # to add the gosper pattern as the initial input
    
    args = parser.parse_args()

    # set grid size 
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)
        
    # animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)
    
    # grid 
    grid = np.array([])
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    else:
        # grid with random on/off, more off than on 
        grid = randomGrid(N)

    # animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation="nearest", cmap='gray') #Greys
    anim = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), 
                                   frames = 100,
                                   interval = updateInterval,
                                   save_count=50)
    
    # output file
    if args.savefile:
        print("Writing animation...")
        argFile = args.savefile
        writerV = animation.FFMpegWriter(fps=10)
        anim.save(argFile, writer= writerV)
        print(f"\nAnimation Saved Successfully as {argFile}!")
        return
        #anim.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()
    
# main
if __name__ == '__main__':
    main()