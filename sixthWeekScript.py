class Car:
    color = "grey"
    hp = 300

    def __init__(self, m = "Tata", mo = "Harrier"):
        self.make = m
        self.model = mo

    def tune(self):
        self.hp += 50
    

shan_car = Car("Porche", "911")
shan_car.model = "911 GT3"
print(shan_car.make, shan_car.model, shan_car.color)

seva_car = Car()
seva_car.model = "macan"
seva_car.color = "green"
print(seva_car.make, seva_car.model, seva_car.color)

hit_car = Car()
hit_car = tune()


class Point:
    
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b
        
    def __str__(self):
        s = f"Point({self.x},{self.y})"
        return s

#******************initializing the distance**************************
##    def __int__(self):
##        f = int(self.distance)
##        return f
    
    def calculateDistance(self):
        distance = (self.x**2 + self.y**2)**0.5
        return distance
    

p1 = Point(1,2)
p2 = Point(4,4)
p3 = Point(3,1)
p4 = Point()

print(p1.calculateDistance())
print(p2.calculateDistance())
print(p3.calculateDistance())
print(p4.calculateDistance())

print(p1)
print(p2)
print(p3)
print(p4)


class Rectangle:

    def __init__(self, a = 0, b = 0):
        self.width = a
        self.height = b

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width*2)+(self.height*2)

r1 = Rectangle(5,5)
print(r1.area(), r1.perimeter())

class Circle:

    def __init__(self, a = 0):
        self.radius = a

    def area(self):
        return (self.radius**2) * 3.14

    def perimeter(self):
        return (self.radius * 2) * 3.14

c1 = Circle(5)
print(c1.area(), c1.perimeter())

class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hrs = h
        self.min = m
        self.sec = s

    def __str__(self):
        return f"{self.hrs}:{self.min}:{self.sec}"

    def normalize(self):
        mins, self.sec = divmod(self.sec, 60)
        self.min += mins
        self.hrs, self.min = divmod(self.min, 60)

    def increment(self, seconds):
        self.sec += seconds
        self.normalize()

    def add():
        self.hrs += other.hrs
        self.min += other.min
        self.sec += other.sec
        self.normalize()

    def add2(self, other):
        new_time = Time()
        new_time.hrs = self.hrs + other.hrs
        new_time.min = self.min + other.min       
        new_time.sec = self.sec + other.sec 
        new_time.normalize()
        return new_time
    
    
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"P({self.x},{self.y})"

    def dist_to(self, p):
        return sqrt((p.x - self.x)**2 + (p.y - self.y)**2)


lst = [(1,2),(3,4),(5,6),(7,8)]
dic = []
count = 0

for tpl in lst:
    x,y = tpl
    p = Point(x,y)
    dic.append(p) #list of objects 

totalX = 0
totalY = 0

for obj in dic:
    totalX += obj.x
    totalY += obj.y
    count += 1

centroidX = totalX / count
centroidY = totalY / count

centroid = Point(centroidX, centroidY)
print(centroid)

class Employee:
    def __init__(self):
        self.salary = 60000
    
    def payRaise(self, increase):
        self.salary += increase

class Manager(Employee):
    #only applicable to Manager
    def bonus (self,increase):
        self.salary += increase


kwon = Manager()
kwon.payRaise(20000)

print(kwon.salary)

jo = Employee()
jo.bonus(10000)

kwon.bonus(10000)

##print(jo.salary) #not working
print(kwon.salary)


class Mammal:
    def __init__(self):
        self.name = Mammal
    def walk(self):
        print(f"Powerwalk the {self.name}"l) 
class Dog(Mammal):
    def __init__(self):
        self.name = Dog
    def bark(self):
        print(f"Woofy the {self.name}")
class Cat(Mammal):
    def __init__(self):
        self.name = Cat
    def meow(self):
        print(f"pushy the {self.name}")


dog = Dog()
cat = Cat()
mammal= Mammal()

dog.walk()
dog.bark()

cat.walk()
cat.meow()

mammal.walk()
mammal.bark() #not working

class Mammal:
    def __init__(self, n = "Mammal"):
        self.name = n
    def walk(self):
        print(f"Powerwalk the {self.name}") 
