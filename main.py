board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

turn = 0

class Player1:

    win = False
    turn = 0

    def __init__(self, name):
        self.name = name

    def new_turn(self):
        self.turn += 1


class Player2:

    win = False
    turn = 0

    def __init__(self, name):
        self.name = name

    def new_turn(self):
        self.turn += 1


def print_board():
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("--|---|--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--|---|--")
    print(f"{board[7]} | {board[8]} | {board[9]}")


def player1_choice():
    try:
        user_choice_case = int(input(f"{player1.name.upper()} wich case (1-9) ? : "))
    
        if user_choice_case > 9 or user_choice_case < 1:
            print("Enter a number between 1 and 9")
            player1_choice()
        elif board[user_choice_case] != " ":
            print("case already filled")
            player1_choice()
        else:
            board[user_choice_case] = "x"
            
    
    except ValueError:
        print("Enter a number pls")
        player1_choice()



def player2_choice():

    player2_turn = 0

    try:
        user_choice_case = int(input(f"{player2.name.upper()} wich case (1-9) ? : "))
    
        if user_choice_case > 9 or user_choice_case < 1:
            print("Enter a number between 1 and 9")
            player2_choice()
        elif board[user_choice_case] != " ":
            print("case already filled")
            player2_choice()
        else:
            board[user_choice_case] = "o"
            
    
    except ValueError:
        print("Enter a number pls")
        player1_choice()



def check_winner():

    # Horizontally
    if (board[1] == "x" and board[2] == "x" and board[3] == "x") or (board[4] == "x" and board[5] == "x" and board[6] == "x") or (board[7] == "x" and board[8] == "x" and board[9] == "x"):
        player1.win = True

    elif (board[1] == "o" and board[2] == "o" and board[3] == "o") or (board[4] == "o" and board[5] == "o" and board[6] == "o") or (board[7] == "o" and board[8] == "o" and board[9] == "o"):
        player2.win = True

    # Vertically
    if (board[1] == "x" and board[4] == "x" and board[7] == "x") or (board[2] == "x" and board[5] == "x" and board[8] == "x") or (board[3] == "x" and board[6] == "x" and board[9] == "x"):
        player1.win = True

    elif (board[1] == "o" and board[4] == "o" and board[7] == "o") or (board[2] == "o" and board[5] == "o" and board[8] == "o") or (board[3] == "o" and board[6] == "o" and board[9] == "o"):
        player2.win = True

    # Diagonally
    if (board[1] == "x" and board[5] == "x" and board[9] == "x") or (board[3] == "x" and board[5] == "x" and board[7] == "x"):
        player1.win = True

    elif (board[1] == "o" and board[5] == "o" and board[9] == "o") or (board[3] == "o" and board[5] == "o" and board[7] == "o"):
        player2.win = True


player1 = Player1(str(input("What's your name ? : ")))
player2 = Player2(str(input("What's your name ? : ")))

print_board()

while not player1.win and not player2.win and turn != 9:

    player1_choice()

    print_board()

    check_winner()

    turn += 1

    if not player1.win and turn != 9:
        player2_choice()

        print_board()

        check_winner()

        turn += 1

    

if player1.win:
    print(f"Congrats {player1.name} ! You win !")
elif player2.win:
    print(f"Congrats {player2.name} ! You win !")
else:
    print("It's a Draw !")