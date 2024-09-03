##word = "banana"
##word2 = [1,2,3,4,5,6] 
##
##reference = word
##reference2 = word2 
##
##print(reference)
##print(word)
##
##print(reference2)
##print(word2)
##
##
##def minAndMax (lst):
##    if (len(lst) < 1):
##        return "error"
##    else:
##        return [min(lst), max(lst)]
##
##
###**************Tuple is immutable**********************
##
##a = 1,2,3,4,5
##print(type(a))
##
##a,b = 1,2
##
##print(a, b)


##a = 1
##b = 2
##temp = 0
##
##temp = a
##a = b
##b = temp
##
##print(a,b)
##a,b = b,a


##def circle (radius):
##    return ((3.14*radius*radius), (3.14*2*radius))
##    #return [(3.14*radius*radius), (3.14*2*radius)] 
##
##radius = float(input("radius?: "))


##a = circle(radius)[0]
##b = circle(radius)[1]
##
##print(a,b)



#************unpacking *******************

##a,b = circle(radius)
##
##d,e,*other = 1,2,3,4,5,6,7
##
##print(d,e)
##print(other)
##
##d, *other, e = 1,2,3,4,5,6,7,8
##
##print(d,e)
##print(other)


##a, c = 3.14444444, 124125.1251251
##
##print(f"The a is {a:0.2f} and the c is {c:0.2f}")
##
### *****************D method is NOT WORKING FIX IT*********************
###print(f"The a is {a:0.2f} and the c is {c:8d}")
##
##rads = range(1,6)
##
##for rad in rads:
##    print(f"{rad:7.0f} {rad*3.14: 7.2f} {rad*5: 7.0f}")


##def time(second):
##    hours, mins = divmod(second, 3600)
##    mins, sec = divmod(mins, 60)
##    return hours, mins, sec
##
##
##second = int(input("Enter a BIG second: "))
##hrs, mins, secs = time(second)
##
##print(f"hr: {hrs: 0.0f} mins:{mins: 0.0f} secs:{secs: 0.0f}")


##names = ["John","sam","sarah"]    
##ages = [40,25,20]
##genders = ["male","male","female"]
##
#####****RANGE MAKES THE LEN(NAMES) ITERABLE & THEY EXPECT INTERATION AFTER 'IN' IN LOOP****
####for x in range(min(len(names), len(ages), len(genders))):
####    print(f"{names[x]} is a  {ages[x]} yrs old {genders[x]}")
##
##
###returning tuples of mixture of each list's value from each index number 
##tple = zip(names, ages, genders)
##print(tple)


##my_dict = {"name": "John",
##           "ages": 42,
##           "gender": "male"}
##
##print(my_dict)
##my_dict["name"] = "sarah"
##print(my_dict)
##
###just a values
##for x in my_dict.values():
##    print(x)
##
###returning tuples
##for x in my_dict.items():
##    print(x)


##my_dict = {"name": "kwon",
##           "age": 25,
##           "gender": "male"}
##
##for x in my_dict.items():
##    a,b = x
##    print(a, b , end= ' ')



###***********************error************** nvm i put like dic = [] = {""}
##newDict = {}
##
##newDict["1"] = "gold"
##newDict["2"] = "silver"
##
##print(newDict["1"])


##phone = {"1":"it",
##         "2":"is",
##         "3":"my",
##         "4":"num",
##         "5":"bur",
##         "6":"huh"
##         }
##count = 1
##
##nums = input("enter your number: ")
##
##for num in nums:
##    #******************just using 'in' we can determine wheteher anything is included in the dictionary
##    if num in phone:
##        print(phone[num], end= ' ')
        
    
##x = phone.copy()
##x["1"] = "this"
##
##print(x["1"])
###be careful not to aliasing the phone dictionary by putting x = phone like that
##print(phone["1"])

##f = open("note2.txt", "w")
##f.write("kwon's file\n")
##f.write("this line should be on the next line")
##
##f.close()
##
###*************just for reading*******************
##f = open("note2.txt", 'r')
##s = f.read(5) # reading and displaying on console whats on the note in file
##print(s)
##f.close()


##newFile = open("note2.txt", 'r') #find the txt by inputting "note2.txt". r for reading
##note = newFile.read(1).split() # read (index) index where reads until
##
##for x in note:
##    print(x)


###*****************************************FILE********************ERRER*********
##newFile2 = open("poem2.txt", 'w')
##newFile2.write("whatever is whatever\n die hard do one thing and be great")
##print(newFile2.read())

##newFile = open("poem.txt", 'r')
##poem = newFile.read()
##print(poem)
##newFile.close()


#**************************************error**************************************
##localNumber = input("Enter your number of your local number: ")
##newLocalNumber = "(" + localNumber
##
##books = open("book.txt", 'r')
##book = books.readline() # the readline reads a line NOT JUST A LINE. IT READS ALL LINES
##
##file = open("friend.txt",'w')
##
##for paper in book:
##    if (newLocalNumber in paper):
##        friendList = file.write(paper)
##    
##books.close()

#***************reverse the number and save it in the file***********



#****************random****************

