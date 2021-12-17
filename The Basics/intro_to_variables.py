

def main():
    #Python has many different types of variables, but this file should show you
    #some of the most common ones.

    #This is a character. A character is any single symbol, be it a number, letter, or other symbol.
    character = 'y'
    print(character)
    print('\n')

    #This is a string. A string is a sequence of characters put together.
    string = 'This is a string 1 2 3 !!!'
    print(string)
    print('\n')

    #This is an integer. An integer is any non-fractional positive or negative number
    integer = -5
    another_integer = 10

    #You can do all the normal math things with integers
    print(integer + another_integer) #Add
    print(integer - another_integer) #Subtract
    print(integer * another_integer) #Multiply
    print(another_integer / integer) #Divide
    print('\n')

    #If you want a decimal, you need to use a float.
    one_half = 0.5
    #You can still do math with floats.
    print(one_half + another_integer) #Add
    print(one_half - another_integer) #Subtract
    print(one_half * another_integer) #Multiply
    print(one_half / another_integer) #Divide
    print('\n')

    #A boolean is a variable that can only ever be either True or False.
    #Be careful, if you type it as true or false, it won't work. It has
    #to be capitalized.
    boolean = True

    #Booleans are useful when doing conditionals, like an 'if' statement

    #This checks if boolean is True
    if boolean == True:
        print('It is true')
        
    #This checks if boolean is False. Notice how this doesn't print in the program's output.
    if boolean == False:
        print('It is not true')


if __name__ == '__main__':
    main()
