# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def val_check_two(mat):
    
    final_val = 0
    
    for i in range(1,len(mat)):
            
            bar = mat[i]
#            print("%%%%%%%%%%%%%%%%")
#            print(bar)
#            print("%%%%%%%%%%%%%%%%%%%%%")
#            print("---------------------")
            stack_index = list()
            
            
            index = 0
            temp = 0
            
            while index < len(bar):
                
                if(len(stack_index) == 0) or bar[stack_index[-1]] <= bar[index]:
                    stack_index.append(index)
                    index+=1
                
                else:
                    
                    last = stack_index.pop()
                    
                    temp = ( bar[last] * ((index - stack_index[-1] -1) if stack_index else index ))
                    final_val = max(temp,final_val)
                
                
                    
            while(len(stack_index)>0):
                
                last = stack_index.pop()
                temp = (bar[last]* ((index - stack_index[-1] -1) if stack_index else index))
                final_val = max(temp,final_val)
            
            
    
    return final_val



        
def val_check(matrix):
    
    temp_val = 0
    val = 0
    
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)):
            if(matrix[i][j]>1):
                temp.append(matrix[i][j])
                if(len(temp)>=2):
                    temp_val = len(temp) * min(temp)
                        #print("temp_val is")
                        #print(temp_val)
                    if(temp_val > val):
                        val = temp_val
                    
            
            elif(matrix[i][j] < 2):
                while(len(temp)>0):
                    #print("inside")
                    
                    temp.reverse()
                    temp.pop()
                    temp.reverse()
                    
                    if(len(temp)>=2):
                        temp_val = len(temp) * min(temp)
                        #print("temp_val is")
                        #print(temp_val)
                        if(temp_val > val):
                            val = temp_val
                    
        #here we compute the value of the min
        
        #print("outside of the temp")
        
        #print(temp)
        #print(val)
        
        while(len(temp) > 0):
            
            temp.reverse()
            temp.pop()
            temp.reverse()
            
            #print(temp)
            
            if(len(temp)>=2):
                temp_val = len(temp) * min(temp)
                
                if(temp_val > val):
                    val = temp_val
                    
    
    
    #val = 0
    
    
#    for i in range(len(matrix)):
#        
#        if(i > 0):
#            temp_val = compute(matrix[i])
#            if temp_val > val:
#                val = temp_val
        
    return val    


def size_of_largest_parallelogram():
    #pass
    
    Rect =     [ x[:] for x in grid]
    Parallel = [ x[:] for x in grid]
    Parallel_left = [ x[:] for x in grid]
    
    # first create the stack which we will check later 
    
    for i in range( len(grid)):
        for j in range(len(grid[i])):
            
            if( j == 0 and i>0):
                if i >0 and Rect[i][j] and Rect[i][j+1]:
                    Rect[i][j]+=Rect[i-1][j]
                    if j<9 :
                        Parallel[i][j]+=Parallel[i-1][j+1]
                    if j > 0:
                        Parallel_left[i][j]+=Parallel_left[i-1][j-1]
                        
            elif ( (j == len(grid[i]) -1) and i >0 and (Rect[i][j] and Rect[i][j-1] )):
                        Rect[i][j]+=Rect[i-1][j]
                        if j<9 :
                            Parallel[i][j]+=Parallel[i-1][j+1]
                        if j > 0:
                            Parallel_left[i][j]+=Parallel_left[i-1][j-1]
                
                
            elif ( i>0 and j>0 and j< (len(grid[i]) - 1) and ( ( Rect[i][j] and Rect[i][j-1]) or (Rect[i][j] and Rect[i][j+1])) ):
                Rect[i][j]+=Rect[i-1][j]
                if j<9 :
                    Parallel[i][j]+=Parallel[i-1][j+1]
                if j > 0:
                    Parallel_left[i][j]+=Parallel_left[i-1][j-1]
                    
                    
     
    print(Rect)
    print(Parallel)
    #print(Parallel_left)
    #Now we will have to check for the created stacks
    
    # first checking for the rect stack
    Rect_val = 0
    Parallel_val = 0
    Parallel_left_val = 0
    final_val = 0
    
    #the below function call will check for the rectangle's value
    Rect_val = val_check_two(Rect)
    print(Rect_val)
    Parallel_val = val_check_two(Parallel)
    print(Parallel_val)
    
    
    Parallel_left_val = val_check_two(Parallel_left)
    print(Parallel_left_val)
    
    final_val = max(Rect_val,Parallel_val,Parallel_left_val)
    
    return final_val;
        
    
    #Now check for the existence of parallelograms if any
    
  
    # REPLACE PASS ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS


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
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')
