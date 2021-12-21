
def main():
    #The goal is to print out the numbers 1-50, but every time there is a
    #multiple of 3, print fizz instead of the number. Every time there is
    #a multiple of 5, print buzz instead of the number. If a numer is a
    #multiple of both 3 and 5, print fizzbuzz instead of the number.

    #This is some sample code that you can add to or change in order to play fizzbuzz.
    #Try to alter the code in order to make it play fizzbuzz properly. Currently, the
    #code prints only the even numbers from 1 to 20.
    for i in range(20):
        num = i + 1 #Remember that i starts at 0 and goes to 19, so we want one more than i

        if isDivisibleBy(num, 2):
            print(num)


#This function can be used to see if a is divisible by b. If it is, the
#function returns True. If it isn't the function returns False.
def isDivisibleBy(a, b):
    if a % b == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
