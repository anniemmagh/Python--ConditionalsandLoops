#conditionals
#IF, else, elif
#if
# n = 10
# if n % 2 == 0:
#     print("This number is even") 
# else:
#     print("This number is odd")
    
#     #elif
#     n = 13
# if n > 0:
#     print("This number is Positive") 
# elif n<0:
#     print("This number is negative")    
# else:
#     print("This number is Zero")

    ### Loops ###

# while loop
# n = 100
# i = 0
# while i < n:
#     print(i)
#     i = i+1

# For loop
# number = [0,1,2,3,4,5,6,7,8,9]
# for i in number:
#     print(i**2)
# n=100
# numbers = [] #initialisation
# for i in range(100):
#     numbers.append(i**2)
#     print(numbers) 

#connect loops and conditions
# n=100
# numbers = [] 
# for i in range(100):
#     if i % 2 ==0:
#         numbers.append(i**2)



n =100
numbers = [] #initialisation
numbers_even = []
for i in range(100):
    numbers.append(i**2)
    if i % 2 ==0:
        numbers_even.append(i**2)
        print(numbers)
        print(numbers_even)
        print(len(numbers))
        print(len(numbers_even))
        
    


