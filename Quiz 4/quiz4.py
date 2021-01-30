# %load quiz4_iter2.py
# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.

##Final Code for the quiz

import sys

#state diagram defination is as follows :

'''
A is the dummy start state (can be removed just taken for simplicity)
B is the state for symbol check
C is the state which checks for '(' and count_) (increases) them
D is the state which checks for ')' and decreases the count_) variable
     on this state we also check if count_) is equal to arity or not?
E is the state which check for ',' 
'''

global count_open_bracket
global count_close_bracket
global count_comma
global words
global count_comma_list
global word_list
global currentState
global tempWords

count_open_bracket = 0
count_close_bracket = 0
count_comma = 0
words = 0

count_comma_list=[]


'''
state_diag ={ "A" : "start",
               AD is space  
              "B" : words and _,
              BD is space
              "C" : count_open_bracket,
              "D" : count_close_bracket,
              "E" : count_comma,
            }
'''


state_diag = ['A','AD','B','BD','C','D','E','ADD','err']



def is_valid(word, arity):
    
    #first convert the word in a list
    
    global words
    global currentState
    global tempWords
    global count_comma
    global count_comma_list
            
    
    currentState = state_diag[0]
    
    word_list = [*word]
    tempWords = []
    count_comma = 0
    #count_comma_list.append(0)
    
    for i in word_list:
        tempWords.append(0)
    
    arity_flag = True
    
    for i in word_list:
        if( (ord(i) >= 97 and ord(i)<=122) or ( ord(i)>= 65 and ord(i)<=90) or (ord(i)==95)):
            if( (currentState == state_diag[0] ) or (currentState == state_diag[1]) or (currentState == state_diag[4]) or (currentState == state_diag[6]) or (currentState == state_diag[2])):
            #global words
                currentState= state_diag[2]
                #print("inside state B")
                #print(i)
            else:
                currentState = state_diag[8]
                #print("error of B")
                break
            #state_diag["B"]= words
        
        elif(ord(i)==32):
            if( (currentState == state_diag[0]) or (currentState == state_diag[4]) or (currentState == state_diag[6]) or (currentState == state_diag[1]) ):
                currentState = state_diag[1]
            elif((currentState == state_diag[5]) or (currentState == state_diag[7])):
                currentState = state_diag[7]
            elif( (currentState == state_diag[2]) or currentState == state_diag[3]):
                currentState = state_diag[3]
            
            else:
                #print("error of space")
                #print(i)
                currentState = state_diag[8]
                break
            
        elif( ord(i)==40):
            global count_open_bracket
            #global count_comma_list
            
            count_open_bracket+=1
            
            #state_diag["C"] = count_open_bracket
            #count_comma_list.append(0)
            
            if(currentState == state_diag[2] or currentState == state_diag[3]):
                currentState = state_diag[4]
                #print("open-bracket")
                #print(i)
            else:
                #print("error of C")
                currentState = state_diag[8]
                break
                
            #print("inside state C")
        
        elif(ord(i)==41):
            #temp = 0
            
            global count_close_bracket
            #global count_comma
            #global count_comma_list
            #print("+++++++++++++++++ words at the current string is :")
            #print(words)
            
            count_close_bracket+=1
            
            if( (currentState == state_diag[2]) or (currentState == state_diag[5]) or (currentState == state_diag[3]) ):
                currentState = state_diag[5]
            else:
                #print("error of D")
                currentState = state_diag[8]
                break
                
            #print("inside state D")
            #print(i)
            
            if (count_close_bracket > count_open_bracket):
                arity_flag = False
                break
                
            #state_diag["D"] = count_close_bracket
            #now checking the arity for the function
            
            
            
        elif(ord(i) == 44 and arity>0):
            
            count_comma +=1
            if(count_comma == 1):
                count_comma_list.append(0)
            
            try:
                tempComma = count_comma_list.pop()
                tempComma+=1
                count_comma_list.append(tempComma)
            except:
                currentState = state_diag[8]
                break
            
            if( (currentState == state_diag[2]) or (currentState == state_diag[5]) or (currentState == state_diag[7]) or (currentState == state_diag[3]) ):
                currentState = state_diag[6]
            else:
                #print(i)
                #print("error of E")
                currentState = state_diag[8]
                break
            
            #print("inside state E")
        else:
            #if there is any failure observed then we will set the final state to initial/error
            #print("error")
            currentState = state_diag[8]
            break
        words+=1    
        
    print("outside for loop")
    
    #checking arity
    if(arity>0 and currentState!= state_diag[8]):
                arity_flag = arit(word,arity)
    
    if( arity == 0):
        if((count_open_bracket == count_close_bracket) and (arity_flag!= False) and (currentState == state_diag[2])):
            return True
        
    elif ( arity>0 ):
            if((count_open_bracket == count_close_bracket) and arity_flag!= False and count_open_bracket!=0 and currentState == state_diag[5]):
                return True
    else:
        return False
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    
    
def arit(wor,ari):
    
    string = wor
    
    word_list_inside = [*string]
    tempString = []
    testStr = []
    
    for i in word_list_inside:
        tempString.append("0")
    
    count = len(word_list_inside)
    
    arity_flag = True
    val = 0
    
    for i in range(0,count):
        if( word_list_inside[i] == ')' ):
            print(word_list_inside[i])
            flag = True
            temp = i
            close = i
            
            while( (flag == True) and (temp>0)):
                tempWord = word_list_inside[temp]
                print("$$$$$$ temp word is $$$$$$$$")
                print(tempWord)
                print("######### temp is ##########")
                print(temp)
                
                if( ( tempWord == '(' ) and (int(tempString[temp])== 0) ):
                    print("$$$ inside temp words")
                    tempString[temp] = 1
                    flag = False
                temp-=1
            
            print("tempstr is as follows ")
            tempstr = string[temp+1:close+1]
            testStr.append(tempstr)
            print(tempstr)
            
                
            #to remove spaces form the temp string
            tempstr.replace(" ","")
        
            #checking the length of the string i.e. it should be greater than 3 (,)
            variable = 0
            j=temp+1
            
            if(len(tempstr) > 3):
                #Now we check the substring 
                for k in tempstr:
                    if ( (k == ',') and (int(tempString[j])!=1)):
                        tempString[j]=1
                        variable+=1
                    j+=1
                
                print("######### variable is ########")
                print(variable)
                

                
            val = arity - variable
            print("----%%%% printing val%%%%----")
            print(val)
            
            print("test Str")
            print(testStr)
            
            if( val != 1 ):
                print("@@@@@ Setting the arity flag@@@@@@@@@@@@@@@@@@")
                arity_flag = False
        
    comval = [ i for i,x in enumerate(word_list_inside) if x==',']
    for i in comval:
        if (tempString[i]!=1):
            arity_flag = False
            break
        
    return arity_flag
    

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')