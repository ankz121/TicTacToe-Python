# Ankit Patel
# TicTacToe
# 04/12/2022

from enum import IntEnum


class TicTacToe:
    class STATES(IntEnum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    # Initializes the board array.
    # Array is empty to start with.

    def __init__(self):
        self.board = []

    # Start method starts the program.
    # Users can enter the rows and columns they want to play
    # Generates the table using 2 for loops the first is for rows the second is for columns
    # Displays the table and prompts the user for the first players symbol
    # Finally starts the play Game method

    def start(self):

        num_rows = int(input("Enter the rows: "))
        num_columns = int(input("Enter the columns: "))

        for i in range(num_rows):
            rows = []
            for j in range(num_columns):
                rows.append("|_|")
            self.board.append(rows)

        for rows in self.board:
            for item in rows:
                print(item, end=" ")
            print()

        player_1 = input("Pick your symbol X or O:")

        self.game(player_1)

    # Game definition is playing the game first checks if there is a winner which at first there is not
    # The method takes the first player who chose any symbol and checks which one it is
    # The player is prompted to enter a row and a column that they want to place the X or O
    # The place_marker takes the symbol, row and column and places it in the array.
    # A swap player is run in place_marker
    # A winner check is done again as the game method is called again.
    # If a winner is found the restart method is called otherwise player 2 plays

    def game(self, player):

        win = False
        if self.isWinner():
            self.restart()

        while True:
            if player == "X":
                row = int(input("Enter the row: "))
                column = int(input("Enter the column: "))

                if win:
                    print("End")
                    break
                else:
                    player = self.place_marker("X", row, column)
                    self.game(player)
                break

            else:
                row = int(input("Enter the row: "))
                column = int(input("Enter the column: "))
                if win:
                    break
                else:
                    player = self.place_marker("O", row, column)
                    self.game(player)
                break

    # Adds the symbol to the array
    # Has to subtract 1 from the index as an array starts from position 0 not 1
    # Prints out the new array
    # Does a player swap and returns the new player

    def place_marker(self, symbol, row, column):

        self.board[row - 1][column - 1] = symbol
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

        if symbol == "X":
            return "O"
        if symbol == "O":
            return "X"

    # isWinner checks for the winner.
    # Winner can be n in a row.
    # Winner can be n in a column.
    # Winner can be n in a diagonally.
    # Uses set container to remove unique values and checks to see if there are any matching
    # The for loop iterates through the array first row and then column for the first loop
    # The second loop goes first through columns then rows
    # If the set finds matching values at each index it prints who won and returns true so prompt the restart method

    def isWinner(self):

        n = len(self.board)

        # Row check

        for rows in self.board:
            if set(rows) == {'X'}:
                print("X wins by rows")
                return True
            if set(rows) == {'O'}:
                print("O wins by rows")
                return True

        for i in range(0, n):
            col_val = []
            for rows in self.board:
                col_val.append(rows[i])
            if set(col_val) == {"X"}:
                print("X wins by columns")
                return True
            if set(col_val) == {"O"}:
                print("O wins by columns")
                return True

        # Left diagonal check
        # Uses [i][i] to find the information at position 1,1 and then 2,2 and then 3,3,...

        left_diag = []
        for i in range(0, n):
            left_diag.append(self.board[i][i])
        if set(left_diag) == {"X"}:
            print("X wins diagonally")
            return True
        if set(left_diag) == {"O"}:
            print("O wins diagonally")
            return True

        # Right diagonal check
        # Does the same as the left however instead of using [i][i] it uses [i][n-1-i] to find the right diagonal
        # n is the length of the array

        right_diag = []
        for i in range(0, n):
            right_diag.append(self.board[i][n - 1 - i])
        if set(right_diag) == {"X"}:
            print("X wins right diagonally ")
            return True
        if set(right_diag) == {"O"}:
            print("O wins right diagonally ")
            return True

    # Performs a restart.
    # If yes clears the array and starts the start method again

    def restart(self):
        restart = input("Do you want to restart Y/N?: ")

        if restart == "Y":
            self.board = []
            main.start()
        else:
            quit()


main = TicTacToe()
main.start()
