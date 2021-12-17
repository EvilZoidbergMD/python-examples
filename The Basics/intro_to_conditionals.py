
def main():
    #Conditionals are how you can have your program respond to different information.
    #The most common conditional is the 'if' statement. Essentially, it checks 'if'
    #something is true. If it is true, then it does the code inside the 'if' statement.
    condition = True

    #The double equals sign is the operator that is used to check if something is equal
    #to something else. So this says 'If condition is True, then print True'
    if condition == True:
        print('True')

    #If condition is False, then print 'False'. Notice how this doesn't print in the program's
    #output. That is because condition is NOT 'False'. Consequently, this block of code doesn't run.
    if condition == False:
        print('False')



    print('\n')



    #Booleans are not the only thing that can be compared.
    number = 10
    if number == 10:
        print('The number is equal to 10')
    if number / 2 == 5:
        print('The number divided by 2 is equal to 5')
    if number * 2 == 50:
        #Notice how this doesn't print
        print('The number times 2 is equal to 50')



    print('\n')



    string = 'Hello'
    if string == 'Hello':
        print('The string says Hello')
    if string == 'Goodbye':
        #Notice how this doesn't print
        print('The string says Goodbye')



    print('\n')



    #An additional thing you can do with 'if' statements is to use an 'else' statement.
    #An 'else' statement comes after an 'if' statement, and only runs if the 'if' statement
    #did not.
    boolean = False
    if boolean == True:
        #Notice how this doesn't print
        print('The boolean is True')
    else:
        #But this does print
        print('The boolean is False')



    print('\n')



    #You can also chain if statements together by using 'elif' statements. An 'elif'
    #Is basically another 'if' statement, but it only runs if the one's chained before
    #it didn't. So the code below checks if the number is 1. If it isn't it checks if
    #the number is 2. If it isn't, it checks if the number is 3, and so on.
    number = 5
    if number == 1:
        print('1')
    elif number == 2:
        print('2')
    elif number == 3:
        print('3')
    elif number == 4:
        print('4')
    elif number == 5:
        #Notice how this is the only one that prints
        print('5')
    elif number == 6:
        print('6')
    elif number == 7:
        print('7')
    else:
        #This else block will only run if ALL of the previous if statements do not
        print('none of the above')



    print('\n')



    #Additionally, you can do more than check if things are equal. You can also check if they are
    #not equal, greater than, less than, greater than or equal to, or less than or equal to.
    if 5 < 3:
        #Doesn't print because the condition is false
        print('5 is less than 3')
    if 5 >= 3:
        #This does print because the condition is true
        print('5 is greater than or equal to 3')
    if 5 != 3:
        #This does print because 5 is not equal to 3
        print('5 is not equal to 3')



    print('\n')



    #Lastly, you can chain conditionals together using 'and' and 'or'. 'and' is the word used to
    #check if multiple conditions are all true. 'or' is used to check if at least one of the conditions
    #is true. Both are useful in different circumstances.
    if 5 > 3 and 6 > 3:
        #This prints because both conditions were true
        print('5 is greater than 3 and 6 is greater than 3')
    if 5 > 3 and 6 < 3:
        #This does NOT print because one of the conditions was false
        print('5 is greater than 3 and 6 is less than 3')
    if 5 > 3 or 6 > 3:
        #This prints when both conditions are true
        print('5 is greater than 3 or 6 is greater than 3')
    if 5 > 3 or 6 < 3:
        #This prints when when one of the two conditions is true
        print('5 is greater than 3 or 6 is less than 3')
    if 5 < 3 or 6 < 3:
        #This does NOT print because neither of the conditions is true
        print('5 is less than 3 or 6 is less than 3')



if __name__ == '__main__':
    main()
