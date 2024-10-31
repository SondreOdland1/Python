
def say_hi(): # When we type 'def' phyton knows that we want to creat a function 
    print('Hello Users,')
    print('how are you')


print('Top')
say_hi() #Calling the function 
print('Bottom')


# We can add parameter to the function, a parameter is a piece of information that we give to the function
def say_hey(name, age):
    print('Hello' + name + str(age))
    print('how are you')       


say_hey(' Sondre ', 19)
say_hey(' Sofia ', 20)