class Dog(Mammal):
    def __init__(self, n = "Dog"):
        self.name = n
    def bark(self):
        print(f"Woofy the {self.name}")
class Cat(Mammal):
    def __init__(self, n= "Cat"):
        self.name = n
    def meow(self):
        print(f"pushy the {self.name}")


dog = Dog()
cat = Cat()
mammal= Mammal()

animals = [dog, cat, mammal]

for animal in animals:
    if isinstance (animal, Dog): # arg 2 must be a type
        animal.walk()
    elif isinstance (animal, Cat):
        animal.walk()

print()
dog.walk()
cat.walk()
mammal.walk()

dog = Dog("tung")
cat = Cat("ston")
mammal= Mammal("hard")

animal = [dog, cat, mammal]

print()
dog.walk()
cat.walk()
mammal.walk()


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __add__(self, other):
        p = Point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p
    def __mul__(self, other):
        return Point((self.x*other.x), (self.y*other.y))
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2


print(p3)

p4 = p1 * p2

print(p4)

p5 = 5 * p1

print(p5)
l

# 5 * p1 is correct
# p1 * 5 is incorrect


import random
import turtle

t = turtle.Turtle()

##count = 1
##while(True):
##    t.forward(count)
##    t.right(count)
##    t.backward(count)
##    t.left(count)
##    count += 1
ran = random.randrange(0,60)

t.speed(0)
for i in range(400):
    for j in range(50):
        ran = random.randrange(0,60)
        t.forward(ran)
        t.left(ran)
        t.right(ran)
        t.left(ran)
    t.left(5)

t.done()


import turtle
import random

ran = random.randrange(40,100)

wn = turtle.Screen()
wn.bgcolor("yellow")

t = turtle.Turtle()
for i in range(50):
    ran = random.randrange(-100,200,10)
    t.setheading(ran)
    t.forward(40)


lst = ["class", "variable"]

for words in lst:
    charac in range(len(word)):
        
        
import turtle
import random

s = turtle.Screen()
s.bgcolor("black")


t = turtle.Turtle()
t.color("white")
t.speed(10)

for i in range(100):
    for j in range(30):
        t.forward(20)
        t.left(12)
    t.right(93)
    t.forward(40)


for i in range(100):
    t = random.randrange(0,100)
    t.forward(i)
    t.right(t)

    
t.penup() #not showing lines
t.backward(100)
t.pendown() #shows lines. After this function, it displays lines

t.fillcolor("red")
t.begin_fill()
t.circle(50, 180)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.circle(50, 360)
t.end._fill()

t.goto(0,100)

def move_down():
    t.setheading(270)
    t.forward(100)
def move_up():
    t.setheading(90)
    t.forward(100)
def move_left():
    t.setheading(180)
    t.forward(100)
def move_right():
    t.setheading(0)
    t.forward(100)
    
t = turtle.Turtle()
s = turtle.Screen()
s.listen()
s.onkey(move_right, "Right")
s.onkey(move_up, "Up")
s.onkey(move_left, "Left")
s.onkey(move_down, "Down")
s.mainloop()

f = open("listOfWords.txt", 'r')
text = f.read().strip()
vocabulary = text.split(',')
print(lst)
file.close()
word = random.choice(vocabulary)
print(word)
lst = list(word)
res = ['_']*len(lst)
output(res)



def update_post(num_wrong):
    t.penup()
    t.goto(0,0)
    t.setheading(0)
    t.pendown()
    if (num_wrong > 0):
        t.forward(100)
        t.backward(200)
        t.forward(50)
        t.left(45)
        if (num_wrong>1):
            t.forward(5000**0.5)
            t.right(90)
            if(num_wrong>2):
                t.forward(5000**0.5)
                t.right(135)
                t.forward(50)
                t.right(90)
                if (num_wrong > 3):
                    t.forward(300)
                    t.right(90)
                    if (num_wrong > 4):
                        t.forward(100)
                        t.right(90)
                        if (num_wrong>5):
                            t.forward(50)
                            t.right(90)
                            t.circle(25)
                            if (num_wrong > 6):
                                t.circle(25)
                                game_over()
                                

def game_over():
    t.hideturtle()
    print("Game Over")
              
        
update_post(7)
update_post(4)





