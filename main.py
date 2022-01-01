line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]


def print_board():
    print(f"{line1[0]} | {line1[1]} | {line1[2]}")
    print("--|---|--")
    print(f"{line2[0]} | {line2[1]} | {line2[2]}")
    print("--|---|--")
    print(f"{line3[0]} | {line3[1]} | {line3[2]}")


print_board()

user_choice_row = int(input("Which row ? : "))
user_choice_column = int(input("Which column ? : "))

if user_choice_column == 1:
    line1[user_choice_row - 1] = "x"
elif user_choice_column == 2:
    line2[user_choice_row - 1] = "x"
elif user_choice_column == 3:
    line3[user_choice_row - 1] = "x"


print_board()

