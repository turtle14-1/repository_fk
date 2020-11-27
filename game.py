def play(nr_1, color):
    secret_number = 3
    secret_color = "blue"

    if int(nr_1) == secret_number and color == secret_color:
        return("You've found the right number and the right color")

    if int(nr_1) == secret_number or color == secret_color:
        return("one of your answers is correct. \nagain!")

    else:
        return("you did not find out the secret. \nagain!")
    
    
    
    



print("Let's play a game!")
nr_1 = input("Enter a number between 1 and 20: ")
color = input("Enter a color: ")

print(play(nr_1, color))

