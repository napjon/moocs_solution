# ----------
# User Instructions:
#
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal.
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid2 = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]


grid = [[0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------


def compute_value():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    #This function will keep running if there's "change" inside the code
    while change:
        change = False#default to false
        for x in range(len(grid)):#for every i and j, not very efficient,
            for y in range(len(grid[0])):#But certainly get the job done
                if goal[0] == x and goal[1] == y:#Check if the goal is same as x,y coordinate
                    if value[x][y] > 0:#check if it's greater than zero
                        value[x][y] = 0#If it does, set it to zero
                        change = True
                elif grid[x][y] == 0:#else not goal and the grid coordinate is zero
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2< len(grid[0]):#if it's legitimate state, that is inside the grid
                            v2 = value[x2][y2] + cost_step #make a value from neighbour + cost_step
                            if v2 < value[x][y]:#if neighbours value is smaller than its value
                                change = True#change it
                                value[x][y] = v2#change the value to its neighbour value

    for i in range(len(value)):
        print value[i]

    return value #make sure your function returns a grid of values as demonstrated in the previous video.


compute_value()
