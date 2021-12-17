
def main():
    #Lists are used to make one variable hold more than one piece of information
    words = ['apple', 'banana', 'cat', 'dog']
    #The different pieces of information can be accessed by their index number.
    #The index number is the order they are in. However, programming languages
    #start counting at 0, not at 1. This means that 'apple' is in the 0 position
    #in our list, and 'dog' is in the 3 position.
    print(words[0])
    print(words[3])



    print('\n')



    #Another way to access the items in a list is to count from the back of the
    #list instead of from the front. The last item in the list can be gotten with
    #the index of -1. -2 would be the second to last item. -3 would be the third to
    #last item, and so on.
    print(words[-1])
    print(words[-2])



    print('\n')



    #To check the size of a list, you can use 'len()' and put the list inside the
    #parentheses.
    print(len(words)) #This prints 4 because there are 4 items in the 'words' list



    print('\n')



    #Under the hood, python treats strings as lists of characters. That means that
    #getting certain characters is done in the same way as lists.
    sentence = 'The quick brown fox jumped over the lazy brown dog'
    print(sentence[0]) #Prints 'T'
    print(sentence[-1]) #Prints 'g'

    #You can also get segments of a string this way. The following code takes every
    #character in the string from position 4 up to, but not including, position 9.
    #It takes that sub-string and then puts it into a variable.
    word = sentence[4:9]
    print(word) #Prints 'quick'
    word = sentence[-3:-1]
    print(word) #Prints 'do'

    #Notice that our last print statement didn't get the 'g' at the end of dog, because
    #slicing lists this way goes up to, but not including, the last character. If we
    #want to just go to the end of the string, we can do this instead:
    word = sentence[-3:]
    print(word) #Prints 'dog'
    word = sentence[27:]
    print(word) #Prints 'the lazy brown dog'

    #This can also be done the other way to start at the beginning of the string
    word = sentence[:3]
    print(word) #Prints 'The'
    word = sentence[:-4]
    print(word) #Prints 'The quick brown fox jumped over the lazy brown'


if __name__ == '__main__':
    main()
