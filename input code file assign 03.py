print('Question 1 ')

string = input('Enter the string (preferably enter a single word) : ')
words=string.split()                      # splitting string into words
word_count = len(words)       #storing number of words in string

dict={}
if  word_count == 1:                     # it will be executed if there is only one word
    for i in words[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
else:                                  # executed when there are more than one words
    for i in words:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)


print("Question 2 ")

while True:
    day = int(input("Enter the day : ")) # using while loop for taking a valid value to run the program for all inputs
    if day >= 1 and day <= 31:
        break
    else:
        print("Please enter a valid day")

while True:
    month = int(input("Enter the month : "))
    if 1 <= month <= 12:
        break
    else:
        print("Please enter valid month")

while True:
    year = int(input("Enter the year : "))
    if 1800<= year <= 2025:
        break
    else:
        print("Please enter a valid year")

print("Date entered is " + str(day) + "/" + str(month) + "/" + str(year) )

if day >= 1 and day <= 27:
    day = day + 1
    print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year))

elif day == 28:
    if month == 2:
        if (((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0):
            day = day + 1
            print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year) )
        else:
            day = 1
            month = 3
            print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year) )
    else:
        day = day + 1
        print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year))

elif day == 29:
    if month == 2:
        if (((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0):
            day = 1
            month = 3
            print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year))
        else:
            print("Invalid Date entered")
    else:
        day = day + 1
        print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year))

elif day == 30:
    if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        day = day + 1
        print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year))
    elif month == (4 or 6 or 9 or 11):
        day = 1
        month = month + 1
        print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year))
    else:
        print("Invalid date entered")

elif day == 31:
    if month == (1 or 3 or 5 or 7 or 8 or 10):
        day = 1
        month = month + 1
        print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year))
    elif month == 12:
        day = 12
        month = 1
        year = year + 1
        print("Next Date is " + str(day) + "/" + str(month) + "/" + str(year))
    else:
        print("Invalid Date entered")





print('Question 3')

number = int(input('Enter number of elements for squaring: \n'))
list1 = []                              #creating a empty list to store values
for i in range(number):                # values added to list
    element_entry = int(input('Enter the number: '))
    list1.append(element_entry)

print('Entered inputs: ' + str(list1))

list2 = []                            # empty list for storing squared values
for i in list1:
    new_tuple = (i, i ** 2)
    list2.append(new_tuple)

print('Our required output is '+ str(list2))



print('Question 4')

grade_points = int(input('Enter your Grade points: '))
if 4 <= grade_points <= 10:
    if grade_points == 4:
        grade,performance = 'D','Poor'
    elif grade_points == 5:
        grade,performance = 'C',"Below Average"
    elif grade_points == 6:
        grade,performance = 'C+','Average'
    elif grade_points == 7:
        grade,performance = 'B','Good'
    elif grade_points == 8:
        grade,performance = 'B+','Very Good'
    elif grade_points == 9:
        grade,performance = 'A','Excellent'
    else:
        grade,performance = 'A+','Outstanding'

    print('Your Grade is %s and  %s Performance. '%(grade,performance))

else:
    print('''INVALID POINTS ENTERED
RERUN AND ENTER CORRECT VALUE
''')

    

print('Question 5')

word = 'ABCDEFGHIJK'

print('__OUTPUT__')

for n in range(6):
    #since it is 11 letter word and 2 less digits are printed each time, range is set at six

    updating = word[0:len(word)-2*int(n)]
    # index for printing is updated constantly
    print(' '* n + updating)          # space multipication is for making the pattern


print('QUESTION 6')

sid = int(input("Enter SID: "))
name = input("Enter Name: ").upper()
students = {sid:name}

while True:
    wish = input("Do you want to enter another student details(Y or N): ") #multiple entries
    wish = wish.upper()
    if wish == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ").upper()
        students[sid] = name
    elif wish == 'N':
        break
    else:
     print('Invalid input!!!')

#PART A
print('part A')
print('students details stored in dictionary are as : ',students)

#PART B

print('part B')
print('Sorted names in alphabetical order are as: ' , {k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#PART C
print('part C')
print('sorted details according to SID are as: ' ,{k:v for k,v in sorted(students.items())})

#PART D
print('part D')
search_sid = int(input("Please Enter SID Of The Student You Want To Search: " ))
print("Student with entered SID is",students[search_sid])


print("Question 7")
i=0
j=1
k=0
sum=i+j
n_term=int(input("Enter number of terms of fibonacci series to print\n"))
print(i)
print(j)

for k in range(n_term-2):
    k=i+j
    sum=sum+k
    print(k)
    i=j
    j=k
print("Average of series is ",(float(sum/n_term)))




print('Question 8')

set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

#part a
parta = (set1|set2)-(set1&set2)
print('a. ' + str(parta))

#part b
partb = (set1|set2|set3)-((set1&set2)|(set1&set3)|(set3&set2))
print('b. ' + str(partb))

#part c
partc = ((set1&set2)|(set1&set3)|(set3&set2))- (set1&set2&set3)
print('c. ' + str(partc))

#partd
new_set = {1,2,3,4,5,6,7,8,9,10}
partd = new_set - set1
print('d. ' + str(partd))

#part e
parte = new_set - (set1|set2|set3)
print('e. ' + str(parte))




    
    
