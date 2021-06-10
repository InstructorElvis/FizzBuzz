#The same way that almost every developers first line of code is printing "Hello World" to the screen, when it comes to interview questions, 9/10 this question pops up for beginner level interviews. 

#Personally I've been asked this question at least 12 times, at 12 different companies. 

#My most successful solution was at an interview with The New York Times in 2016, I solved this using Java, and I used OOP like a god. So understand this question is one that i want you all to be able to recognize like the back of your hand. 

#FizzBuzz Challenge: 
'''
    Print out the values 1-100. Except if the number is divisible by 3, instead of printing the number, print "fizz". If the number is divisible by 5, instead of printing the number, print "buzz". If the number is divisible by both 3 and 5, instead of printing the number, print "fizzbuzz", if not divisible print the number itself. 
'''

def fizzbuzz(num = 101):
    for i in range(1, num):
        if(i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif(i % 3 == 0):
            print("fizz")
        elif(i % 5 == 0):
            print("buzz")
        else: 
            print(i)

fizzbuzz()













# def fizzBuzz(num = 101):
#   for i in range(1, num):
#     if(i % 5 == 0 and i % 3 == 0):
#       print('fizzbuzz')
#     elif(i % 5 == 0):
#       print('buzz')
#     elif(i % 3 == 0):
#       print('fizz')
#     else:
#       print(i)
# fizzBuzz()