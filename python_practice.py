#!/bin/python3



#String

print('hello world')

print('''then string runs multiople 
lines''')  #to print in  multiple lines....

print("""then string runs multiople 
lines""")  #to print in  multiple lines....

print("this string "+"is awesom")

print('\n')

print('\n')


#MATH


print(50+50)#sums up no
print('\n')
print(50/3)
print(50//3)#returns no reminder
print('\n')

#VARIABLE AND METHOD

quote= "All is fair in love and war"
print(quote)
print('\n')
#methods
print('#######################methods######################')
print('\n')
print('\n')

print(quote.upper())#converts to upper case
print(quote.lower())#convertss to lower case

print(quote.title())#converts to tille case

print(len(quote)) #len() returns length of the string

print('\n')
print('\n')

name = 'Sadashiv'
age = 21
gpa = 8.9

print(name)
print(age)
print(int(age))

print(int(30.9))#doesnt rounf off

print("My name is "+name+" and i am "+str(age)+" years old")#while printing intiger type in print statment always convert int to str  , by using str(int)

age+=1
print(str(age))
print(str(gpa))



birthday = 1
age+=birthday
print(str(age))

print('\n')



#FUNCTIONS
print('######################FUNCTIONS#####################')
print('\n')

def add_one_hundred(num):
    print(num+100)

print(add_one_hundred(20))

print('######################')
print('\n')



def who_am_i():#fun without parameter
    name = 'Sadashiv'
    age='21' #here i declare int as string string by putting('') so in print i dont have to use str(int)

    print("My name is "+name+" and i am "+age+" years old")

print(who_am_i())




def add(x,y):
    return(x+y)

print(add(4,12))





def sqrt(x): #takes square root of no
    return(x ** 0.5)

print(sqrt(64))
print(sqrt(4))






def sqrt(x): #returns square of  no
    return(x ** 2)

print(sqrt(64))
print(sqrt(4))


def nl(): #ufn to print new line
    print('\n')

nl() #being called

def mul(x):
    print(x*100)

mul(10)

nl()


#BOOLEAN
print('#################boolean###############')
nl()
nl()

bool1 = True 
bool2 = 3+3==9
bool3 = False
bool4 = 3*3!=9
print(bool1,bool2,bool3,bool4)

bool5=23

print(type(bool1))#type method cheaks the class of given input
print(type(bool5))#type method cheaks the class of given input

nl()

#RELATIONAL AND BOOLEAN OPERATORS
print("#######RELATIONAL AND BOOLEAN OPERATORS#######")

nl()

is_greaterthan = 5>7

print(is_greaterthan)

test_and = (7>5)and(5<7) #if both condition is true then full statment is TRUE
test_and2 = (7>5)and(5>7)
test_OR = (7>5)or(7<5)#if one condition is true then full statment is TRUE
test_OR2 = (7>5)or(7>5)
print(test_and)
print(test_and2)
print(test_OR)
print(test_OR2)
nl()

#CONDTIONAL STATMENT
print('#CONDTIONAL STATMENT')


nl()



def drink(money):
    if money>=2:
        return "you can drink"
    else:
        return "you cant drink"
print(drink(2.9))
nl()



def drink(money):#without return statment
    if money>=2:
        print("you can drink")
    else:
        print("you cant drink") 
    
drink(1.9)
nl()


#age and money shoud be sufficent to drink

def alocholdrnk(age,money):
    if(age>=21 and money >=5):
        return"you can drink"
    elif(age>=21 and money < 5):
        return"uou need money more"
    elif(age<21 and money >= 5):
        return"you need to grow old"
    else:
        return"come with more money and age"
    
print(alocholdrnk(21,6))
print(alocholdrnk(21,4))
print(alocholdrnk(20,6))
print(alocholdrnk(11,4))
nl()
nl()



#LISTS
print('#LISTS')
nl()

movies =['when harry met sally','the eifil tower','Wildflower']
print(movies)

print(movies[1])#prints the second item in list

print(movies[-1])#prints last movie in list
print(movies[1:3])#prints movies from 1 to 3 but excluding 3
print(movies[0:])#prints all movies in list

#apply method to list

print(len(movies))#prints no of element in list movie

movies.append('Jaws')#adds jaws to last in the list
print(movies)

movies.insert(2,'Hustle')#adds Hustle in position 2
print(movies)

movies.pop()#pops element from end of list
print(movies)

movies.pop(2)#pops item from 2 position of the list
print(movies)

#concatination of two lists

amber_movies = ['Just grow','50 dates']

our_movies = amber_movies + movies
print(our_movies)

#2D lists

grades = [['bob',82],['lisha',90],['jeff',72]]
bob_grades = grades[0][1]
lisha_grades = grades[1][1]
print(bob_grades)
print(lisha_grades)
#modifying lists
grades[0][1]=84
print(grades)