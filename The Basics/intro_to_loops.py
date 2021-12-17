
def main():
    #Loops are very useful for repeating code multiple times.
    #There are two main types of loops: for loops, and while loops.
    #For loops work like this:
    for counter in range(10):
        #This code will run 10 times, and print out the numbers 0 to 9
        #That is because programming languages usually start counting at 0
        #instead of starting at 1.
        print(counter)

    print('\n')

    #You can also adapt it to input
    number = int(raw_input('How many times to run? >>> '))
    for counter in range(number):
        print(counter)

    print('\n')

    #For loops can also be used to run once for each item in a list
    words = ['apple', 'banana', 'cat', 'dog']

    #This will loop through each item in the 'words' list. The current
    #item is put into the 'word' variable.
    for word in words:
        print(word)

    print('\n')

    #A while loop works a little differently. Instead of running a certain
    #number of times, it checks a condition each time and only ends when the
    #condition is false.
    keep_running = True
    while(keep_running == True):
        #This will keep running until 'keep_running' is no longer True
        command = raw_input('Enter a command >>> ')
        print('The command was ' + command)

        if command == 'exit':
            #'keep_running' is only changed by using the 'exit' command
            keep_running = False
            print('Goodbye!')

    print('\n')

    #Any type of conditional can be used with a while loop
    number = 0
    while number < 3:
        #This code will keep running until numer is no longer less than 3
        print(number)
        number = number + 1


if __name__ == '__main__':
    main()
