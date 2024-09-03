##age = int(input("Enter your age: "))
##if(age < 18):
##    print("too young")
##elif (age > 80):
##    print("eye exam required")
##elif (age >= 18 and age <= 80):
##    print("valid for a driver license")

##for x in range(9, 6, -1):
##    print(x)
##    print("yay")
    
##for y in range(0, 5):
##    print("hello student")
    
##for x in range (30, 2, -1):
##    print(x)

##for x in range (50, 101, 2):
##    print(x)

##for x in range (0, 51):
##    if ( x % 2 == 0):
##        print(x)

##for x in range (51, 100, 2): #not even number wrong example
##    print(x)

##for x in ["joe","danny", "shanks"]:
##    print("Hi " + x)

##hr = 10
##while(hr <= 14):
##    print ("attend")
##    hr = hr + 2
##print("free to go")

##num = 50
##while(num < 100):
##    if (num % 2 == 1):
##        print(num)
##    num = num + 1


##num = int(input("Enter the number: "))
##for x in range(num, 0, -1):
##    print(x)

##num = int(input("enter the number: "))
##while(num > 0):
##    print(num)
##    num = num - 1


##number = 45
##total = 0
##while (number != 30): #number = 30 ends Loop before total += 30
##    total = total + number
##    number = number - 5
##print (total) #45+40+35 = 120

##total = 1 
##factorial = int(input("Enter the number for factorial: "))
##for x in range(1, factorial+1):
##    total = total * x
##print(total)


##choice = 'y'
##while(choice != 'Y' or choice != 'Y'):
##    factorial = int(input("enter the number"))
##    count = 1
##    total = 1
##
##    while(count <= factorial):
##        total *= count
##        count += 1
##
##    print(total)
##    print("Continue?: ")
##    choice = input()

###Calculate the total mark to print Grade
##total = 0
##for count in range(0, 5):
##    mark = int(input("Mark?: "))
##    total += mark
##
##if(total < 50):
##    print("F")
##elif(total < 60):
##    print("D")
##elif(total < 70):
##    print("C")
##elif(total < 80):
##    print("B")
##else:
##    print("A")


##mark = int(input("Enter your mark: " ))
##total = 0
##count = 0
##
##while(mark >= 0 and mark <= 20):       
##    total += mark
##    count += 1
##    if (count % 5 == 0):
##        if (total < 50):
##           print("F")
##        elif (total < 60):
##            print("D")
##        elif (total < 70):
##            print("C")
##        elif (total < 80):
##            print("B")
##        else:
##            print("A")
##        total = 0
##    mark = int(input("try again 1- 20: "))


##def add(num, num2):
##    total = num + num2
##    return total
##
##print(add(2,3))

##def greet(name):
##    return ("Hi, How are you? " + str(name))
##
##print("ladies and gentlemen, " + greet("kwon"))


##def add(num, num2):
##    total = num + num2
##    print("The total is ", total)
##
##def switchSign (num):
##    num = num * -1
##    return num 
##
##def abs(num):
##    if(num < 0):
##        num = num * (-1)
##    return num
##
###Main Program 
##num = int(input("enter a number: "))
##num2 = int(input("enter a second number to add with the first: "))
##add(num, num2)
##num = int(input("Enter the number to switch sign: "))
##print(switchSign(num))
##num = int(input("enter the number to convert into absolute value: "))
##print(abs(num))


##def max (num, num2):
##    if ( x > t):
##        return x
##    elif( t > x):
##        return t
##
##def min (num, num2):
##    if ( x < t):
##        return x
##    elif( t > x):
##        return t
##
##x = 4
##t = 6
##z = max (x, t)
##w = min (x, t)
##print ("max = ", z, "min = ", w)


##def forceTheUserToInput(minimum, maximum):
##    realMinimum = minimum
##    realMaximum = maximum
##    num = float(input("Enter number between %s to %s for each component: " % (realMinimum, realMaximum)))
##    while (num < minimum or num > maximum):
##         num = float(input("INVALID! Try to enter number between {} to {} for each component: ".format(realMinimum, realMaximum)))
##    return num
##
##def calculateGrade():
##    total = 0
##    dummy = 0
##    numberOfComponent= int(input("Enter how many component (assignment, quiz, exam, etc) in the course?: "))
##    percentagePerComponent = 100/numberOfComponent
##    for x in range(0, numberOfComponent):
##        dummy = forceTheUserToInput(0, percentagePerComponent)
##        total += dummy
##    return total
##
##def gradeToLetter(num):
##    print("Your grade is:")
##    if (num < 50):
##        print("F")
##    elif (num < 60):
##        print("D")
##    elif (num < 70):
##        print("C")
##    elif (num < 80):
##        print("B")
##    else:
##        print("A")
##
###main function
##gradeToLetter(calculateGrade())   

