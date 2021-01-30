# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:39:11 2019

@author: Uttkarsh Sharma
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:31:20 2019

@author: Uttkarsh Sharma
"""

import re
import time

startTime = time.time()

# the pattern to check for the first case
pattern_one_A="^Please convert \\w*$"
test_one_A= re.compile(pattern_one_A)

#sub pattern for case one
pattern_one = "^Please convert (\d){0,1}(\d){0,1}(\d){0,1}(\d){0,1}$"
test_one = re.compile(pattern_one)

#the pattern to check for the roman numbers presence
pattern_two = "^Please convert \\b[I|V|X|L|M|C|D|M]*\\b$"
test_two = re.compile(pattern_two)

#pattern to check for the second case
pattern_three_A= "^Please convert \\w* using \\w*$"
test_three_A = re.compile(pattern_three_A)


#the pattern for checking the validity of the roman numbers
pattern_three = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
test_three = re.compile(pattern_three)

#this is the pattern for the second question i.e. first digit to roman 
pattern_four = "^Please convert \\b[0-9]*\\b using \\b[a|A-z|Z]*\\b$"
#pattern_four = "^Please convert \\w* using \\w*$"
test_four = re.compile(pattern_four)

#this is the pattern for the second question second part i.e. roman to digit
pattern_five = "^Please convert \\b[a|A-z|Z]*\\b using \\b[a|A-z|Z]*\\b$"
test_five = re.compile(pattern_five)

#this is the pattern for the third question
pattern_six ="^Please convert \\w* minimally$"
test_six = re.compile(pattern_six)

Entre = input("How can I help you? ")
enter = ' '.join(Entre.split())

#for the roman number to arabic check case
en = Entre.split()   
    

output = ""
#for question 1 part 1 ( changing the given arabic number to roman)

def arabic_to_roman(number):
    
    if(number<=0 or number >=4000):
        #print("error")
        return "error"
    else:
        romanDict = [ [1000 , 'M'] , [ 900, 'CM' ], [ 500, 'D' ] , [ 400 , 'CD'],
            [ 100 , 'C' ], [90, 'XC'] , [50,'L'] , [40,'XL'] ,
            [  10, 'X'] , [9,'IX'], [5,'V'], [4,'IV'],
            [   1, 'I']]
    
        result = ''
        for denominator, roman_digit in romanDict:    
            result += roman_digit*(int)(number/denominator)
    #        print("The result is as follows :")
    #        print(result)
            
            number %= denominator
    #        print("the number is as follows:")
    #        print(number)
            
    #        print("The denom is as follows:")
    #        print(denom)
        #romanDict.    
        return result

##for question 1 changing the roman number to arabic
def roman_to_arabic(num):
    
    lof = [i for i in num]

    roman = {
              'I' : 1,
              'V':  5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000
            }
    
    prev = 0
    res = 0
    
    for i in lof : 
      curr = roman[i]
      if (curr>prev):
          temp = curr - prev
          res-=prev
          prev=0
      else:
          temp = curr
      
      prev = temp
      res+=temp
    
    return res

#the below two functions cater to the second question
    
def arabic_to_Roman_using(arabic,code):
    
    count = len(code)
    codec = [ i for i in code ]
    #print("codec is as follows:")
    #print(codec)
    test = codec.pop()
    first = [1,test]
    codec.reverse()

    c_f_f = 1
    c_f_t = 0
    
    temp = []
    val = 0
    
    
    prev_sym = test
    
    four_nine = [4,9]
    power = 0
    cnt = 0
    
    for i in codec:
        temp.append([four_nine[cnt%2]* (10**power), prev_sym + i])
        cnt+=1
        
        val = (5**(c_f_f) ) * (2**(c_f_t))
        temp.append([val,i])   
        
        if ( c_f_f > c_f_t):
            c_f_t+=1
        elif( c_f_f == c_f_t):
            c_f_f+=1
            power+=1
            prev_sym = i
            
    temp.reverse()
    temp.append(first)
    
    #print(temp)
    number = int(arabic)
    
    result = ''
    
    for denominator, roman_digit in temp:    
        result += roman_digit*(int)(number/denominator)
    #        print("The result is as follows :")
    #        print(result)
        
        number %= denominator
    #        print("the number is as follows:")
    #        print(number)
        
    #        print("The denom is as follows:")
    #        print(denom)
    #romanDict.    
    
    #printing the number
        
    return result
    

#again second question part 2 for the roman to arabic
    
def roman_to_Arabic_using(number,cod,define):
    
    flag = False
    alphaCheck = False
    count_flag = True
    
    if(define == 'using'):
        
        set_cod = set(cod)
        
        tmp1 = len(set_cod)
        tmp  = len(cod)
        
        #print(tmp1)
        #print(tmp)
        
        if(cod.isalpha()):
            alphaCheck = True
            
        if( tmp1 == tmp and bool(alphaCheck)):
            flag = True
        
        if( bool(flag) and bool(alphaCheck)):
            cod_rev = cod[::-1]
            
            test_string = cod_rev[1::2]
            
            for i in test_string:
                if(number.count(i) >1):
                    count_flag = False
                    break
    
#    flag = False
#    alphaCheck = False
#    
#    if(define == 'using'):
#        
#        set_cod = set(cod)
#        
#        tmp1 = len(set_cod)
#        tmp  = len(cod)
#        
#        #print(tmp1)
#        #print(tmp)
#        
#        if(cod.isalpha()):
#            alphaCheck = True
#            
#        if( tmp1 == tmp and bool(alphaCheck)):
#            flag = True
        
        #set_cod = set(cod)
        
#        if(cod.isalpha() != True):
#            flag = False
            
#        elif(len(set_cod) == len(cod)):
#            temp =""
#            op=""
#            
#            for s in number:
#                if(s not in op):
#                    op+=s
#            
#            if(op == cod):
#                flag = True
#            else:
#                flag = False
#        else:
#            flag = False
        
    elif( define == 'min' ):
        flag = True
        alphaCheck = True
        count_flag = True
    
        
    if(flag == True and bool(alphaCheck) and bool(count_flag)):
        
        code = [i for i in cod]
    #print(code)
        codec = {}
        
        c_f_f = 1
        c_f_t = 0
        
        try:
            fi = code.pop()
            codec[fi] = 1
        
            code.reverse()
        
            for i in code :
            
                val = (5**(c_f_f) ) * (2**(c_f_t))
                codec[i] = val   
            
                if ( c_f_f > c_f_t):
                    c_f_t+=1
                elif( c_f_f == c_f_t):
                    c_f_f+=1
        except:
            res = "error"
            return res
            
        #print(codec)
        
        #now convering the number
        lof = [ i for i in number]
    
        prev = 0
        res = 0
        
        for i in lof : 
          try:
              
              curr = codec[i]
              if (curr>prev):
                  temp = curr - prev
                  res-=prev
                  prev=0
              else:
                  temp = curr
              
              prev = temp
              res+=temp
          except:
             #print("error")
             res = "error"
             break
        #print(res)
        return res
    
    else:
        res = "error"
        return res


#function for the third question, minimal conversion:

def roman_to_arabic_minimally(x):
    
    
    set_x = set(x)

    op = ""
    if( len(set_x) == len(x)):
        
        stack_x = [ i for i in x]
        
        length = len(stack_x)
        
        while(len(stack_x)!=0):
            
                top    = stack_x.pop()
                if(len(stack_x)!=0):
                    second = stack_x.pop()
                    op += second + top 
                else:
                    op += top
        
        out = op[::-1]
        #print(out)
        re = roman_to_Arabic_using(x,out,'min')
        return re,out
    
    else:
    
        x_rev = x[::-1]
        string = [i for i in x]
        temp = 0
        genRoman = []
        
        placeval = 1
        
        prev = ''
        
        while(len(string)!=0):
            
            char = string.pop()
            if(char in genRoman and char!=prev):
                   
                       testchar = genRoman.pop()
                       
                       #while(testchar!=char and len(genRoman)!=0 ):
                       while(testchar!=char):
                           if(len(genRoman)!=0):
                               testchar = genRoman.pop()
                           else:
                               break
                       ## this section will re-construct the string i.e. first get the index of the string
                       result = [i for i, letter in enumerate(x_rev) if letter == char]
                       
                       result_set = len(result)
                       left = result[0]
                       right = result[1]     
                       
                       sub_rev = x_rev[left:right+1]
                       
                      #counting length of the substring
                       
                       sub = sub_rev[::-1]
                       #print("SubString is " + sub)
                       length = len(sub)
                       
                       if(length == 3):
                           
                           le =  sub[0:1]
                           mid = sub[1:2]
                           right = sub[2:3]
                           
                           addString = le + right + mid
                           
                           #adding the string here
                           
                           string.append(le)
                           string.append(right)
                           string.append(mid)
                           
                           #print("After adding the string:" + addString)
                        
                       elif(length == 4 ):
                           first = sub[0:1]
                           second = sub[1:2]
                           third = sub[2 : 3]
                           fourth = sub[3:4]
                           
                           addString = second + first + fourth + third
                           
                           string.append(second)
                           string.append(first)
                           string.append(fourth)
                           string.append(third)
                       
                       stacklen = len(genRoman)
                       #setting the value of temp here, and will have to check
            
                       temp = stacklen%2
            
            elif(temp == 0):
                    genRoman.append(char)
                    temp = 1
                    
            elif( temp == 1 and prev!=char):
                
                rem_check = string.count(char)
                if( rem_check == 0):
                    genRoman.append(char)
                    temp = 0
                else:
                    genRoman.append(str(placeval))
                    placeval+=1
                    temp = 0
                    
                    string.append(char)
                
            prev = char    
        
        op = ""
        genRoman.reverse()
        
        output = op.join(genRoman)
        
        #print(output)
            
        #print("The output is as follows :")
        #print(output)
        
        re = roman_to_Arabic_using(x,output,'min')
        return re,output


def check(re,co):

    codex = ""
    cof = co[::-1]
    
    string = str(re)
    lof = [i for i in string]
    
    lof.reverse()
    
    start = 0
    end   = 2
    
    cnt = 0
    for i in lof:
        if( i == '6'):
            lof[cnt] = '4'
            first  =  cof[start:start+1]
            second = cof[start+1:end]
            
            codex+=second+first
        else:
            sub = cof[start:end]
            codex+=sub
        start = end
        end+=2
        cnt+=1
        
    op = codex[::-1]
    lof.reverse()
    
    num =""
    num = ''.join(lof)
    
    #print(op)
    return num,op
    


def check_for_minima(string,codex):
    
    string_list = [i for i  in string]
    code_list = [i for i in codex]
    
    length_of_code = len(code_list)
    
    final_list = []
    final_codex= []
    
    temp = []
    
    index = []
    list_of_strings =[]
    cnt = 0
    
    length = len(string)
    
    for s in string:
        temp = string
        if (int(s) == 6):
            index.append(cnt)
        cnt+=1
    
    #print(index)
    
    construct = []
    
    ## now reversing this index and the finding the number of cases
    index.reverse()
    
    for i in index:
        
        #print(i)
        
        temp = list(string_list)
        temp_code = list(code_list)
        
        temp[i] = '4'
        #print(temp[i])
        
        first_half = temp_code[0:i]
        #print(first_half)
        
        first  = temp_code[i:i+1]
        #print(first)
        
        second = temp_code[i+1:i+2]
        #print(second)
        
        rest = temp_code[i+2:length_of_code]
        #print(rest)
        
        construct = first_half + second + first + rest
        
        temp_str = ''.join(temp)
        constructed_code = ''.join(construct)
        
        final_list.append(temp_str)
        final_codex.append(constructed_code)
    
    #print(final_list)
    #print(final_codex)
     
    final_list.reverse()
    final_codex.reverse()
    
    return final_list,final_codex
    

#This is where we begin our main function
#### ---> From here we begin our checks for the given strings <--------#####
check_one = bool(re.fullmatch(pattern_one_A,enter))

if(check_one == True):
    
    if(bool(re.fullmatch(pattern_one,enter))):
        test = [int(s) for s in enter if s.isdigit()]
    
        if( int(test[0]) == 0):
            print("Hey, ask me something that's not impossible to do!")
        else:
            num = int(re.search(r'\d+', enter).group(0))
            res = arabic_to_roman(num)
    
            if(res!="error"):
                output = "Sure! It is " + res
                print(output)
            else:
                print("Hey, ask me something that's not impossible to do!")
                
    elif( bool(re.fullmatch(pattern_two,enter))):
        
        if (bool(re.fullmatch(pattern_three,en[2]))):
        
            number = en[2]
            res = roman_to_arabic(number)
        
            output = "Sure! It is " + str(res)
            print(output)
        else:
            print("Hey, ask me something that's not impossible to do!")
    else:
        print("Hey, ask me something that's not impossible to do!")

elif(bool(re.fullmatch(pattern_three_A,enter))):
    
    if(bool(re.fullmatch(pattern_four,enter))):
        #for digit check
        test = [int(s) for s in enter if s.isdigit()]
    
        if( int(test[0]) == 0 and len(test)>0 ):
            print("Hey, ask me something that's not impossible to do!")
        else:
            res = arabic_to_Roman_using(en[2],en[4])
        
            if(res!="error"):
                output = "Sure! It is " + str(res)
                print(output)
            else:
                print("Hey, ask me something that's not impossible to do!")
       
        #print(output)
    elif( bool(re.fullmatch(pattern_five,enter))):
    
        res = roman_to_Arabic_using(en[2],en[4],'using')
    
        if(res!="error"):
            check_case = arabic_to_Roman_using(res,en[4])
    #print("check")
    
            if( en[2] == check_case):
                output = "Sure! It is " + str(res)
                print(output)
            else:
                print("Hey, ask me something that's not impossible to do!")
        else:
            print("Hey, ask me something that's not impossible to do!")
    else:
        print("Hey, ask me something that's not impossible to do!")

elif( bool(re.fullmatch(pattern_six,enter))):
    #print("####inside")
    
    flag = True
    inside_flag = True
    
    for s in en[2]:
        if s.isdigit():
            flag = False
            break
    if(flag == True):
        #first response
        res,code = roman_to_arabic_minimally(en[2])
        
        #print(res)
        #print(code)
        
        if(res!="error"):
            
            #this gives the possible minima
            final, codex = check(res,code)
            #print(final)
            #print(codex)
            
            #sanity check for the output(maxima)
            inv_iter2 = arabic_to_Roman_using(res,code)
            
            if(en[2] == inv_iter2):
                ## to check which amongst the two is correct: this is the boundary check
                
                #the below is a possible minima          
                inv_iter = arabic_to_Roman_using(final,codex)
                #print(inv_iter)
                
                if(en[2] != inv_iter):
                #print("error")
                    #We will now check for the list here for a possible occurence of a minima
                    
                    #list_num = []
                    #list_co  = []
                    
                    list_num,list_co = check_for_minima(str(res),code)
                    
                    print(list_num)
                    print(list_co)
                    
                    count_of_min = 0
                    
                    for i in range(0,len(list_num)):
                        check_min = arabic_to_Roman_using(int(list_num[count_of_min]),list_co[count_of_min])
                        if(check_min == en[2]):
                            final = list_num[count_of_min]
                            codex = list_co[count_of_min]
                            inside_flag = False
                            break
                        count_of_min+=1
                else:
                    inside_flag = False
                    
                    
                if(bool(inside_flag)):
                     final = res
                     codex = code
            
                for s in range(0,len(code)):
                    if (code[s].isdigit()):
                        #print("inside")
                        codex = codex.replace(code[s],'_')
                
                out_put = "Sure! It is " + str(final) +" using " + codex
                print(out_put)
            
            else:
                print("Hey, ask me something that's not impossible to do!")
                
        else:
            print("Hey, ask me something that's not impossible to do!")
            
    else:
        print("Hey, ask me something that's not impossible to do!")
        
else:
    print("I don't get what you want, sorry mate!")

endTime = time.time()

elapsed_time = endTime-startTime
print(elapsed_time)