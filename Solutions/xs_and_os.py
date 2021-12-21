
def xs_and_os(string):
    #Modify this file to return True if the input string has more X characters
    #than O characters. Return False is there is an equal number, or more O characters.


    x_count = 0
    o_count = 0

    for char in string:
        if char == 'X':
            x_count = x_count + 1
        if char == 'O':
            o_count = o_count + 1

    return x_count > o_count

def main():
    string1 = 'XXXXOOOOXXXXXXXXXXX'
    expected1 = True
    print('Test string with more Xs')
    test(xs_and_os(string1), expected1)

    string2 = 'XXXXOOOO'
    expected2 = False
    print('Test string with equal number of Xs and Os')
    test(xs_and_os(string2), expected2)

    string3 = 'XXXXOOOOO'
    expected3 = False
    print('Test string with more Os')
    test(xs_and_os(string3), expected3)

def test(result, expected):
    if result == expected:
        print('Passed!')
    else:
        print('Failed!')
        print('Expected result was: ' + str(expected))
        print('Actual result was: ' + str(result) + '\n')


if __name__ == '__main__':
    main()
