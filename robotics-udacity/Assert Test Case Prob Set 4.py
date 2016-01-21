atc1 = [[0,0,0],
		[0,0,0]]

vatc1 = [[60.472, 37.193, 0.000],
		 [63.503, 44.770, 37.193]]

opatc1 = [['>', '>', '*'],
		  ['>', '^', '^']]



atc2 = [[94.041, 1000.000, 0.000],
		[86.082, 73.143, 44.286]]



  if 1<=x2<len(grid)-1 and 1<=y2<len(grid)-1 and grid[x2][y2] == 0:
    value[x][y] = value[x2][y2] * e
elif x2 == 0 or x2 == len(grid)-1 or y2 == 0 or y2 == len(grid[0])-1:
    value[x][y] = collision_cost * e
change = True