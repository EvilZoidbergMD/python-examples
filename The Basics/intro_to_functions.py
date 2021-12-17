
def main():
    #Functions are some of the most useful tools for organizing your code.
    #Most big programs are divided up into tons of functions. Not only do
    #functions help organize your code, they also allow you to reuse your
    #code. If I set a variable to be 5, I can call the same code to do an
    #action to it repeatedly instead of copy/pasting the code all of those
    #times. Also if I decide I want to change what I'm doing, I only have
    #to go change it in one place, instead of changing it in every place
    #that I copy/pasted it.
    number = 5
    print('Original number: ' + str(number))

    #Here, we call our function 'addFive()' and put 'number' inside the parentheses.
    #When the function executes, the value of number will be used as 'input'.
    #'new_number' is being set equal to the function. What this does is that the
    #value that the function returns is put into the variable 'new_number'
    new_number = addFive(number)
    print('New number: ' + str(number))

    #And we can do this more than once with different inputs and get different outputs
    another_new_number = addFive(new_number)
    print('Another new number: ' + str(number))

    #We can even change the value of an existing variable to be something else.
    #This is very common in programming. In math, seeing x = x + 1 would be very
    #strange, but in programming it just means 'make x equal to whatever it currently
    #is plus 1'.
    number = addFive(another_new_number)
    print('Number again: ' + str(number))
    number = addFive(number)
    print('Number again: ' + str(number))
    number = addFive(number)
    print('Number again: ' + str(number))


#This function takes an input named 'input'. Whatever you put in the parentheses
#when you call it will be called 'input' here.
def addFive(input):
    #A return statement is what the function sends back to where it was called.
    return input + 5;


if __name__ == '__main__':
    main()
