# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.

def colour_shapes():
    #pass
    
    count_shapes = 2
    spikes = []
    
    res_list = []

## the following code snippet finds the postition of spikes.
    
    #first find the spikes in the matrix and store the co-ordinates in a list
    
    for i in range(0, len(grid)):
        for j in range(0,len(grid[i])):
            if ( grid[i][j] == 1 ):
                if( i==0 and j==0 ):
                    if((grid[i][j+1] == 0 and grid[i+1][j] == 1) or (grid[i][j+1] == 1 and grid[i+1][j] == 0) ):
                        spikes.append((i,j))
                elif( (i== 0 and (0 < j < (len(grid[i]) -1) ) ) ) :
                    if( (grid[i][j-1] == 0 and grid[i][j+1] == 1 and grid[i+1][j] == 0) or ( grid[i][j-1] == 0 and grid[i][j+1] == 0 and grid[i+1][j] ==1 ) or (grid[i][j-1] ==1 and grid[i][j+1] == 0 and grid[i+1][j] == 0 )):
                        spikes.append((i,j))
                elif( i==0 and  (j == (len(grid[i]) -1) ) ):
                    if ( (grid[i][j-1] == 0 and grid[i+1][j] == 1) or ( grid[i][j-1] == 1 and grid[i+1][j] == 0 ) ):
                        spikes.append((i,j))
                
                elif(  (0< i < len(grid) -1) and j==0  ) :
                    if ( (grid[i-1][j] == 0 and grid[i+1][j] == 1 and grid[i][j+1] == 0) or ( grid[i-1][j] == 1 and grid[i][j+1] == 0 and grid[i+1][j] ==0) or ( grid[i-1][j] == 0 and grid[i][j+1] == 1 and grid[i+1][j] == 0 ) ):
                        spikes.append( (i,j))
                        
                elif( i == ( len(grid) -1) and j == 0 ) :
                    if ( ( grid[i-1][j] == 1 and grid[i][j+1] == 0 ) or ( grid[i-1][j] == 0 and grid[i][j+1] == 1 ) ) :
                        spikes.append( (i,j))
                
                elif ( (i == len(grid) -1) and ( 0< j< (len (grid[i]) -1) ) ):
                    if( (grid[i][j-1] == 0 and grid[i-1][j] == 1 and grid[i][j+1] == 0) or ( grid[i][j-1] == 1 and grid[i-1][j] == 0 and grid[i][j+1] == 0) or (grid[i][j-1] == 0 and grid[i-1][j] == 0 and grid[i][j+1] == 1 )):
                        spikes.append((i,j))
                        
                elif( ( i== len(grid) -1) and j == ( len(grid[i]) -1) ) :
                    if (  (grid[i][j-1] == 0 and grid[i-1][j] == 1) or ( grid[i][j-1] == 1 and grid[i-1][j] == 0) ) :
                        spikes.append((i,j))
                
                elif(  ( 0< i < (len(grid) -1) and j == (len(grid[i]) -1  ) ) ):
                    if ( (grid[i][j-1] == 0  and grid[i-1][j] == 1 and grid[i+1][j] == 0) or ( ( grid[i][j-1] == 1 and grid[i-1][j] == 0 and grid[i+1][j] ==0)) or ( grid[i][j-1] == 0 and grid[i-1][j] == 0 and grid[i+1][j] == 1 ) ):
                        spikes.append((i,j))
                    
                else:
                    if( (grid[i][j-1] == 0 and grid[i-1][j] == 0 and grid[i][j+1] == 1 and grid[i+1][j] == 0 ) or ( grid[i][j-1] == 0 and grid[i-1][j] == 1 and grid[i][j+1] == 0 and grid[i+1][j] == 0) or (grid[i][j-1] == 1 and grid[i-1][j] == 0 and grid[i][j+1] ==0 and grid[i+1][j] ==0) or (grid[i][j-1] == 0 and grid[i-1][j] == 0 and grid[i][j+1] == 0 and grid[i+1][j] == 1 ) ):
                        spikes.append((i,j))
                    
## now printing the spikes
    #print(spikes)
    
## now using iteration to find the shapes
## did not use dfs since there was a corner case of disconnected graphs, the following appooach is much better
    
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            
            if(grid[i][j] == 1):
                edge_list = [(i,j)]
                
                while edge_list:
                    
                    current_x,current_y = edge_list.pop()
                    
                    up_x = current_x 
                    up_y = current_y - 1
                    
                    if( 0 <= up_x < len(grid) and 0 <= up_y < len(grid) and grid[up_x][up_y] == 1 ):
                        edge_list.append((up_x,up_y))
                        
                    
                    right_x = current_x + 1
                    right_y = current_y
                    
                    if( 0 <= right_x < len(grid) and 0 <= right_y < len(grid) and grid[right_x][right_y] == 1 ):
                        edge_list.append((right_x,right_y))
                    
                    down_x = current_x 
                    down_y = current_y + 1 
                    
                    if( 0 <= down_x < len(grid) and 0 <= down_y < len(grid) and grid[down_x][down_y] == 1 ):
                        edge_list.append((down_x,down_y))
                    
                    left_x = current_x -1
                    left_y = current_y 
                    
                    if( 0 <= left_x < len(grid) and 0 <= left_y < len(grid) and grid[left_x][left_y] == 1 ):
                        edge_list.append((left_x,left_y))
                    
                    
                    if( 0<= current_x < len(grid) and 0<= current_y < len(grid)) :
                        grid[current_x][current_y] = count_shapes
#                   
                    
                   
                count_shapes+=1   


    res_list.append(count_shapes)
    res_list.append(spikes)
#    
#    display_grid()
    
    print(res_list)

    return res_list    
        
        
        
    # Replace pass above with your code


def max_number_of_spikes(nb_of_shapes):
    #pass
    
    spike_list = nb_of_shapes.pop()
    number_of_shapes = nb_of_shapes.pop()
    
    count_list = {}
    
    count_list[1] = 0
    
    for i in range(2,number_of_shapes+1):
        count_list[i] = 0
    
    for (i,j) in spike_list:
        val = grid[i][j]
        count_list[val]+=1
    
    res = max(count_list.values())
    
    return res
    # Replace pass above with your code


# Possibly define other functions here    


try: 
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