##import random
##
##maximum = 0
##count = 1
##choice = 'y'
##playerList = {}
##champion = {}
##champName = ''
##
##while(choice == 'y'):
##    num = random.randrange(10)
##    guess = int(input("Enter your guess number: "))
##    
##    while(guess != num):
##        print("Too big" if guess>num else "Too small")
##        guess = int(input("Enter your guess number: "))
##        count += 1
##
##    print(f"you won in {count} tries")
##
##    name = input("Enter your name ")
##    
##    playerList[name] = count


#*********************guessing game********************************

##    if (playerList.get(name) == None):
##        champion[name] = count
##        champName = name   
##        print(1)
##    if(playerList.get(name) < champion.get(champName)):
##        champion[name] = count
##        champName = name
##        print(champName)
##        print(champion[champname])
##    count = 0
##    choice = input("continue (y): ")
##
##file = open("players.txt",'a')
##
##file.write(str(name))
##file.write(str(count))
##
##if (count > maximum):
##    maximum = count
##    file.write(str(name))
##    file.write(str(count))
##


###********************************practice using matrix*******************


#this program calculate the rate of change 
# of the discount offered based on how much I spend
# ex) at 40% discount it will show the exponential chart of price being dependant variable
# to decide your spending.

##def display(totalPrice):
##    stars = ''
##    while(True):
##        totalPrice =- 5
##        if (totalPrice != 0):
##            stars += "*"
##        elif(totalPrice == 0):
##            break
##    return stars
##
##print("This program will display how much you can save as more you spend")
##
##minimum = int(input("What is your lowest of your budget in spending for food"))
##maximum = int(input("What is your highest of your budget in spending for food"))
##discount = int(input("Enter the percentage of discount: %"))
##totalPrice = [[0]*(maximum+1)]*50
##
##
##for x in range(minimum,maximum):
##    totalPrice[discount][x] = x - (x * discount)
##    print(totalPrice[discount][x])
##    slope = ((discount[discount][x]) - (discount[discount - 1][x-1]))/(x-(x-1))
##    #print("the rate of change in each price interval is ", slope)
##
##for x in range(minimum, maximum):
##    print(display(totalPrice))


##pivot = 0
##
##tikTak = [['_','_','_'],
##          ['_','_','_'],
##          ['_','_','_']]
##
##while(True):
##    
##    for x in tikTak:
##        print(x)
##
##    row, column= int(input("Row: ")), int(input("colum: "))
##    tikTak[row][column] = 'o'
##
##
##    
##    for x in range(2):
##        for y in range(2):
##            if 'o' == tikTak[x][y]:
##                privot = y
##    



###*********************************Recursion******************************



##def factorial (n):
##    if (n == 1):
##        return 1
##    else:
##        return n * factorial(n-1)
##
##print(factorial(3))

###JUST ORDINARY RECURSIVE
##def fib(n):
##    if (n <= 1):
##        return 1
##    else:
##        return fib(n-1) + fib(n - 2)
###INCOMPLETE USING LIST TO SAVE THE UNNECCSARY EXECUTION
##def fib2(n, lst):
##    if n < len(lst):
##        
##    if n <= 1:
##        return 1
##    result = fib(n-1) + fib(n - 2)

##def fib3(n, dic):
##    if n in dic:
##        return dic[n]
##    if n <= 1:
##        return 1
##    result = fib(n-1, dic) + fib(n - 2, dic)
##    dic[n] = result
##    return result
##
##print(fib(5))
##
##def addition (n):
##    if n == 1:
##        return 1
##    else:
##        return n + addition(n-1)
##
##print(addition(5))

##def power(n, e):
##    if e == 1:
##        return n
##    else:
##        return n * power(n, e-1)
####
##print(power(2,4))
##
##def addition (n):
##    if len(n) == 0:
##        return n[0]
##    else:
##        return addition[0]+addition[n]
##    

##def palindrome (string):
##    if len(string) <= 1 :
##        return True
##    else:
##        return string[0]==string[-1] and palindrome(string[1:-1])




#**************************Sorting*****************************************





##lst = {5,2,6,3,1,10,11}
##
##sortedLst = {}
##
##for i in lst:
##    index = 0
##    smallest = lst[i]
##    for j in range(len(lst)):
##        if lst[j] < smallest:
##            smallest = lst[j]
##            index = j
##    sortedLst.append(smallest)
##    lst[index] = 999
##    print(sortedLst)
##
##
##def selectionSort(lst):
##    for i in range(len(lst)):
##        index = i
##        smallest = lst[i]
##        for j in range(i, len(lst)):
##            if lst[j] < smallest:
##                smallest = lst[j]
##                index = j
##        swapped = lst[i]
##        lst[i] = lst[index]
##        lst[index] = swapped
##    return (lst)

##def insertionSort(lst):
##    for i in range(1, len(lst)):
##        newCard = lst[i]
##        j = i
##        while j > 0 and newCard<lst(j-1):
##            lst[j] = lst[j-1]
##            j =- 1
##        lst[j] = newCard
##    return lst


##def bubbleSort(lst):
##    for i in lst:
##        for j in range(len(lst)-1):
##            if lst [j] > lst [j+1]:
##                lst[j], lst[j+1] = lst [j+1],lst[j]
##            print(lst)
##        print()
##    return lst







        











