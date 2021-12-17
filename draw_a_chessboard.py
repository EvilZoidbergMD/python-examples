
def main():
    #One of the cool things about python is that it can print out any unicode character.
    #That includes emojis, symbols, and characters from many different languages.
    #The full list of unicode characters can be found here: https://en.wikipedia.org/wiki/List_of_Unicode_characters
    #One of the more fun things in unicode is that it has all of the chess pieces as symbols
    #So we can use them to make a chessboard in the terminal.

    #In order to print unicode characters, you have to put a u in front of the string
    #Then use \u0000 where 0000 is replace with the specific code for the character you want.
    #For example, print(u'\u265C') would print the black rook.
    print(u'\u250F \u2501 \u2501 \u2501 \u2501 \u2501 \u2501 \u2501 \u2501 \u2513')
    print(u'\u2503 \u265C \u265E \u265D \u265B \u265A \u265D \u265E \u265C \u2503')
    print(u'\u2503 \u265F \u265F \u265F \u265F \u265F \u265F \u265F \u265F \u2503')
    print(u'\u2503 \u2591 \u2593 \u2591 \u2593 \u2591 \u2593 \u2591 \u2593 \u2503')
    print(u'\u2503 \u2593 \u2591 \u2593 \u2591 \u2593 \u2591 \u2593 \u2591 \u2503')
    print(u'\u2503 \u2591 \u2593 \u2591 \u2593 \u2591 \u2593 \u2591 \u2593 \u2503')
    print(u'\u2503 \u2593 \u2591 \u2593 \u2591 \u2593 \u2591 \u2593 \u2591 \u2503')
    print(u'\u2503 \u2659 \u2659 \u2659 \u2659 \u2659 \u2659 \u2659 \u2659 \u2503')
    print(u'\u2503 \u2656 \u2658 \u2657 \u2655 \u2654 \u2657 \u2658 \u2656 \u2503')
    print(u'\u2517 \u2501 \u2501 \u2501 \u2501 \u2501 \u2501 \u2501 \u2501 \u251B')


if __name__ == '__main__':
    main()
