
def main():
    #Get two numbers from the user
    first_num = raw_input('What is the first number >>> ')
    second_num = raw_input('What is the second number >>> ')

    #The two variables are currently strings, so we need to change them to integers, then add them
    #Note: If the user types in a non-number, this will just throw an error and stop running.
    result = int(first_num) + int(second_num)

    #Because we changed the variables to numbers, result is a number, so we need to chang it
    #back to a string before printing it.
    print('The result is ' + str(result))

if __name__ == '__main__':
    main()