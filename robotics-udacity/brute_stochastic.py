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


grid  = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]


grid1 = [[0,0,0],
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

def stochastic_brute():
	#value  = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    #policy = [[' '  for row in range(len(grid[0]))] for col in range(len(grid))]


    #valuel = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    #valuer = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    #valueu = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    #valueb = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]

    big_value = [[[1000 for row in range(len(grid[0]))] for col in range(len(grid))] for dimension in range(len(delta))]
    
    for orientaion in range(len(delta)):
    	for x in range(len(big_value[0])):
    		for y in range(len(big_value[0][0])):
    			x2 = x + delta[orientaion][0]
    			y2 = y + delta[orientaion][1]

    			if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
    				#valuel[x][y] = value[x][y]
    				big_value[orientaion][x][y] = big_value[orientaion][x2][y2]
    			else:
    				#valuel[x][y] = collision_cost
    				big_value[orientaion][x][y] = collision_cost

    for orientaion in range(len(delta)):
    	for x in range(len(big_value[0])):
    		for y in range(len(big_value[0][0])):
    			print big_value[orientaion][x]

    return

stochastic_brute()

