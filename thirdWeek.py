##ch = "banana"
##count = 0
##
##for x in ch:
##    if (x == 'a'):
##        count += 1
##print("there are ", count, " 'a'")


##def countCh(string, ch):
##    count = 0
##    for x in string:
##        if x == ch:
##            count += 1
##    return count
##
##print(countCh("banana", 'a'))


##print("banana".index('n'))
##print("banana".find('n'))


# **************string.find(Null) RETURN -1 ********************
##def inBrackets(string):
##    indexOfP = string.find('(')
##    indexOfP2 = string.find(')')
##
##    if(indexOfP == -1):
##        return "No opening bracket"
##    if(indexOfP2 == -1):
##        return string[indexOfP +1: ]
##
##    return string[indexOfP+1: indexOfP2]
##
##print(inBrackets("ban(ana"))


##string = "whatever I want i go hard to get it"
##
##splitedString = string.split(" ")
##
##print(splitedString)
##
##for x in splitedString:
##    if (x == "want"):
##        print(splitedString.index(x))
##print(type(splitedString))


#*******List*************
##arr = ["Hi", 3.0, 4, [3,4]]
##
##for x in arr:
##    print (x)
##
##print(type(arr))


#**************List is mutable APPEND CHANGES ARR**********************
##arr = list("Hello")
###arr = list(range(10))
##
##print(arr) # NOT WORKING IT. RETURNS NOTHING. CHANGES ARR


#find the number of which email have been in the list
##def findEmail(listEmail):
##        
##
##
##def countEmail(listEmail, domain):
##
##
##        
##while (True):
##    string = str(input("Enter your email: "))
    

##******************8End of stirng and list**********************
##print("banana".find("n", 3))


##first = [0] * 10
##first = list(range(10))
##print(first[2:5])

# **********************[] on the console is an empty list **************

##arr = list("abcdef")
##
##index = arr.index('f')
##arr.insert(index, "dangBoy") 
##print(arr)
##
##arr.pop(1)
##print(arr)
##
##arr.remove('a')
##print(arr)
##
###kind of adding a list USE APPENED IF YOU WANNA ADD AN ELEMENT AS ITSELF
##arr.extend("what")
##print(arr)
##
###APPEND
##arr.append("what")
##print(arr)
##
##arr.insert(0, "what")
##print(arr)
##
##arr.reverse()
##print(arr)
##
###ALPHABETICAL ORDER or NUMERICAL ORDER
##arr.sort()
##print(arr)


##newArrSen = []
##arr = ["sad","cat","was","wet"]
##
##arr.remove("was")
##print(arr)
##
##arr.pop(2)
##print(arr)
##
###since the list is mutable you can
###arr[0] = "sat"
##arr.insert(0, "sat")
##arr.remove("sad")
##print(arr)
##
##arr.append("fat")
##arr.insert(0, "mat")
##arr.reverse()
##
##index = 0
##
##newArr = arr[:3]
##newArr2 = arr[3:]
##newArrSen = ["on","the"]
##
##for x in newArr:
##    newArrSen.insert(index,x)
##    index += 1
##
##for x in newArr2:
##    newArrSen.append(x)
##    
##print(newArrSen)
##
##sen = newArr + newArrSen + newArr2
##print(sen)
##
###****************this can work inserting in between *******************8
##arr[3:3] = ["on","the"]
##print(arr)
##
##string = " ".join(arr)
##print(string)

##temp = 0
##count = 0
##lst = [1,3,4,2,6,5,7,10]
##
##minimum = lst[0]
##maximum = lst[0]
##
##for x in lst:
##    if minimum >= x:
##        minimum = x
####    if maximum <= x:
####        maximum = x
##    
##print(minimum)
##print(lst)

##count = 0
##total = 0
##lst = [1,2,3,4,5,6,7,8,9]
##
##for x in lst:
##    total += x
##    count +=1
##
##print(total / count)

#************************************String if you try to change the sstring by using briket that's fine ****************


##lst = [2,5,4,3,2,4,4,4,4,5,5,1,2,2,2,5,6,7,8,9,9,9,4]
##
##indexPivot = 0
##indexCompare = 0
##
##while():
##    while():
##        pivot = lst[indexPivot]
##        compare = lst[indexCompare]
##        
##        if pivot == compare:
##            lst.remove(compare)
##            indexCompare += 1
##            
##        indexCompare += 1
##    indexPivot += 1    


lst = [[22,20],[24,0],[26,10]]
print("we need to do ", lst[2][1], " problems on ", lst[2][0], "th")

for x in lst:
    for y in x:
        print(y, end= ' ')
        
        
























    






