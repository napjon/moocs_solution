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

value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
policy =[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

value_cstep = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]

value3 = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]

def optimum_policy():
   # value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    #policy =[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value_cstep[x][y] > 0:
                       # value[x][y] = 0
                        value_cstep[x][y] = 0


                        change = True

                elif grid[x][y] == 0:
                    #save = 99
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value_cstep[x2][y2] + cost_step
                            #v2 = value[x2][y2] + cost_step

                            if v2 < value_cstep[x][y]:
                                change = True
                                #value[x][y] = v2
                                value_cstep[x][y] = v2


                                policy[x][y] = delta_name[a]
                                #save = value[x2][y2]

    policy[goal[0]][goal[1]] = '*'

    for i in range(len(value)):
        print value_cstep[i]
    for i in range(len(policy)):
        print policy[i]
    return policy # Make sure your function returns the expected grid.


def stochastic_value():
    #value  = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    #policy = [[' '  for row in range(len(grid[0]))] for col in range(len(grid))]
    optimum_policy()
    #value  = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    iter  = 0
    maxed = max([e for e in value_cstep[len(value_cstep)-1] if e != 1000])
    print "HI im maxed",maxed
    #test = 0
    while change:
        change = False
        #print iter
        #iter  = (iter+1)%3
        iter+=1
        for x in range (len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                 
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True
                        
                        policy[x][y] = '*'

                elif grid[x][y] == 0 and value_cstep[x][y] == iter:
                    #print 'log',iter
                    saved = 1000
                    for n in range(len(delta_name)):
                        if policy[x][y] == delta_name[n]:
                            saved = n

                    #for a in range(len(delta)):
                     #   x2 = x + delta[a][0]
                      #  y2 = y + delta[a][1]
                    polici = 1000
                    value[x][y] = 0
                    for i in range(len(action)):

                        #print "I got in"
                        #change =  True
                        o2  = (saved + action[i]) % 4
                        x2 = x + delta[o2][0]
                        y2 = y + delta[o2][1]
                        v2 = 0
                        #if o2 != saved:#Because it was done by optimum policy
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0 and value[x][y]!=1000:
                            v2 = value[x2][y2] * action_prob [i]
                            #value[x][y] = value[x2][y2] *
                            #print value[x2][y2]
                            if v2 < polici and v2!=0:
                                #print "policy should be change"
                                polici = v2
                                policy[x][y] = delta_name[o2]
                                
                        else:
                            v2 = collision_cost * action_prob[i]
                        #print action_prob[i],v2,(x,y),value[x][y],policy[x][y]


                        repeat[i] = v2
                        value[x][y] +=v2
                    #value[x][y] += value_cstep[x][y]
                    change = True
                    """
        if iter == maxed:
            x = len(value)/2
            y = len(value[0])/2
            v4 = 0

            for m in range(len(delta_name)):
                if policy[x][y] == delta_name[m]:
                    saved = m

            #print "hello2", (x,y),m, value[x][y]
            for q in range(len(action)):
                o2  = (saved + action[q]) % 4
                x2 = x + delta[o2][0]
                y2 = y + delta[o2][1]

                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                    v4+= value[x2][y2] * action_prob [i]
                else:
                    v4+= collision_cost * action_prob[i]
                v4+=value_cstep[x][y]

            if value[x][y] != v4:
                print iter
                iter = 0
                change = True
                """

    


    for l in range(len(value)):
        print value_cstep[l]                            

    for g in range(len(value)):
    	print value[g]

    for i in range(len(policy)):
    	print policy[i]



    return

stochastic_value()