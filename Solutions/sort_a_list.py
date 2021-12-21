
def sort_a_list(numbers):
    #This function needs to sort numbers, then return it. Right now,
    #it just returns the original list. Modify this function to return
    #a sorted list. After you modify this function, run the file to test
    #two different lists and see if it works correctly

    done = False

    while not done:
        changed = False

        for i in range(len(numbers) - 1):
            #If the two numbers are in the wrong order...
            if numbers[i] > numbers[i + 1]:
                #...swap them
                temp = numbers[i + 1]
                numbers[i + 1] = numbers[i]
                numbers[i] = temp

                changed = True

        #If we didn't have to swap anything this time around, the list must be in order!
        if not changed:
            done = True

    return numbers


def main():
    test1()
    test2()


def test1():
    numbers = [5, 3, 1, 4, 6, 5, 8, 1000]
    print('Testing a list of whole numbers')
    result = sort_a_list(numbers)
    expected = [1, 3, 4, 5, 5, 6, 8, 1000]

    printTestResult(result, expected)


def test2():
    numbers = [5, -3, 1, 4, -6, 5, -8, 1000]
    print('Testing a list of whole numbers')
    result = sort_a_list(numbers)
    expected = [-8, -6, -3, 1, 4, 5, 5, 1000]

    printTestResult(result, expected)


def printTestResult(result, expected):
    if result == expected:
        print('Passed!\n')
    else:
        print('Failed!')
        print('Expected result was: ' + str(expected))
        print('Actual result was: ' + str(result) + '\n')


if __name__ == '__main__':
    main()
