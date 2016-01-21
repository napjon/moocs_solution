# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. NOTE: the 'v' should be
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    expands = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    expanded = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    n = -1
    open = [[g, x, y]]
    expanded[x][y] = n
    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand


    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            n+=1
            expanded[x][y] = n

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i #not x,y as x,y because it searching,
                            #x2,y2 is more spesific
                            #i to remember what type of action the delta has to get to this coordinate

    x = goal[0]
    y = goal[1]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    policy[x][y] = '*'
    while x!= init[0] or y!= init[1]:#inverse to start coordinate
        x2 = x - delta[action[x][y]][0]#action[x][y] as i to delta[i][0] and delta[i][1],
        y2 = y - delta[action[x][y]][1]#we infer x2,y2 by substracting x,y with type of action
        policy[x2][y2] = delta_name[action[x][y]]#assign the character to from delta_name[i]
        x = x2#change it back to (x,y)
        y = y2
    for i in range(len(expand)):
        print policy[i]

    return # make sure you return the shortest path.

'''

    save = [goal[0],goal[1],999]
    expand[save[0]][save[1]] = '*'
    founded = False
    close = []
    #while save[0] != init[0] and save[1] != init[1]:
    while not founded:
        if save[0] == init[0] and save[1] == init[1]:
            founded = True
        else:
            for i in range(len(delta)):
                print (save[0],save[1])
                x2 = save[0] + delta[i][0]
                y2 = save[1] + delta[i][1]
                #print (x2,y2)
                if 0<=x2<len(grid) and 0<=y2<len(grid[0]) and expanded[x2][y2] != -1:
                    #print (x2,y2)
                    if expanded[x2][y2] < save[2] and (x2,y2) not in close:
                        save = [x2,y2,expanded[x2][y2]]
                        close.append((x2,y2))
                        expand[save[0]][save[1]] = delta_name[(i+2)%len(delta_name)]
                        print save


    for i in range(len(expand)):
        print expand[i]
'''




search()
