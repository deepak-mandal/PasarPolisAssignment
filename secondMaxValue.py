#Name: DEEPAK KUMAR MANDAL
#Email: dkmiitg@gmail.com
#Date: 28 May 2021
'''
Write a function which takes an array of integers given as string as an argument,
and returns second max value from the input array. If there is no second max return -1
'''

def secondMaxFunct(arr):
    arrLen=len(arr)     #length of array
    
    #if less then 2 element
    if arrLen<2:
        return -1
    
    minValue = min(arr) - 1    #storing minimum of the minimum value available
    #Initilizing both max and 2nd_max value to the Minimum values for integer
    firstMax= minValue
    secondMax= minValue
    
    
    for i in range(len(arr)):
        #if current element is greater then firstMax then updating both accordingly
        if arr[i]>firstMax:
            secondMax=firstMax
            firstMax=arr[i]
            #print('1. firstMax: {} secondMax: {} '.format(firstMax, secondMax))
            
        #if current element is in between max & 2nd_max the update secondMax. It will also reduce duplicates
        elif arr[i]>secondMax and arr[i] != firstMax:
            secondMax=arr[i]
            #print('2. firstMax: {} secondMax: {} '.format(firstMax, secondMax))
        
    
    if secondMax == minValue:      #for empty array of element
        return -1
    else:
        return secondMax                    #returns second max value as a output




if __name__ == '__main__':
    inpStr=input("Enter (Integer separation by space): ")      #Taking string as an argument 
    
    count = 0
                                    #Atfirst spliting the input string then checking the size of integer after converting the str dtype into int dtype
    for x in inpStr.split():        #For checking the individual element of the list is maximum length of 1024 only allowed
        try:
            if len(str(x)) > 1024:    # len(str(x)) > 1024 If we need each integer's character length of 1024 digit long
                count+=1
        except:
            pass
    
    
    if count == 0:     #Maximum length of the integer string can be 2^10=1024 digits
        try:
            arr=list(map(int, inpStr.split()))      #converting string to List /Array of integer type
            print(secondMaxFunct(arr))
        except Exception:
            print(-1)       #If given input is not an Integer type then return -1
    else:
        print(-1)           #if max. length of integer string exceed 1024 digits then return -1
    







'''
Sample test case:-
1. For array ["3", "-2"] should return "-2"
2. For array ["5", "5", "4", "2"] should return "4"
3. For array ["4", "4", "4"] should return -1 (duplicates are not considered as the second max)
4. For [] (empty array) should return -1.
5. For ["-214748364801","-214748364802"] should return -214748364802.

Conditions:-
1. CPU complexity should be O(n) :- Time complexity of our algorithm is O(n)
2. You are not allowed to change the array :- Here we are not changing the array
3. Maximum length of the integer string can be 2^10=1024 digits :- Applied this condition, while taking the input
'''