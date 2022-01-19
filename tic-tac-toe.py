"""
Assignment: Create a Tic-Tac-Toe
Author: Anamilena Casariego
"""

def main():
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Welcome to...\n-----TIC TAC TOE-----\n\n")
    print("Rules are simle:\n-Chose the number  where you want to play your turn."
    "\n-Win the first in maje a row. It can be vertically, horizontally or diagonally.")
    print()

    x_o = input("Do you want to start with x or o? ")
    x_o = x_o.lower()

    while x_o != "x" and x_o != "o":

        print("Please choose a correct option.")
        x_o = input("Do you want to start with x or o? ")
        x_o = x_o.lower()
    
    game = False
    turns = 9
    while game == False:

        print_grid(grid)

        if search_the_row(grid) == True:
            game = True

            if x_o == "x":
                print("\nO WINS!!\n")

            else:
                print("\nX WINS!!\n")

        elif turns == 0:
            game = True
            print("\nNobody wins...\n")

        else:
            correct_choose = False
            while correct_choose == False:
                position = int(input(f"\n{x_o}'s turn to choose a square (1-9): "))
                print()

                if grid[position - 1] != "x" and grid[position - 1] != "o":
                    if x_o == "x":

                        grid[position - 1] = "x"
                        x_o = "o"
                        correct_choose = True

                    elif x_o == "o":

                        grid[position - 1] = "o"
                        x_o = "x"
                        correct_choose = True
                
                else:
                    print("Please choose a different square.")
                    correct_choose = False

        turns -= 1

        
    if game:
        print("Thanks for playing Tic Tac Toe.\n")

def print_grid(grid):


    print(f"{grid[0]}|{grid[1]}|{grid[2]}\n"
           "-+-+-\n"
          f"{grid[3]}|{grid[4]}|{grid[5]}\n"
           "-+-+-\n"
          f"{grid[6]}|{grid[7]}|{grid[8]}")

def search_the_row(grid):
    s1 = grid[0]
    s2 = grid[1]
    s3 = grid[2]
    s4 = grid[3]
    s5 = grid[4]
    s6 = grid[5]
    s7 = grid[6]
    s8 = grid[7]
    s9 = grid[8]

    if (s1 == s2 and s2 == s3) or (s4 == s5 and s5 == s6) or (s7 == s8 and s8 == s9):
        return True

    elif (s1 == s4 and s4 == s7) or (s2 == s5 and s5 == s8) or (s3 == s6 and s6 == s9):
        return True

    elif (s1 == s5 and s5 == s9) or (s3 == s5 and s5 == s7):
        return True

    else:
        return False
    
if __name__ == "__main__":
    main()