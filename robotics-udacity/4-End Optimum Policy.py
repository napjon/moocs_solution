# ----------
# User Instructions:
#
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
#
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------
dynam_list = []
#dynam_list = [path1,path2,path3.....]
initial_path = [0,[init]]
###Format of path 2.0########
repath = [0,[[4,3,0],[3,3,0],[2,3,0],[1,3,0],[0,3,-1],[0,4,0],[0,5,-1],[1,5,0],
             [2,5,-1],[2,4,0],[2,3,0],[2,2,0],[2,1,0],[2,0,0]]]
###########
#dynam_list.append(repath)

def call_recursive(path):
    [x,y,o] = path[1][-1]
    save = [[x,y,o]]
    #path[0] += cost[action.index(o)]
    #count= path[0] + cost[action.index(o)]
    if [x,y] == goal:
        path[0] -= cost[o]
        return path
    else:

        for i in range(len(action)):
            e = forward[o]
            x2 = x+e[0]
            y2 = y+e[1]

            content = [x2,y2,action[i-o%abs(1)]]
            save.append(content)
            count= path[0] + cost[action.index(o)]
            if 0<=x2<len(grid) and 0<=y2<len(grid[0]):
	           if grid[x2][y2] == 0 and (save[1] not in path[1] or save[0] not in path[1]):
                    #path[1].append(content)

                    element =[count,path[1]+[content]]
                    #print element
                    dynam_list.append(call_recursive(element))
                    #print element


def optimum_policy2D():
    call_recursive(initial_path)
    list_f = []
    #print dynam_list
    for e in dynam_list:
        if e != None:
            #dynam_list.remove(e)
            list_f.append(e)
        #else:
            #print e
    #return
    #dynam_list.sort()
    #path = dynam_list[0]
    list_f.sort()
    path = list_f[0]
    print list_f
    return
    policy2D = [['' for i in range(len(grid[0]))] for j in range(len(grid))]
    for n in range(len(path[1])):
        [i,j,o] = path[1][n]
        if [i,j] == goal:
            policy2D[i][j] = '*'
        else:
            policy2D[i][j] = action_name[action.index(o)]

    for i in range(len(policy2D)):
        print policy2D[i]
    print path[0]
    return policy2D # Make sure your function returns the expected grid.

optimum_policy2D()







###Format of path 1.0#######
#repath = [0,[[4,3],[3,3],[2,3],[1,3],[0,3],[0,4],[0,5],[1,5],[2,5],
#             [2,4],[2,3],[2,2],[2,1],[2,0]],
#            [['#'],['#'],['#'],['#'],['R'],['#'],['R'],['#'],['R'],
#             ['#'],['#'],['#'],['#'],['*']]
#            ]
###########################
###Optimum_Policy 1.0######
function = """
def optimum_policy2D():
    dynam_list.sort()
    path = dynam_list[0]
    policy2D = [['' for i in range(len(grid[0]))] for j in range(len(grid))]
    for n in range(len(path[1])):
        [i,j] = path[1][n]
        [policy2D[i][j]] = path[2][n]

    for i in range(len(policy2D)):
        print policy2D[i]
    return policy2D # Make sure your function returns the expected grid.
            """