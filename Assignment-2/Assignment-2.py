# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:41:19 2019

@author: Uttkarsh Sharma
"""


# COMP9021 19T3 - Rachid Hamadi
# Assignment 2 *** Due Sunday Week 10


# IMPORT ANY REQUIRED MODULE

import re


class MazeError(Exception):
    def __init__(self, message):
        self.message = message


class Maze:
    
    
    def wall_creation(self,matrix_map,wall_list):
            
        #temp_str = ""
        
        for i in range(1,len(matrix_map),2) :
            for j in range(1,len(matrix_map[0]),2) :
                if(matrix_map[i][j] == '1'):
                    matrix_map[i-1][j-1] = 'W'
                    matrix_map[i-1][j] = 'W'
                    matrix_map[i-1][j+1] = 'W'
                    
                    wall_list.append((i-1,j-1))
                    wall_list.append((i-1,j))
                    wall_list.append((i-1,j+1))
            
                if( matrix_map[i][j] == '2') :
                    matrix_map[i-1][j-1] = 'W'
                    matrix_map[i][j-1] = 'W'
                    matrix_map[i+1][j-1] = 'W'
                    
                    wall_list.append((i-1,j-1))
                    wall_list.append((i,j-1))
                    wall_list.append((i+1,j-1))
                    
                if(matrix_map[i][j] == '3'):
                
                #first for the top row
                    matrix_map[i-1][j-1] = 'W'
                    matrix_map[i-1][j] = 'W'
                    matrix_map[i-1][j+1] = 'W'
                    
                    wall_list.append((i-1,j-1))
                    wall_list.append((i-1,j))
                    wall_list.append((i-1,j+1))
                    
                #now for the straight row
                    matrix_map[i][j-1] = 'W'
                    matrix_map[i+1][j-1] = 'W'
                    
                    wall_list.append((i,j-1))
                    wall_list.append((i+1,j-1))
    
    
    #    for row in matrix_map:
    #        print('    ',*row)
    
    
    #inside_main
    ## first reading the file and then interpreting the data in a matrix    
    
    #gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid,matrix_map,directions)
    def analysis_loop(self,gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid,matrix_map,directions):
        
    ## outer iterative loop with branching to facilitate different condiditons
    
        for i in range(0,len(matrix_map)-1):
            for j in range(0,len(matrix_map[i])-1):
                
                # for the gates in the top row
                if ( i == 0 and 0 < j < ( len(matrix_map[i]) -2  ) and j%2==1):
                    if(( matrix_map[i][j] == 'p' or matrix_map[i][j] == 'D' ) and ( matrix_map[i][j-1] == 'W' or matrix_map[i][j-1] == 'p' ) and ( matrix_map[i][j+1] == 'W' or matrix_map[i][j+1] == 'p' ) ):
                        matrix_map[i][j] = 'G'
                        gates.append((i,j))
                        count_gates+=1
                
                # for the gates in the left column
                elif( j == 0 and 0 < i < ( len(matrix_map)-1 ) and i%2 == 1):
                    if( ( matrix_map[i][j] == 'p' or matrix_map[i][j] == 'D' ) and ( matrix_map[i-1][j] == 'W' or matrix_map[i-1][j] == 'p' ) and ( matrix_map[i+1][j] == 'W' or matrix_map[i+1][j] == 'p' ) ) :
                        matrix_map[i][j] = 'G'
                        gates.append((i,j))
                        count_gates+=1
                
                # for the gates in the bottom row
                
                elif( i == (len(matrix_map) -2) and 0< j < ( len(matrix_map[i]) -2) and j%2 == 1) :
                    if( ( matrix_map[i][j] == 'p' or matrix_map[i][j] == 'D') and (matrix_map[i][j-1] == 'W' or matrix_map[i][j-1] == 'p' ) and ( matrix_map[i][j+1] == 'W' or matrix_map[i][j+1] == 'p' )):
                        matrix_map[i][j] = 'G'
                        gates.append((i,j))
                        count_gates+=1
                
                # for the gates in the right column
                
                elif( j == (len(matrix_map[i]) -2) and 0 < i < (len(matrix_map) -1) and i%2 == 1) :
                    if( ( matrix_map[i][j] == 'p' or matrix_map[i][j] == 'D') and ( matrix_map[i-1][j] == 'W' or matrix_map[i-1][j] == 'p' ) and ( matrix_map[i+1][j] == 'W' or matrix_map[i+1][j] == 'p' )):
                        matrix_map[i][j] = 'G'
                        gates.append((i,j))
                        count_gates+=1
                
                
                
                # now checking for the inaccessible inner points
                # Note that this loop only checks for the closed boxes i.e. individual ones
                if ( i%2 == 1 and j%2==1 and matrix_map[i][j].isdigit() ):
                    if (matrix_map[i-1][j-1] == 'W' and matrix_map[i-1][j]=='W' and matrix_map[i-1][j+1]=='W' and matrix_map[i][j+1]=='W' and matrix_map[i+1][j+1]=='W' and matrix_map[i+1][j]=='W' and matrix_map[i+1][j-1]=='W' and matrix_map[i][j-1]=='W' ) :
                        matrix_map[i][j] = 'C'
                        closed.append((i,j))
                        closed_count+=1
                    
                    #now we will check for the Dead ends.
                    elif (matrix_map[i-1][j]=='W' and matrix_map[i-1][j+1]=='W' and matrix_map[i][j+1]=='W' and matrix_map[i+1][j+1]=='W' and matrix_map[i+1][j]=='W' and matrix_map[i+1][j-1]=='W' and matrix_map[i][j-1]=='W' ) :
                        matrix_map[i][j] = 'D'
                        dead_ends.append((i,j))
                    
                    
                    elif (matrix_map[i-1][j-1] == 'W' and matrix_map[i-1][j+1]=='W' and matrix_map[i][j+1]=='W' and matrix_map[i+1][j+1]=='W' and matrix_map[i+1][j]=='W' and matrix_map[i+1][j-1]=='W' and matrix_map[i][j-1]=='W' ) :
                        matrix_map[i][j] = 'D'
                        dead_ends.append((i,j))
                    
                    elif (matrix_map[i-1][j-1] == 'W' and matrix_map[i-1][j]=='W' and matrix_map[i][j+1]=='W' and matrix_map[i+1][j+1]=='W' and matrix_map[i+1][j]=='W' and matrix_map[i+1][j-1]=='W' and matrix_map[i][j-1]=='W' ) :
                        matrix_map[i][j] = 'D'
                        dead_ends.append((i,j))
                    
                    elif (matrix_map[i-1][j-1] == 'W' and matrix_map[i-1][j]=='W' and matrix_map[i-1][j+1]=='W' and matrix_map[i+1][j+1]=='W' and matrix_map[i+1][j]=='W' and matrix_map[i+1][j-1]=='W' and matrix_map[i][j-1]=='W' ) :
                        matrix_map[i][j] = 'D'
                        dead_ends.append((i,j))
                    
                    elif (matrix_map[i-1][j-1] == 'W' and matrix_map[i-1][j]=='W' and matrix_map[i-1][j+1]=='W' and matrix_map[i][j+1]=='W' and matrix_map[i+1][j]=='W' and matrix_map[i+1][j-1]=='W' and matrix_map[i][j-1]=='W' ) :
                        matrix_map[i][j] = 'D'
                        dead_ends.append((i,j))
                    
                    elif (matrix_map[i-1][j-1] == 'W' and matrix_map[i-1][j]=='W' and matrix_map[i-1][j+1]=='W' and matrix_map[i][j+1]=='W' and matrix_map[i+1][j+1]=='W' and matrix_map[i+1][j-1]=='W' and matrix_map[i][j-1]=='W' ) :
                        matrix_map[i][j] = 'D'
                        dead_ends.append((i,j))
                    
                    elif (matrix_map[i-1][j-1] == 'W' and matrix_map[i-1][j]=='W' and matrix_map[i-1][j+1]=='W' and matrix_map[i][j+1]=='W' and matrix_map[i+1][j+1]=='W' and matrix_map[i+1][j]=='W' and matrix_map[i][j-1]=='W' ) :
                        matrix_map[i][j] = 'D'
                        dead_ends.append((i,j))
                    
                    #the last condition to check for the Dead ends.
                    elif (matrix_map[i-1][j-1] == 'W' and matrix_map[i-1][j]=='W' and matrix_map[i-1][j+1]=='W' and matrix_map[i][j+1]=='W' and matrix_map[i+1][j+1]=='W' and matrix_map[i+1][j]=='W' and matrix_map[i+1][j-1]=='W') :
                        matrix_map[i][j] = 'D'
                        dead_ends.append((i,j))
                        
                
                #finding the sets of walls, and storing them in the variable sets of walls
                
                if(grid[i][j] == 'W'):
                    edge_list = [(i,j)]
                
                    while edge_list:
                        
                        current_x,current_y = edge_list.pop()
                        
                        up_x = current_x 
                        up_y = current_y - 1
                        
                        if( 0 <= up_x < len(grid) and 0 <= up_y < len(grid[0]) and grid[up_x][up_y] == 'W' ):
                            edge_list.append((up_x,up_y))
                            
                        
                        right_x = current_x + 1
                        right_y = current_y
                        
                        if( 0 <= right_x < len(grid) and 0 <= right_y < len(grid[0]) and grid[right_x][right_y] == 'W' ):
                            edge_list.append((right_x,right_y))
                        
                        down_x = current_x 
                        down_y = current_y + 1 
                        
                        if( 0 <= down_x < len(grid) and 0 <= down_y < len(grid[0]) and grid[down_x][down_y] == 'W' ):
                            edge_list.append((down_x,down_y))
                        
                        left_x = current_x -1
                        left_y = current_y 
                        
                        if( 0 <= left_x < len(grid) and 0 <= left_y < len(grid[0]) and grid[left_x][left_y] == 'W' ):
                            edge_list.append((left_x,left_y))
                        
                        
                        if( 0<= current_x < len(grid) and 0<= current_y < len(grid[0])) :
                            grid[current_x][current_y] = count_walls+4
                    #variable counting sets of walls                   
                    count_walls+=1
                    
                
                if(matrix_map[i][j] == 'D'):
                        
                        dead_list = [(i,j)]
                    
                        while dead_list:
                            
                            current_x,current_y = dead_list.pop()
                            #matrix_map[current_x][current_y] = 'D'
                            grid[current_x][current_y] = 'D'
                            
                            #adding the dead end to the list
                            dead_ends.append((current_x,current_y))
                            
                            wall_temp = []
                            #wall_list = []
                            
                            for (direction_x, direction_y) in directions:
                                    next_x, next_y = direction_x + current_x, direction_y + current_y
                                    
                                    if 0 <= next_x < len(matrix_map)-1 and 0 <= next_y < len(matrix_map[0])-1:
                                        wall_temp.append(grid[next_x][next_y])
                            
                            wall_list = [temp for temp in wall_temp if type(temp) == int]
                            wall_list.sort()
                                
                            wall = wall_list.pop()
                            
                            #wall_list = 
                            
                            up_x = current_x 
                            up_y = current_y - 1
                            
                            right_x = current_x + 1
                            right_y = current_y
                            
                            down_x = current_x 
                            down_y = current_y + 1
                            
                            left_x = current_x -1
                            left_y = current_y 
                            
                            temp_val = []
                            
                            if( 0 <= up_x < len(matrix_map)-1 and 0 <= up_y < len(matrix_map[0])-1 and grid[up_x][up_y]!='D' and matrix_map[up_x][up_y]!='W' and matrix_map[up_x][up_y]!='Z' ) :
                                
                                #val = grid[up_x][up_y]
                                
                                for (direction_x, direction_y) in directions:
                                    next_x, next_y = direction_x + up_x, direction_y + up_y
                                    
                                    if 0 <= next_x < len(matrix_map)-1 and 0 <= next_y < len(matrix_map[0]):
                                        temp_val.append(grid[next_x][next_y])
                                
                                #temp = temp_val.pop()
                                #temp_val.append(temp)
                                
        #                        wall_list = [temp for temp in temp_val if type(temp) == int]
        #                        wall_list.sort()
        #                        
        #                        wall = wall_list.pop()
                                
                                ce = temp_val.count(wall)
                                d_count = temp_val.count('D')
                                
                                if(ce == 3 or  (ce == 2 and d_count == 1) or (ce == 1 and (d_count == 2 or d_count == 3))):
                                    dead_list.append((up_x,up_y))
                                        
                                #matrix_map[up_x][up_y] = 'D'
                                #matrix_map[current_x][current_y] = 'D'
                                
                                #list_dead.append((current_x,current_y))
                                
                                #list_dead.append((up_x,up_y))
                            temp_val = []
                            
                            if( 0 <= right_x < len(matrix_map) and 0 <= right_y < len(matrix_map[0]) and grid[right_x][right_y]!='D' and matrix_map[right_x][right_y] !='W' and matrix_map[right_x][right_y]!='Z' ):
                                
                                for (direction_x, direction_y) in directions:
                                    next_x, next_y = direction_x + right_x, direction_y + right_y
                                    
                                    if 0 <= next_x < len(matrix_map)-1 and 0 <= next_y < len(matrix_map[0]):
                                        temp_val.append(grid[next_x][next_y])
                                
                                #temp = temp_val.pop()
                                #temp_val.append(temp)
        #                        wall_list = [temp for temp in temp_val if type(temp) == int]
        #                        wall_list.sort()
        #                        
        #                        wall = wall_list.pop()
                                
                                ce = temp_val.count(wall)
                                d_count = temp_val.count('D')
                                
                                if(ce == 3 or  (ce == 2 and d_count == 1) or (ce == 1 and (d_count == 2 or d_count == 3))):
                                    dead_list.append((right_x,right_y))
                                #list_dead.append((current_x,current_y))
                                #list_dead.append((right_x,right_y))
                                
                            
                             
                            
                            if( 0 <= down_x < len(matrix_map) and 0 <= down_y < len(matrix_map[0]) and grid[down_x][down_y]!='D' and matrix_map[down_x][down_y] !='W' and matrix_map[down_x][down_y]!='Z' ):
                                
                                for (direction_x, direction_y) in directions:
                                    next_x, next_y = direction_x + down_x, direction_y + down_y
                                    
                                    if 0 <= next_x < len(matrix_map)-1 and 0 <= next_y < len(matrix_map[0]):
                                        temp_val.append(grid[next_x][next_y])
                                
                                #temp = temp_val.pop()
                                #temp_val.append(temp)
        #                        wall_list = [temp for temp in temp_val if type(temp) == int]
        #                        wall_list.sort()
        #                        
        #                        wall = wall_list.pop()
                                
                                ce = temp_val.count(wall)
                                d_count = temp_val.count('D')
                                
                                if(ce == 3 or  (ce == 2 and d_count == 1) or (ce == 1 and (d_count == 2 or d_count == 3))):
                                    dead_list.append((down_x,down_y))
                            
                            
                            if( 0 <= left_x < len(matrix_map) and 0 <= left_y < len(matrix_map[0]) and grid[left_x][left_y] and matrix_map[left_x][left_y] !='W' ):
                                
                                for (direction_x, direction_y) in directions:
                                    next_x, next_y = direction_x + left_x, direction_y + left_y
                                    
                                    if 0 <= next_x < len(matrix_map)-1 and 0 <= next_y < len(matrix_map[0]):
                                        temp_val.append(grid[next_x][next_y])
                                
                                #temp = temp_val.pop()
                                #temp_val.append(temp)
                                
        #                        wall_list = [temp for temp in temp_val if type(temp) == int]
        #                        wall_list.sort()
        #                        
        #                        wall = wall_list.pop()
                                
                                ce = temp_val.count(wall)
                                d_count = temp_val.count('D')
                                
                                if(ce == 3 or  (ce == 2 and d_count == 1) or (ce == 1 and (d_count == 2 or d_count == 3))):
                                    dead_list.append((left_x,left_y))
        
        
        
        #now the second itertion:
        
        for i in range(0,len(grid)-1):
            for j in range(0,len(grid[0])-1):
                
                wall_list = []
                wall_temp = []
                wall_ch = []
                #ce = 0
                
                if (grid[i][j]!='D' and matrix_map[i][j]!='W' and matrix_map[i][j]!='Z'):
                    
                    for (direction_x, direction_y) in directions:
                        next_x, next_y = direction_x + i, direction_y + j
                                    
                        if 0 <= next_x < len(matrix_map)-1 and 0 <= next_y < len(matrix_map[0])-1:
                            wall_temp.append(grid[next_x][next_y])
                    
                    if(len(wall_temp) > 0):
                        wall_list = [temp for temp in wall_temp if type(temp) == int]
                        wall_ch   = [temp for temp in wall_temp if type(temp) == str]
                        
                        wall_list.sort()
                        if(len(wall_list) > 0):
                            wall = wall_list.pop()
                            wall_list.append(wall)
                        
                            if(wall > 3):
                                ce = wall_list.count(wall)
                                d_count = wall_temp.count('D')
                        
                            if( (ce == 1 and d_count == 2) or (ce == 2 and d_count == 1) or d_count==3 ):
                                grid[i][j] = 'D'
                                dead_ends.append((i,j))
                        else:
                                
                            d_co = wall_ch.count('D')
                            if(d_co == 3 ):
                                    grid[i][j] = 'D'
                                    dead_ends.append((i,j))
                            
                    
                    
                    
        #print(wall_ch)
        #print(type(grid[23][13]))
        
        #print()
#        print(count_gates)
#        print(count_walls)
#        print(closed_count)
#        #print(count_visited)
#        print(count_dead)
#        #print(len(path_list))
#        print(dead_ends)
        
        return gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid

    
    def pillar(self,pillars,matrix_map,grid):
        for i in range(0,len(matrix_map)-1):
            for j in range(0,len(matrix_map[i])-1):
                if( i%2 == 0 and j%2 == 0 and matrix_map[i][j] == 'p'):
                    if (matrix_map[i-1][j-1] != 'W' and matrix_map[i-1][j]!='W' and matrix_map[i-1][j+1]!='W' and matrix_map[i][j+1]!='W' and matrix_map[i+1][j+1]!='W' and matrix_map[i+1][j]!='W' and matrix_map[i+1][j-1]!='W' and matrix_map[i][j-1]!='W' ) :
                        matrix_map[i][j] = 'Z'
                        grid[i][j] = 'Z'
                        pillars.append((i,j))
    
    
    def visited_loop(self,gates,count_visited,matrix_map_visited):
        
        #count_visited = 0
        
        for i,j in gates:
                    
                    #print((i,j))    
                    
                    #gates_visited.append((i,j))
                    
                    edge_list = [(i,j)]
                    
                    while len(edge_list)>0:
                        
                        current_x,current_y = edge_list.pop()
                        
                        up_x = current_x 
                        up_y = current_y - 1
                        
                        if( 0 <= up_x < len(matrix_map_visited)-1 and 0 <= up_y < len(matrix_map_visited[0])-1  and (matrix_map_visited[up_x][up_y]=='p' or matrix_map_visited[up_x][up_y]=='0' or matrix_map_visited[up_x][up_y] == '1' or matrix_map_visited[up_x][up_y] == '2' or matrix_map_visited[up_x][up_y] == '3' or matrix_map_visited[up_x][up_y] == 'D' or matrix_map_visited[up_x][up_y] == 'G' )):
                            if((up_x,up_y) in gates):
                                gates.remove((up_x,up_y))
                            edge_list.append((up_x,up_y))
                            
                        
                        right_x = current_x + 1
                        right_y = current_y
                        
                        if( 0 <= right_x < len(matrix_map_visited)-1 and 0 <= right_y < len(matrix_map_visited[0])-1  and (matrix_map_visited[right_x][right_y] == 'p' or matrix_map_visited[right_x][right_y] =='0' or matrix_map_visited[right_x][right_y] == '1' or matrix_map_visited[right_x][right_y] == '2' or matrix_map_visited[right_x][right_y]=='3' or matrix_map_visited[right_x][right_y]=='D' or matrix_map_visited[right_x][right_y]=='G' )):
                            if((right_x,right_y) in gates):
                                gates.remove((right_x,right_y))
                            edge_list.append((right_x,right_y))
    
                        
                        down_x = current_x 
                        down_y = current_y + 1 
                        
                        if( 0 <= down_x < len(matrix_map_visited)-1 and 0 <= down_y < len(matrix_map_visited[0])-1 and (matrix_map_visited[down_x][down_y] == 'p' or matrix_map_visited[down_x][down_y] =='0' or matrix_map_visited[down_x][down_y] =='1' or matrix_map_visited[down_x][down_y] =='2' or matrix_map_visited[down_x][down_y] =='3' or matrix_map_visited[down_x][down_y] == 'D' or matrix_map_visited[down_x][down_y] =='G' )):
                            if((down_x,down_y) in gates):
                                gates.remove((down_x,down_y))
                            edge_list.append((down_x,down_y))
                        
                        left_x = current_x -1
                        left_y = current_y 
                        
                        if( 0 <= left_x < len(matrix_map_visited)-1 and 0 <= left_y < len(matrix_map_visited[0])-1 and (matrix_map_visited[left_x][left_y] == 'p' or matrix_map_visited[left_x][left_y] =='0' or matrix_map_visited[left_x][left_y] =='1' or matrix_map_visited[left_x][left_y] =='2' or matrix_map_visited[left_x][left_y] =='3' or matrix_map_visited[left_x][left_y] =='D' or matrix_map_visited[left_x][left_y] =='G' )):
                            if((left_x,left_y) in gates):
                                gates.remove((left_x,left_y))
                            edge_list.append((left_x,left_y))
                        
                        
                        if( 0<= current_x < len(matrix_map_visited)-1 and 0<= current_y < len(matrix_map_visited[0])-1 and (matrix_map_visited[current_x][current_y]!='W') ) :
                            matrix_map_visited[current_x][current_y] = count_visited*(-1)
    #                   
                    count_visited+=1
                
        return count_visited
    
    
    
    
    def closed_call(self,closed_count,inaccessible,matrix_map,matrix_map_visited,dead_ends,grid):
        
        temp_count = 0
        
        for i in range(len(matrix_map)-1):
            for j in range(len(matrix_map[0])-1):
                if ( matrix_map_visited[i][j] == 'D' ):
                    inaccessible.append((i,j))
                    grid[i][j] = 'C'
                    
                    if((i,j) in dead_ends):
                        dead_ends.remove((i,j))
                
                    if( i%2 == 1 and j%2==1):
                        temp_count+=1
                        
                elif( type(matrix_map_visited[i][j]) == str):
                    if(matrix_map[i][j] !='C'):
                        grid[i][j] = 'C'
                        
                        if( i%2 == 1 and j%2==1):
                            temp_count+=1
    #    print("inie")                
    #    print(grid[31][17])        
        closed_count +=temp_count
        
        return closed_count
        
    
    def dead_call(self,count_dead,matrix_map_dead,matrix_map):
        
        for i in range(len(matrix_map)):
            for j in range(len(matrix_map[0])):
                
                ## this code path checks for the matrix dead-paths that are consecutive
                
                if(matrix_map_dead[i][j] == 'D'):
                        edge_list = [(i,j)]
                        
                        while edge_list:
                            
                            current_x,current_y = edge_list.pop()
                            up_x = current_x 
                            up_y = current_y - 1
                            
                            if( 0 <= up_x < len(matrix_map_dead) and 0 <= up_y < len(matrix_map_dead[0])  and (matrix_map_dead[up_x][up_y] == 'D') ):
                                edge_list.append((up_x,up_y))
                                
                            
                            right_x = current_x + 1
                            right_y = current_y
                            
                            if( 0 <= right_x < len(matrix_map_dead) and 0 <= right_y < len(matrix_map_dead[0]) and (matrix_map_dead[right_x][right_y] == 'D')):
                                edge_list.append((right_x,right_y))
        
                            
                            down_x = current_x 
                            down_y = current_y + 1 
                            
                            if( 0 <= down_x < len(matrix_map_dead) and 0 <= down_y < len(matrix_map_dead[0]) and (matrix_map_dead[down_x][down_y] == 'D')):
                                edge_list.append((down_x,down_y))
                            
                            left_x = current_x -1
                            left_y = current_y 
                            
                            if( 0 <= left_x < len(matrix_map_dead) and 0 <= left_y < len(matrix_map_dead[0]) and (matrix_map_dead[left_x][left_y] == 'D') ):
                                edge_list.append((left_x,left_y))
                            
                            
                            if( 0<= current_x < len(matrix_map_dead) and 0<= current_y < len(matrix_map_dead[0])) :
                                matrix_map_dead[current_x][current_y] = count_dead-99999999999999999999999999999999999
        #                   
                        count_dead+=1       
        
        return count_dead
    
    
    def path_call(self,gates_to_gates,matrix_map_visited,visited,rejected,path_list):
        
        temp_path = []
        
        for i,j in gates_to_gates :
            
            val = matrix_map_visited[i][j]
            path = []
            edge_list = []
            
            if( matrix_map_visited[i][j]!='D' and matrix_map_visited[i][j] not in visited):
                if(matrix_map_visited[i][j] not in rejected):
                    
                    edge_list.append((i,j))
                    path.append((i,j))
                    matrix_map_visited[i][j] = 'V'
                    
                    
                    while edge_list:
                        
                        current_x , current_y = edge_list.pop()
                        matrix_map_visited[current_x][current_y] = 'V'    
                        #now we will check for the path_count
                        path_count = 0
                        
                        
                        up_x = current_x 
                        up_y = current_y - 1
                        
                        if( 0 <= up_x < len(matrix_map_visited)-1 and 0 <= up_y < len(matrix_map_visited[0])-1  and matrix_map_visited[up_x][up_y] == val and matrix_map_visited[up_x][up_y]!='D' and matrix_map_visited[up_x][up_y]!='W' and matrix_map_visited[up_x][up_y]!='Z' ):
                            temp_path.append((up_x,up_y))
                            #matrix_map_visited[up_x][up_y] = 'V'
                            path_count+=1
                            
                            if(matrix_map_visited[up_x][up_y] == 'G'):
                                visited.append(matrix_map_visited[up_x][up_y])
                            
                        
                        right_x = current_x + 1
                        right_y = current_y
                        
                        if( 0 <= right_x < len(matrix_map_visited)-1 and 0 <= right_y < len(matrix_map_visited[0])-1  and matrix_map_visited[right_x][right_y] == val and matrix_map_visited[right_x][right_y]!='D' and matrix_map_visited[right_x][right_y]!='W' and matrix_map_visited[right_x][right_y]!='Z'):
                            #edge_list.append((right_x,right_y))
                            temp_path.append((right_x,right_y))
                            #matrix_map_visited[right_x][right_y] = 'V'
                            
                            path_count+=1
                            
                            if( matrix_map_visited[right_x][right_y] == 'G'):
                                visited.append(matrix_map_visited[right_x][right_y])
            
                        
                        down_x = current_x
                        down_y = current_y + 1 
                        
                        if( 0 <= down_x < len(matrix_map_visited)-1 and 0 <= down_y < len(matrix_map_visited[0])-1 and matrix_map_visited[down_x][down_y] == val and matrix_map_visited[down_x][down_y]!='D' and matrix_map_visited[down_x][down_y]!='W' and matrix_map_visited[down_x][down_y]!='Z'):
                            #edge_list.append((down_x,down_y))
                            temp_path.append((down_x,down_y))
                            #matrix_map_visited[down_x][down_y] = 'V'
                            
                            path_count+=1
                            
                            if(matrix_map_visited[down_x][down_y] == 'G'):
                                visited.append(matrix_map_visited[down_x,down_y])
                        
                        left_x = current_x -1
                        left_y = current_y
                        
                        if( 0 <= left_x < len(matrix_map_visited)-1 and 0 <= left_y < len(matrix_map_visited[0])-1 and matrix_map_visited[left_x][left_y] == val and matrix_map_visited[left_x][left_y]!='D' and matrix_map_visited[left_x][left_y]!='W' and matrix_map_visited[left_x][left_y]!='Z'):
                            #edge_list.append((left_x,left_y))
                            temp_path.append((left_x,left_y))
                            #matrix_map_visited[left_x][left_y] = 'V'
                            
                            path_count+=1
                            
                            
                            if(matrix_map_visited[left_x][left_y] == 'G'):
                                visited.append(matrix_map_visited[left_x,left_y])
                        
                        #now post checking the path_count
                        if(path_count == 1):    
                            
                            next_x,next_y = temp_path.pop()
                            edge_list.append((next_x,next_y))
                            path.append((next_x , next_y))
                            
                        else:
                            if(len(temp_path)>0):
                                next_x,next_y = temp_path.pop()
                                rejected.append(matrix_map_visited[next_x][next_y])
                                temp_path = []
                                path = []
                            break
                        
                    if(len(path)!= 0):
                        path_list.append(path)        
                        
    
    def vertical(self,temp_vertical):
        
        wall_vertical = []
        temp_ver_stack = []
        
        rejected =[]
        
        
        for i,j in temp_vertical:
                
                if (len(temp_ver_stack)>0):
                    top_i,top_j = temp_ver_stack.pop()
                    temp_ver_stack.append((top_i,top_j))
                        
                    if(top_j == j):
                        if(abs(i - top_i) == 1):
                            temp_ver_stack.append((i,j))
                        
                        else:
                            length = len(temp_ver_stack)
                            if(length > 1):
                                wall_vertical.append((temp_ver_stack[0]))
                                wall_vertical.append((temp_ver_stack[length-1]))
                    
                            temp_ver_stack = []
                            rejected.append((i,j))
                            
                        
                    else:
                        if(len(temp_ver_stack)>=2):
                            length = len(temp_ver_stack)
                            wall_vertical.append((temp_ver_stack[0]))
                            wall_vertical.append((temp_ver_stack[length-1]))
                        rejected.append((i,j))
                        temp_ver_stack = []
                else:
                    
                    if(len(rejected)>0):
                        rejected_i,rejected_j = rejected.pop()
                        
                        if(rejected_j == j):
                            if(abs(i - rejected_i) == 1):
                                temp_ver_stack.append((rejected_i,rejected_j))
                                temp_ver_stack.append((i,j))
                            else:
                                rejected.append((i,j))
                        
                        else:
                            rejected.append((i,j))
                        
                    else:
                        temp_ver_stack.append((i,j))
        
        if(len(temp_ver_stack)>=2):
            wall_vertical.append((temp_ver_stack[0]))
            wall_vertical.append((temp_ver_stack[len(temp_ver_stack)-1]))
            
        #print(wall_vertical)
        return wall_vertical


    def horizontal(self,temp_horizontal):
        
        wall_horizontal = []
        temp_hor_stack = []
        
        rejected =[]
        
        
        for i,j in temp_horizontal:
                
                if (len(temp_hor_stack)>0):
                    top_i,top_j = temp_hor_stack.pop()
                    temp_hor_stack.append((top_i,top_j))
                        
                    if(top_i == i):
                        if(abs(j - top_j) == 1):
                            temp_hor_stack.append((i,j))
                        
                        else:
                            length = len(temp_hor_stack)
                            if(length > 1):
                                wall_horizontal.append((temp_hor_stack[0]))
                                wall_horizontal.append((temp_hor_stack[length-1]))
                    
                            temp_hor_stack = []
                            rejected.append((i,j))
                            
                        
                    else:
                        if(len(temp_hor_stack)>=2):
                            length = len(temp_hor_stack)
                            wall_horizontal.append((temp_hor_stack[0]))
                            wall_horizontal.append((temp_hor_stack[length-1]))
                        rejected.append((i,j))
                        temp_hor_stack = []
                else:
                    
                    if(len(rejected)>0):
                        rejected_i,rejected_j = rejected.pop()
                        
                        if(rejected_i == i):
                            if(abs(j - rejected_j) == 1):
                                temp_hor_stack.append((rejected_i,rejected_j))
                                temp_hor_stack.append((i,j))
                            else:
                                rejected.append((i,j))
                        
                        else:
                            rejected.append((i,j))
                        
                    else:
                        temp_hor_stack.append((i,j))
        
        if(len(temp_hor_stack)>=2):
            wall_horizontal.append((temp_hor_stack[0]))
            wall_horizontal.append((temp_hor_stack[len(temp_hor_stack)-1]))
                
        #print(wall_horizontal)
        return wall_horizontal





    def display_file(self,wall_list,pillars,dead_ends,path_list,row,col,filename):
        
        #doing the task for the walls
        
        we = set(wall_list)
        
        horizontal_wall_list = list(we)
        
        horizontal_wall_list.sort(key=lambda x:(x[0],x[1]))
        
        hori = self.horizontal(horizontal_wall_list)
        
        temp_wal = [temp for temp in wall_list]
        
        we_v = set(temp_wal)
        
        vertical_wall_list = list(we_v)
        
        vertical_wall_list.sort(key=lambda x:(x[1],x[0]))
        
        veri = self.vertical(vertical_wall_list)
        
        final_horizontal = [(int(j/2),int(i/2)) for i,j in hori  ]
        final_vertical = [(int(j/2),int(i/2)) for i,j in veri]
        
        #here we will have the pillars
        #final_pillars = [(j/2,i/2) for i,j in pillars]
        
        
        #formatting the dead ends here
        
        de = []
        
        for i in range(0,len(dead_ends)):
            if( dead_ends[i][0]%2==1 and dead_ends[i][1]%2==1):
                de.append(dead_ends[i])
        #print("ded")
        #print(de)
        
        final_dead_ends = [ ((j/2),(i/2)) for i,j in de]
        
        
        ### now setting the data for the file
        start1 =   r"""\documentclass[10pt]{article}"""
        start2 = r"""\usepackage{tikz}"""
        start3 = r"""\usetikzlibrary{shapes.misc}"""
        start4 = r"""\usepackage[margin=0cm]{geometry}"""
        start5 = r"""\pagestyle{empty}"""
        start6 = r"""\tikzstyle{every node}=[cross out, draw, red]"""
        
        start7= r"""\begin{document}"""
        
        start8=r"""\vspace*{\fill}"""
        start9=r"""\begin{center}"""
        start10=r"""\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]"""
        
        string = "testing_disp_" + filename +".tex"
        
        with open(string,"w") as file:
            
            file.write(start1)
            file.write('\n')
            file.write(start2)
            file.write('\n')
            file.write(start3)
            file.write('\n')
            file.write(start4)
            file.write('\n')
            file.write(start5)
            file.write('\n')
            file.write(start6)
            file.write('\n')
            file.write('\n')
            file.write(start7)
            file.write('\n')
            file.write('\n')
            file.write(start8)
            file.write('\n')
            file.write(start9)
            file.write('\n')
            file.write(start10)
            file.write("\n")
            file.write("% Walls")
            
            string = '\draw'
            string_fill = r'\fill[green]'
            string_fill_1 = r'circle(0.2);'
            file.write("\n")
            
            #for the horizontal_walls
            for i in range(0,len(final_horizontal),2):
                
                first_x = final_horizontal[i][0]
                first_y = final_horizontal[i][1]
                
                second_x = final_horizontal[i+1][0]
                second_y = final_horizontal[i+1][1]
                
                res = "    " + string + ' ' + '(' + str(first_x) + ',' + str(first_y) + ')' + ' -- ' + '(' + str(second_x) + ',' + str(second_y) + ')' + ';'
                
                file.write(res)
                file.write("\n")
                
            #for the vertical walls
            
            for i  in range(0,len(final_vertical),2):
                first_x = final_vertical[i][0]
                first_y = final_vertical[i][1]
                
                second_x = final_vertical[i+1][0]
                second_y = final_vertical[i+1][1]
                
                res = "    " + string + ' ' + '(' + str(first_x) + ',' + str(first_y) + ')' + ' -- ' + '(' + str(second_x) + ',' + str(second_y) + ')' + ';'
            
                file.write(res)
                file.write("\n")
                
            
            #for the pillars
            pi = r"""% Pillars"""
            file.write(pi)
            file.write("\n")
            
            #we = set()
            final_pillars = [ (int(j/2),int(i/2)) for i,j in pillars ]  
            
            for i,j in final_pillars:
                res = "    " + string_fill + ' ' + '(' + str(i) + ',' + str(j) + ')' + ' ' + string_fill_1
                file.write(res)
                file.write("\n")
                
            #for the inner dead-ends
            string_inner = r"""% Inner points in accessible cul-de-sacs"""
            file.write(string_inner)
            file.write("\n")
            
            inner = r"""    \node at """
            inner_end = r""" {};"""
            
            #print(final_dead_ends)
            
            for i,j in final_dead_ends:
                res = inner + '(' + str(i) + ',' + str(j) + ')' + inner_end
                file.write(res)
                file.write("\n")
            
            
            #for the horizontal path_list
            path_list_horizontal = []
            
            for i in range(0,len(path_list)):
                temp_wall_list = []
                
                we = set(path_list[i])
                #print(we)
                temp_wall_list = list(we)
                #print(temp_wall_list)
                temp_wall_list.sort(key=lambda x:(x[0],x[1]))
                #print(temp_wall_list)
                temp_hori = self.horizontal(temp_wall_list)
                #print(temp_hori)
                for i in range(len(temp_hori)):
                    path_list_horizontal.append(temp_hori[i])
                #path_list_horizontal.append(temp_hori)
            
            #print(path_list_horizontal)
            #for the horizontal paths
            final_horizontal_paths_temp = [ ((j/2),(i/2)) for i,j in path_list_horizontal]
            #print(final_horizontal_paths)
            
            final_horizontal_paths = []
            
            for i in range(0,len(final_horizontal_paths_temp),2):
                first_x = final_horizontal_paths_temp[i][0]
                first_y = final_horizontal_paths_temp[i][1]
                
                second_x = final_horizontal_paths_temp[i+1][0]
                second_y = final_horizontal_paths_temp[i+1][1]
                
                
                if(first_x == 0 or first_x == 0.0):
                    first_x = -0.5
                if(second_x == col-1 or second_x == (col-1)*1.0):
                    second_x+=0.5
                
                final_horizontal_paths.append((first_x,first_y))
                final_horizontal_paths.append((second_x,second_y))
            
            final_hori_dict = {}
            
            for i in range(0,len(final_horizontal_paths),2):
                final_hori_dict[final_horizontal_paths[i]] = final_horizontal_paths[i+1]
            
            hori_keys = [*final_hori_dict.keys()]
            
            hori_keys.sort(key=lambda x:(x[1],x[0]))
            
#            print("$$$$$$$$$$$$$$$$$")
#            print(hori_keys)
#            print("$$$$$$$$$$$$$$$$$$")
            #final_horizontal_paths.sort(key=lambda x:(x[1],x[0]))
                
            pt = r"""% Entry-exit paths without intersections"""
            file.write(pt)
            file.write("\n")
            
            pen = r"""    \draw[dashed, yellow] """
    #        for i in range(0,len(final_horizontal_paths),2):
    #            
    #            first_x = final_horizontal_paths[i][0]
    #            first_y = final_horizontal_paths[i][1]
    #            
    #            second_x = final_horizontal_paths[i+1][0]
    #            second_y = final_horizontal_paths[i+1][1]
    #            
    #            res = pen + '(' + str(first_x) + ',' + str(first_y) + ')' + ' -- ' + '(' + str(second_x) + ',' + str(second_y) + ')' + ';'
    #            
    #            file.write(res)
    #            file.write("\n")
                
            for i in range(0,len(hori_keys)):
                
                first_x = hori_keys[i][0]
                first_y = hori_keys[i][1]
                
                second_x = final_hori_dict[hori_keys[i]][0]
                second_y = final_hori_dict[hori_keys[i]][1]
                
                res = pen + '(' + str(first_x) + ',' + str(first_y) + ')' + ' -- ' + '(' + str(second_x) + ',' + str(second_y) + ')' + ';'
                
                file.write(res)
                file.write("\n")
            
            ## for the vertical horizontal paths
            path_list_vertical = []
            
            for i in range(0,len(path_list)):
                temp_wall_list = []
                
                we = set(path_list[i])
                #print(we)
                temp_wall_list = list(we)
                #print(temp_wall_list)
                temp_wall_list.sort(key=lambda x:(x[1],x[0]))
                #print(temp_wall_list)
                temp_ver = self.vertical(temp_wall_list)
                #print(temp_hori)
                for i in range(len(temp_ver)):
                    path_list_vertical.append(temp_ver[i])
                #path_list_horizontal.append(temp_hori)
            
            #print(path_list_horizontal)
            #for the vertical paths
            final_vertical_paths_temp = [ ((j/2),(i/2)) for i,j in path_list_vertical]
            #print(final_vertical_paths_temp)
            
            final_vertical_paths = []
            
            #print("After")
            for i in range(0,len(final_vertical_paths_temp),2):
                first_x = final_vertical_paths_temp[i][0]
                first_y = final_vertical_paths_temp[i][1]
                
                second_x = final_vertical_paths_temp[i][0]
                second_y = final_vertical_paths_temp[i+1][1]
                
                if(first_y == 0 or first_y == 0.0):
                    first_y = -0.5
                if(second_y == row-1 or second_y == (row-1)*1.0):
                    second_y+=0.5
            
                final_vertical_paths.append((first_x,first_y)) 
                final_vertical_paths.append((second_x,second_y))
                
            #print(final_vertical_paths)
    #        pt = r"""% Entry-exit paths without intersections"""
    #        file.write(pt)
    #        file.write("\n")
            
            final_veri_dict = {}
            
            for i in range(0,len(final_vertical_paths),2):
                final_veri_dict[final_vertical_paths[i]] = final_vertical_paths[i+1]
            
            veri_keys = [*final_veri_dict.keys()]
            
            veri_keys.sort(key=lambda x:(x[0],x[1]))
            
            
            
            pen = r"""    \draw[dashed, yellow] """
    #        for i in range(0,len(final_vertical_paths),2):
    #            
    #            first_x = final_vertical_paths[i][0]
    #            first_y = final_vertical_paths[i][1]
    #            
    #            second_x = final_vertical_paths[i+1][0]
    #            second_y = final_vertical_paths[i+1][1]
    #            
    #            res = pen + '(' + str(first_x) + ',' + str(first_y) + ')' + ' -- ' + '(' + str(second_x) + ',' + str(second_y) + ')' + ';'
    #            
    #            file.write(res)
    #            file.write("\n")
            
            for i in range(0,len(veri_keys)):
                
                first_x = veri_keys[i][0]
                first_y = veri_keys[i][1]
                
                second_x = final_veri_dict[veri_keys[i]][0]
                second_y = final_veri_dict[veri_keys[i]][1]
                
                res = pen + '(' + str(first_x) + ',' + str(first_y) + ')' + ' -- ' + '(' + str(second_x) + ',' + str(second_y) + ')' + ';'
                
                file.write(res)
                file.write("\n")
            
            
            
            #end of the file
            
            end1=r"""\end{tikzpicture}"""
            end2=r"""\end{center}"""
            end3=r"""\vspace*{\fill}"""
            
            end4=r"""\end{document}"""
            
            file.write("\n")
            file.write(end1)
            file.write("\n")
            file.write(end2)
            file.write("\n")
            file.write(end3)
            file.write("\n")
            
            file.write("\n")
            file.write("\n")
            file.write(end4)
            
            
            
            file.close()


    
    ###init_calls ----
                        
    
    def start(self):
        #start = time.time()
        
        filename = self.file
        
        matrix = []
        tempStr = ""
        
        file = open(filename,'r')
        
        line = file.readline()
        
        while line:
            tempStr = line.strip()
            if(len(tempStr)>0):
                temp1 = ''.join(tempStr.split())
                matrix.append(temp1)
            line = file.readline()
            
        
        ## checking the validation of the matrix
        
        length = len(matrix)
        
        ## to check around the matrix
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
        
        
        expression = "[0-3]*"
        re.compile(expression)
        
        expression_two = "[0-1]*"
        re.compile(expression)
        
        prev_length = len(matrix[0])
        
        #first_check = 0
        first_check_length = len(matrix)
        first_check_col = len(matrix[0])
        
        curr_length = 0
        
        for i in range(0,length):
            check_one = bool(re.fullmatch(expression,matrix[i]))
            
            #checking that the matrix has only 0-3 values
            
            if(check_one == False):
                #print("boom_diggy---> Incorrect input")
                
                raise Exception("maze.MazeError: Incorrect input.")
                
            
            # now to check for the length
            curr_length = len(matrix[i])
            #print(curr_length)
            
            if((2>first_check_length or first_check_length>31) or ((2>first_check_col or first_check_col>41))):
                raise Exception("maze.MazeError: Incorrect input.")
            
            if(curr_length != prev_length ):
                #print(curr_length)
                #print("boom-boom--second-----> Incorrect input")
                #print("now")
                raise Exception("maze.MazeError: Incorrect input.")
                #print(prev_length)
            
            #now checking for last digit
            if ( matrix[i][curr_length -1] == '1' or matrix[i][curr_length - 1] == '3' ):
                #print("dhoom-dhoom ---> Input does not represent a maze")
                raise Exception("maze.MazeError: Input does not represent a maze.")
                
            if( i == length-1):
                check_two = bool(re.fullmatch(expression_two,matrix[i]))
                
                if (check_two == False):
                    #print("dhoom-boom ---> Input does not represent a maze")
                    raise Exception("maze.MazeError: Input does not represent a maze.")
#            print("SSS\n")    
#            print(curr_length)
#            print(prev_length)
#            print("$$$\n")
            prev_length = curr_length
        
        
        #creation of the matrix map
        matrix_map = [[ 'p' for j in range( (2*len(matrix[0])))] for i in range(2*len(matrix))]
        
        
        #counter_variables
        
        count_j = 0
        count_i = 0
        
        #cretion of the matrix_map
        ## now creating the matrix map for the maze
        
        for i in range(1,len(matrix_map),2) :
             #setting the value of count j equal to zero here
            
            count_j = 0
            for j in range(1,len(matrix_map[i]),2) :
                
                if ( count_j <= len(matrix[0]) and count_i<=len(matrix) ) :
                    matrix_map[i][j] = matrix[count_i][count_j]
                    count_j+=1
            count_i +=1
        
        wall_list = []
        
        ##  function creating the walls
        self.wall_creation(matrix_map,wall_list)
        #print(len(matrix_map))
        #the endpoints having list of gates
        gates = []
        
        #the counter for the gates
        count_gates = 0
        
        
        #the list for the walls
        walls = []
        
        #the counter for the walls
        count_walls = 0
        
        #the list for the closed 
        closed = []
        
        #the count for closed
        closed_count = 0
        
        #the list for dead count
        dead_ends = []
        
        #count of dead
        count_dead = 0
        
        
        
        ## used for checking the set of the walls and passed in the analysis_loop
        grid = [temp[:] for temp in matrix_map]
        
        # the call for the analysis_loop
        # this loop is identifying the walls, gates,counts etc.
        gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid = self.analysis_loop(gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid,matrix_map,directions)
        gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid
        
        matrix_map_dead =  [temp[:] for temp in matrix_map ]
        
        ## for the dead_ends
        list_dead = []
        
        
        
        #list for where the pillars are present
        pillars = []        
        
        ## for the identification of the pillars
        self.pillar(pillars,matrix_map,grid)        
        
        
        ### now checking the accessible areas for the maze 
        ##matrix_map_visited = [ temp[:] for temp in matrix_map]
        matrix_map_visited = [ temp[:] for temp in grid]
        
        #the list of the gates
        gates_to_gates = [temp for temp in gates]
        
        #visited count for the accessible areas
        count_visited = 0
        
        ##checking accessible areas of the maze
        count_visited = self.visited_loop(gates,count_visited,matrix_map_visited)
        
        
        # now finding the in-accessible paths and consecutive dead ends
        inaccessible = []
        
        #checking the inaccessible areas of the maze
        temp_count = self.closed_call(closed_count,inaccessible,matrix_map,matrix_map_visited,dead_ends,grid)
        closed_count=temp_count
        
        #count for the connected dead_ends
        count_dead = 0
        
        ## now finding the dead ends that are connected with each other
        matrix_map_dead = [ temp[:] for temp in grid]
        
        # function which counts the dead ends in the matrix
        temp_count = self.dead_call(count_dead,matrix_map_dead,matrix_map)
        count_dead+=temp_count
        
         
        
        
        ## setting the dead ends in the matrix_map_visited
        for i,j in dead_ends:
            matrix_map_visited[i][j] = 'D'
        
        ##now we have the visited matrix with the dead ends and we have the starting point of the gates.
        
        
        ## We will find the unique path from here
        
        path_list = [] 
        
        path = []
        temp_path = []
        
        
        edge_list = []
        
        #to keep the rejected value
        rejected = []
        
        visited = []
        
        
        self.path_call(gates_to_gates,matrix_map_visited,visited,rejected,path_list)
        
        
        #for row in matrix_map:
        #    print('   ', *row)
        #
        #print('\n')
        #
#        for row in grid:
#            print('  ', *row)
        
        ##here we will print the output of the file :
        
#        print(count_gates)
#        print(count_walls)
#        print(closed_count)
#        print(count_visited)
#        print(count_dead)
#        print(len(path_list))
#        print(dead_ends)
        
        if count_gates == 0:
            print("The maze has no gate.")
        elif count_gates == 1:
            print("The maze has a single gate.")
        elif count_gates > 1:
            print("The maze has " + str(count_gates) +" gates.")

        if count_walls == 0:
            print("The maze has no wall.")
        elif count_walls == 1:
            print("The maze has walls that are all connected.")
        elif count_walls > 1:
            print("The maze has " + str(count_walls)+ " sets of walls that are all connected.")
        
        if closed_count == 0:
            print("The maze has no inaccessible inner point.")
        elif closed_count == 1:
            print("The maze has a unique inaccessible inner point.")
        elif closed_count > 1:
            print("The maze has " + str(closed_count) +" inaccessible inner points.")
        
        if count_visited == 0:
            print("The maze has no accessible area.")
        elif count_visited == 1:
            print("The maze has a unique accessible area.")
        elif count_visited > 1:
            print("The maze has " + str(count_visited) + " accessible areas.")
        
        if count_dead == 0:
            print("The maze has no accessible cul-de-sac.")
        elif count_dead == 1:
            print("The maze has accessible cul-de-sacs that are all connected.")
        elif count_dead > 1:
            print("The maze has " + str(count_dead) + " sets of accessible cul-de-sacs that are all connected.")
        
        if len(path_list) == 0:
            print("The maze has no entry-exit path with no intersection not to cul-de-sacs.")
        elif len(path_list) == 1:
            print("The maze has a unique entry-exit path with no intersection not to cul-de-sacs.")
        elif len(path_list)> 1:
            print("The maze has " + str(len(path_list)) + " entry-exit paths with no intersections not to cul-de-sacs.")
            
        #print(count_visited)    


    def start_disp(self):
        
        filename = self.file
        
        matrix = []
        tempStr = ""
        
        file = open(filename,'r')
        
        line = file.readline()
        
        while line:
            tempStr = line.strip()
            if(len(tempStr)>0):
                temp1 = ''.join(tempStr.split())
                matrix.append(temp1)
            line = file.readline()
            
        
        ## checking the validation of the matrix
        
        length = len(matrix)
        
        ## to check around the matrix
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
        
        
        expression = "[0-3]*"
        re.compile(expression)
        
        expression_two = "[0-1]*"
        re.compile(expression)
        
        prev_length = len(matrix[0])
        
        #first_check = 0
        first_check_length = len(matrix)
        first_check_col = len(matrix[0])
        
        curr_length = 0
        
        for i in range(0,length):
            check_one = bool(re.fullmatch(expression,matrix[i]))
            
            #checking that the matrix has only 0-3 values
            
            if(check_one == False):
                #print("boom_diggy---> Incorrect input")
                
                raise Exception("maze.MazeError: Incorrect input.")
                
            
            # now to check for the length
            curr_length = len(matrix[i])
            #print(curr_length)
            
            if((2>first_check_length or first_check_length>31) or ((2>first_check_col or first_check_col>41))):
                raise Exception("maze.MazeError: Incorrect input.")
            
            if(curr_length != prev_length ):
                #print(curr_length)
                #print("boom-boom--second-----> Incorrect input")
                #print("now")
                raise Exception("maze.MazeError: Incorrect input.")
                #print(prev_length)
            
            #now checking for last digit
            if ( matrix[i][curr_length -1] == '1' or matrix[i][curr_length - 1] == '3' ):
                #print("dhoom-dhoom ---> Input does not represent a maze")
                raise Exception("maze.MazeError: Input does not represent a maze.")
                
            if( i == length-1):
                check_two = bool(re.fullmatch(expression_two,matrix[i]))
                
                if (check_two == False):
                    #print("dhoom-boom ---> Input does not represent a maze")
                    raise Exception("maze.MazeError: Input does not represent a maze.")
#            print("SSS\n")    
#            print(curr_length)
#            print(prev_length)
#            print("$$$\n")
            prev_length = curr_length
        
        
        #creation of the matrix map
        matrix_map = [[ 'p' for j in range( (2*len(matrix[0])))] for i in range(2*len(matrix))]
        
        
        #counter_variables
        
        count_j = 0
        count_i = 0
        
        #cretion of the matrix_map
        ## now creating the matrix map for the maze
        
        for i in range(1,len(matrix_map),2) :
             #setting the value of count j equal to zero here
            
            count_j = 0
            for j in range(1,len(matrix_map[i]),2) :
                
                if ( count_j <= len(matrix[0]) and count_i<=len(matrix) ) :
                    matrix_map[i][j] = matrix[count_i][count_j]
                    count_j+=1
            count_i +=1
        
        wall_list = []
        
        ##  function creating the walls
        self.wall_creation(matrix_map,wall_list)
        #print(len(matrix_map))
        #the endpoints having list of gates
        gates = []
        
        #the counter for the gates
        count_gates = 0
        
        
        #the list for the walls
        walls = []
        
        #the counter for the walls
        count_walls = 0
        
        #the list for the closed 
        closed = []
        
        #the count for closed
        closed_count = 0
        
        #the list for dead count
        dead_ends = []
        
        #count of dead
        count_dead = 0
        
        
        
        ## used for checking the set of the walls and passed in the analysis_loop
        grid = [temp[:] for temp in matrix_map]
        
        # the call for the analysis_loop
        # this loop is identifying the walls, gates,counts etc.
        gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid = self.analysis_loop(gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid,matrix_map,directions)
        gates,count_gates,walls,count_walls,closed,closed_count,dead_ends,count_dead,grid
        
        matrix_map_dead =  [temp[:] for temp in matrix_map ]
        
        ## for the dead_ends
        list_dead = []
        
        
        
        #list for where the pillars are present
        pillars = []        
        
        ## for the identification of the pillars
        self.pillar(pillars,matrix_map,grid)        
        
        
        ### now checking the accessible areas for the maze 
        ##matrix_map_visited = [ temp[:] for temp in matrix_map]
        matrix_map_visited = [ temp[:] for temp in grid]
        
        #the list of the gates
        gates_to_gates = [temp for temp in gates]
        
        #visited count for the accessible areas
        count_visited = 0
        
        ##checking accessible areas of the maze
        count_visited = self.visited_loop(gates,count_visited,matrix_map_visited)
        
        
        # now finding the in-accessible paths and consecutive dead ends
        inaccessible = []
        
        #checking the inaccessible areas of the maze
        temp_count = self.closed_call(closed_count,inaccessible,matrix_map,matrix_map_visited,dead_ends,grid)
        closed_count=temp_count
        
        #count for the connected dead_ends
        count_dead = 0
        
        ## now finding the dead ends that are connected with each other
        matrix_map_dead = [ temp[:] for temp in grid]
        
        # function which counts the dead ends in the matrix
        temp_count = self.dead_call(count_dead,matrix_map_dead,matrix_map)
        count_dead+=temp_count
        
        ## setting the dead ends in the matrix_map_visited
        for i,j in dead_ends:
            matrix_map_visited[i][j] = 'D'
        
        ##now we have the visited matrix with the dead ends and we have the starting point of the gates.
        
        
        ## We will find the unique path from here
        
        path_list = [] 
        
        path = []
        temp_path = []
        
        
        edge_list = []
        
        #to keep the rejected value
        rejected = []
        
        visited = []
        
        row_disp = len(grid)
        col_disp = len(grid[0])
        
        self.path_call(gates_to_gates,matrix_map_visited,visited,rejected,path_list)
        
        
        temp_dead_list_list = []
    
        for i in range(0,len(grid)-1):
            for j in range(0,len(grid[0])-1):
                if grid[i][j] == 'D' and matrix_map[i][j]!='G':
                    temp_dead_list_list.append((i,j))
        
        
        self.display_file(wall_list,pillars,temp_dead_list_list,path_list,int(row_disp/2),int(col_disp/2),filename)
        
    
    def __init__(self, filename):
        #pass
        # REPLACE PASS ABOVE WITH YOUR CODE
        self.file = filename
        #file = filename
    
    # POSSIBLY DEFINE OTHER METHODS
        

    def analyse(self):
        #pass
        self.start()
        
        #start()
        ##  function creating the walls
        
        # REPLACE PASS ABOVE WITH YOUR CODE
        
    
    def display(self):
        #pass
        self.start_disp()
        # REPLACE PASS ABOVE WITH YOUR CODE