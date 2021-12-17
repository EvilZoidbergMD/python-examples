

def main():
    #Get input and store it in a variable called 'person'
    person = raw_input('What is your name? ')
    #Print out hello plus the information stored in the variable 'person'
    print('Hello, ' + person)



    #Print a blank line
    print('\n')



    #Loop through this code 10 times
    #counter will start at 0, and then loop
    #up until it hits 9 for a total of 10
    #repetitions.
    for counter in range(10):
        #Print out what loop we are on
        #Notice that since counter is a number, we have to use
        #str() to turn it into a string so that we can add it to
        #the other words we want to print.
        print('We have looped ' + str(counter) + ' times!')



    #Print a blank line
    print('\n')



    #Run the code we've named fizzBuzz twice
    #Notice that we can run code out of order
    #using this
    fizzBuzz()
    fizzBuzz()



    #Print a blank line
    print('\n')



    #Get information from the user and store it in 'yes_or_no'
    yes_or_no = raw_input('Do you like oregano? ')

    #Check if 'yes_or_no' says 'yes'
    if yes_or_no == 'yes':
        #If 'yes_or_no' says 'yes', reply to it
        print('Me too!')
    #if 'yes_or_no' doesn't say 'yes' then check if it says 'no'
    elif yes_or_no == 'no':
        #If it does, reply to it
        print("Well I'm putting it on the pizza anyway!")
    #if it says neither 'yes' nor 'no'
    else:
        print("Well that isn't a very good answer...")


#This code can be run out of order by
#calling fizzBuzz()
def fizzBuzz():
    print('Fizzy Fizzy Buzz Buzz')



if __name__ == '__main__':
    main()
