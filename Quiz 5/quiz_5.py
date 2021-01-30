# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys
import re

def encode(list_of_integers):
    
    initial_list = [ bin(i)[2: ] for i in list_of_integers]
    string = ""
    
    list_given = [ str(i) for i in initial_list]
    
    final_list = []
    
    for i in list_given:
        length = len(i)
        temp = ""
        string = ""
        
        for j in range(0,length):
            temp = i[j]*2
            string+=temp
        final_list.append(string)
    
    cnt_zero = 0
    length = len(final_list)
    
    string = ""
    
    for num in final_list:
        #print(num)
        #print (cnt_zero)
        
        string+=num
        if(length - cnt_zero >1):
            string+='0'
            cnt_zero+=1
            
    #print(string)
    #print( int(string,2))
    
    return int(string,2)
    # REPLACE pass ABOVE WITH YOUR CODE    


def decode(integer):
    #pass
    
    string = bin(integer)[2: ]
    #print("$$$$$$$$$")
    #print(string)
    
    pattern = "(00|11)*"
    re.compile(pattern)
    
    last = True
    cnt_check = 0
    
    final_list = []
    #string = bin(integer)[2: ]
    #string = "11000110000011000000011000000000110000000000"
    #flag = bool(re.fullmatch(pattern,string))
    
    ## this will give the reply to the matching ones
    ## note that the indices will be in the set of two
    iter =  re.finditer(pattern,string)
    
    indices = [m.start() for m in iter]
    
    ## check for inidces:
    
        
    #print(flag)
    print(indices)
    
    length = len(indices)
    
    if(cnt_check == 0 and length>2 and length%2==0):
        check = length -2
        for i in range(1,check,2):
            if(string[indices[i]] == '1'):
                print("error")
                return None
        cnt_check +=1
        
    #print(indices)
    #print(length)
    
    valid = True
    
    list_of_num =[]
    
    if(length>2 and length%2==0):
                
        for i in range(0,length,2):
            sub = string[indices[i]:indices[i+1]]
            list_of_num.append(sub)
            
    elif(length%2==0):
        if(len(string)>=2):
            list_of_num.append(string)
        else:
            #print("error")
            valid = False
            return None
        
    else:
        #print("error")
        valid = False
        return None
    #print(list_of_num)
    
    if(valid == True):
        middle_list = []
        
        
        #first check for the values to be added in the middle list
        
        for i in list_of_num:
            
            length_num = len(i)
            sub = ""
            
            for k in range(0,length_num,2):
                    sub+=i[k]
            
            if(last == True):
                middle_list.append(sub)
        
        
        print(middle_list)
        
        if( last == True):
            for i in middle_list:
                temp = int(i,2)
                final_list.append(temp)

        #print(final_list)    
        
    
    return final_list
    
    
    
    # REPLACE pass ABOVE WITH YOUR CODE


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
