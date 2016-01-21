# -------------- # USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.


grid1  = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]


grid = [[0,0,0],
        [0,0,0]]

vatc1 = [[60.472, 37.193, 0.000],
         [63.503, 44.770, 37.193]]

opatc1 = [['>', '>', '*'],
          ['>', '^', '^']]



goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100
cost_step = 1
repeat = [0,0,0]


############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

action_prob = [failure_prob,success_prob,failure_prob]
action = [-1, 0, 1]

value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
policy =[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

value_cstep = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]

value3 = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]

#def optimum_policy():
def stochastic_value():
   # value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    #policy =[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                       # value[x][y] = 0
                        policy[x][y] = '*'
                        value[x][y] = 0


                        change = True

                elif grid[x][y] == 0:
                    #save = 99
                    for a in range(len(delta)):
                        v2 = cost_step
                        for i in range(-1, 2):
                            

                            a2 = (a+i)% len(delta)
                            x2 = x + delta[a2][0]
                            y2 = y + delta[a2][1]

                            if i == 0:
                                p2 = success_prob
                            else:
                                p2 = failure_prob

                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                #v2 = value_cstep[x2][y2] + cost_step
                                #v2 = value[x2][y2] + cost_step
                                v2 += p2 * value[x2][y2]
                            else:
                                v2 += p2 * collision_cost

                        if v2 < value[x][y]:
                            change = True
                            value[x][y] = v2
                            policy[x][y] = delta_name[a]
                    
    return value,policy # Make sure your function returns the expected grid.


print stochastic_value()
