import random

# Global variables:
counter = 0  # turns counter
move = 0  # seek position
hitTheTreasure = False   #the condition to run the game


def settingTheGame():
    with open(r'C:\Users\orel.briga\Downloads\DevOps Course\Project_file.txt', 'w') as mainFile:  # write by overriding to file or by createing new file
        for i in range(10):
            a = random.randint(1,20)
            i = str(i)
            mainFile.write(a * i)
        mainFile.write('TREASURE')
        for i in range(9,-1,-1):
            a = random.randint(1,20)
            i = str(i)
            mainFile.write(a * i)


def checkWin():
    with open(r'C:\Users\orel.briga\Downloads\DevOps Course\Project_file.txt', 'r') as mainFile:
        global move
        global hitTheTreasure
        winner = ['T', 'R', 'E', 'A', 'S', 'U', 'R', 'E']
        mainFile.seek(move)
        Result = mainFile.read(1)

        '''The next "if" statement is for a case where the player choose a position that is higher then last letter
           in the file, we first force the seek to point the real last letter and then we move one step backwards
           so we can read it and give the player a real indication where he hit, as part of the game messages.  '''

        if Result == '' :
            mainFile.seek(0, 2)
            move = mainFile.tell() - 1
            mainFile.seek(move)
            Result = mainFile.read(1)

        for i in winner:
            if Result == i:
                hitTheTreasure = True
                print(f'Congrats! you hit \'{Result}\' which is part of the TREASURE letters!\
                \nTotal tries until winning: {counter} turns.')
                break

        if not hitTheTreasure:
            print(f'You hit \'{Result}\', keep moving!\n')


def playTime():
    with open(r'C:\Users\orel.briga\Downloads\DevOps Course\Project_file.txt', 'r') as mainFile:
        global counter
        global move
        while not hitTheTreasure:
            try:
                pointer = int(input('Where you want to move?\n1 - forward\n2 - backwards \n'))

                if pointer == 1:
                    amoutOfSteps = int(input('How many steps would you like to move forward?\n'))
                    move += amoutOfSteps  #adding the desired steps to seek to relocate the pointer accordingly.
                    counter += 1
                    checkWin()
                    move -= 1  #returning the pointer one step behind after reading the letter

                elif pointer == 2:
                    if move <= 0:
                        print('Beginning of file, can only move forwards!')
                        continue
                    amoutOfSteps = int(input('How many steps would you like to move backwards?\n'))
                    move -= amoutOfSteps  #subtracting the desired steps from the seek to relocate the pointer accordingly
                    if move < 0:
                        move = 0
                    counter += 1
                    checkWin()
                    move -= 1  #returinng the pointer one step behind after reading the letter
                else:
                    print('Invalid option, try again.')
                    continue

            except ValueError:
                print('Invalid option, try again.')
                continue


settingTheGame()  # creating the file + setting the game

playTime()   # yalla ten barosh!



