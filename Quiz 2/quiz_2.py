# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3

import sys
from random import seed, randrange
from pprint import pprint
from collections import defaultdict

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE


temp_keys = [*sorted(mapping.keys())]

j=0;
flag = True;
cycle = {}

for i in temp_keys :
    #print('Key value :', i )
    flag = True
    temp_cycle = []
    
    temp_cycle.append(i)
    
    temp = mapping[i]
    
    while (temp!= i):
        
        try:
            #condition to check for self loops and previous encountered loops
            if(temp == mapping[temp] or temp < i) :
                #print("inside")
                flag = False
                break
        except:
            flag = False
            break
        
        #condition to check for forward occuring loops yet to be encountered
        if(temp_cycle.count(temp)<2):
            temp_cycle.append(temp)
        else:
            flag = False
            break
        
        try:
            temp = mapping[temp]        
        except :
            #print("exception")
            flag = False
            break
    
    if(flag == True):
        #temp_cycle.append(i)
        #temp_cycle.sort()
        #temp_cycle.add(i)
        cycle[j] = temp_cycle
        j+=1

cycles = [*cycle.values()]

#The following code deals with the reversed dictionary

inv_dict = {}

# first inverse of the list
for key,value in mapping.items():
    inv_dict[value] = inv_dict.get(value,[])
    inv_dict[value].append(key)
    

final_dict = {}
#final_dict.setdefault(list)

#sorting via counting the values of the keys to create another temporary value a tuple 
temp = sorted((len(value),(key,value)) for key,value in inv_dict.items())

#creation of the final dicionary

#the final result
for count,(key,value) in temp:
    #final_dict[cnt][k] = v
    final_dict[count] = final_dict.get(count,{})
    final_dict[count][key] = value

#keys = temp.keys()

reversed_dict_per_length = dict(final_dict)

#below code is not sorting the values, hence the approach was changed. 
"""
inv_keys = [*inv_map.keys()]
inv_values = [*inv_map.values()]

for k in inv_keys:
    count = len(inv_map.get(k))
    #reversed_dict_per_length.update(count,inv_map.get(v))
    try:
        exist = reversed_dict_per_length[count]
        exist[k] = inv_map.get(k)
        temp_val = exist
    except:
        temp_val = inv_map.get(k)    
    reversed_dict_per_length[count] = {k:temp_val}
    #reversed_dict_per_length.update({count:temp_val})


mat_keys = [*sorted(mapping.keys())]
mat_values = [*sorted(mapping.values())]

rows, cols = (len(mat_keys),len(mat_values))

mat = [[[0]*rows]*cols]
for i in range (0,rows) :
    for j in range (0,cols):
        print('$$$$$$$$$$$$$$')
        print(mat[i][j])
        print('\t')
    print("\n")

"""
print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
print(reversed_dict_per_length)
