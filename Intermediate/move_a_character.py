
def main():
    #Make a list of lists that contains characters that represent what each tile is.
    #We'll use 'X' to represent a wall, ' ' to represent an open tile of floor, and
    #'P' to represent the player.
    level = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', ' ', 'X', 'X', ' ', 'X', 'X', ' ', 'X'],
        ['X', ' ', 'X', ' ', ' ', ' ', 'X', ' ', 'X'],
        ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X'],
        ['X', ' ', 'X', ' ', ' ', ' ', 'X', ' ', 'X'],
        ['X', ' ', 'X', 'X', ' ', 'X', 'X', ' ', 'X'],
        ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ]
    #This will control when the game ends
    playing = True

    #These will be the coordinates that we use to keep track of where the player is
    player_x = 1
    player_y = 1

    while(playing == True):
        #This will be our main game loop. We will repeat this until the game ends.
        #First, draw the level
        draw_level(level, player_x, player_y)

        #Then get the input from the player
        command = raw_input('Enter a command >>> ')

        #Add some spacing to the output
        print('\n')

        #Check what the command is
        if command == 'up':
            #Make sure they won't hit a wall before moving
            if level[player_x][player_y - 1] == 'X':
                print("Can't move there. That's a wall.")
            else:
                player_y = player_y - 1

        elif command == 'down':
            #Make sure they won't hit a wall before moving
            if level[player_x][player_y + 1] == 'X':
                print("Can't move there. That's a wall.")
            else:
                player_y = player_y + 1

        elif command == 'left':
            #Make sure they won't hit a wall before moving
            if level[player_x - 1][player_y] == 'X':
                print("Can't move there. That's a wall.")
            else:
                player_x = player_x - 1

        elif command == 'right':
            #Make sure they won't hit a wall before moving
            if level[player_x + 1][player_y] == 'X':
                print("Can't move there. That's a wall.")
            else:
                player_x = player_x + 1

        elif command == 'exit':
            #Stop the look by changing 'playing'
            playing = False

        elif command == 'help':
            #List out the commands
            print('up: move up')
            print('down: move down')
            print('left: move left')
            print('right: move right')
            print('help: list commands')
            print('exit: exit the game')

        else:
            #If none of the other 'if' statements were triggered, that means that they put in
            #a command that doesn't exist. In that case, print a help message.
            print('Invalid command. Type "help" to see the available commands')

    #This will only be reached when the loop is finished
    print('Thanks for playing!')


def draw_level(level, player_x, player_y):
    #Add some spacing to the output
    print('\n')
    
    #Loop through the rows
    for y in range(len(level)):
        #This is what the row will look like. We'll add each tile one at a time
        row = ''

        #Loop through the tiles in the row
        for x in range(len(level[0])):
            if x == player_x and y == player_y:
                #Add the player
                row = row + 'P'
            else:
                #Add the tile
                row = row + level[y][x]

        #Then print the row
        print(row)

    #Add some spacing to the output
    print('\n')

if __name__ == '__main__':
    main()