##def isTriangle (side, side2, side3):
##    if (side<(side2+side3) and side2<(side+side3) and side3<(side+side2)):
##        if (0 < side and 0 < side2 and 0 < side3):
##            return True
##    else:
##        return False
##
##def perimeter (side, side2, side3):
##    '''Calculate perimteter using 3 sides a,b,c,'''
##    if (isTriangle(side, side2, side3)):
##        return (side+side2+side3)
##    else:
##        return "(invalid option. Try again to input allowed number for each side)"
##
##def area (side, side2, side3):
##    '''Calculate area using/calling the perimter function''' 
##    if (isTriangle(side, side2, side3)):
##        dummyPerimeter = perimeter(side, side2, side3)
##        semiPer = dummyPerimeter / 2
##    else:
##        return "(invalid option. Try again to input allowed number for each side)"
##    return ((semiPer * (semiPer-side)*(semiPer - side2)*(semiPer-side3))**0.5)
##
##while(True):
##    choice = ''
##    side = float(input("Enter the first side: "))
##    side2 = float(input("Enter the Second sid: "))
##    side3 = float(input("Enter the Third sid: "))
##
##    p = perimeter(side, side2, side3)
##    a = area(side, side2, side3)
##
##    print("The perimeter is: ")
##    print(p)      
##    print("The area is: ")     
##    print(a)
##
##    choice = str(input("try again?: (Y/y) "))
##    if (choice != 'Y' and choice != 'y'):
##        break
        

##def totalInterest(initialAmount, interestRate, compoundPerYear, numberOfYear):
##    a = initialAmount * (1 + (interestRate / compoundPerYear)) ** (compoundPerYear*numberOfYear)
##    return a
##
##
##initialAmount = float(input("Enter the amount of initial amount of money to invest: "))
##interestRate = float(input("Enter the interest rate: "))
##compoundPerYear = float(input("Enter the number of times the interest is compounded per year: "))
##numberOfYear = float(input("Enter the number of years: "))
##print("The total interest you will get is: ", totalInterest(initialAmount, interestRate, compoundPerYear, numberOfYear) , "  let's get rich! keep it up")

##course = "Introduction to Computation"
##
##for x in range(0, len(course)):
##    print(course[x])
##
##dummy = ""
##for x in range(0, course.index('d')):
##    dummy += course[x]
##print(dummy)

##dummy = ""
##course = "Introduction to Computation"
##
##for x in range(-1, -28, -1):
###for x in range(1, len(course)+1):
##    dummy += course[x]
##print(dummy)

##fruit = "banana"
##for char in fruit:
##    print(char)

##def findLastLetterFromSen(course):
##    ch = str(input("Enter the character you wanna find: "))
##    
##    for x in range(len(course)):
##        if(course[x] == ch):
##           count = x
##    return count   
##
##def findFromSen(course):
##    ch = str(input("Enter the character you wanna find: "))
##    
##    for x in range(len(course)):
##        if(course[x] == ch):
##            break   
##    return x
##
##sen = "Intro to comp"
##index = findFromSen(sen)
##index2 = findLastLetterFromSen(sen)
##print("your sliced sentence between ", index, " to ", index2, " is ")
##print(sen[index:index2+1])


#*************string is immutable*******************************************
#SUCH course[3] = 'r' is INVALID
##course = "Introduction to Computation"
##
##dummy = course[0:16]
##dummy2 = course[17:27]
##
##dummy3 = dummy + "B" + dummy2
##print(dummy3)

course = "    Intro to Comp     "
##print(course.upper())
##print(course.lower())
##print(course.swapcase())
##print(course.index("Comp"))#C's index
print(course.strip()) #remove the space at the end and start of a string
print(course.count('o')) #how many character in sentence
    
           
