import tkinter

# Stockage global
buttons = []
current_player ="X"
win =False
# Creer la fenetre du jeu
root = tkinter.Tk()

def check_null():
    print("match null")

def print_winner():
    global win
    if not win:
        win = True
        if current_player == "O":
            print("player 2  has won")
        else:
            print("player 1 has won")

def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
def check_win(clicked_row, clicked_column):
    count=0
    #victoire horizontale
    for col in range(3):
        current_button = buttons[col][clicked_row]
        if current_button['text'] == current_player:
            count+=1
    if count == 3:
        print_winner()

    count= 0
    for i in range(3):
        current_button = buttons[clicked_column][i]
        if current_button['text'] == current_player:
            count+=1
    if count == 3:
        print_winner()
    #diagonalement
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    #inverse diagonal
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
    #detecter match nulle
    if not win:
        count = 0
        for i in range(3):
            for j in range(3):
                current_button = buttons[i][j]
                if current_button['text'] == "X" or current_button['text'] == "O":
                    count += 1
        print(count)
        if count == 9:
            check_null()

def place_symbol(row, column):
    print("click", row, column)

    # On utilise bien [column][row] comme tu le souhaitais !
    clicked_buttons = buttons[column][row]
    print(clicked_buttons['text'])
    if clicked_buttons['text'] == '':
        clicked_buttons.config(text=current_player)
        check_win(row, column)
        switch_player()

def draw_grid():
    # INVERSION ICI : On boucle d'abord sur les colonnes
    for column in range(3):
        button_in_col = []  # Ce sont les boutons de la colonne actuelle

        # Puis on boucle sur les lignes
        for row in range(3):
            button = tkinter.Button(
                root,
                font=("Arial", 40),
                width=2,
                height=1,
                command=lambda r=row, c=column: place_symbol(r, c)
            )

            # L'affichage à l'écran reste inchangé (row=row, column=column)
            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

            # On ajoute le bouton à notre liste de colonne
            button_in_col.append(button)

        # On ajoute la colonne complète à notre stockage global
        buttons.append(button_in_col)


# personnalisation de la fenetre
root.title("Tic Tac Toe")
root.minsize(500, 500)

# donner une couleur de fond à la fenêtre pour faire ressortir l'espacement
root.configure(bg="#333333")

# Configurer la fenêtre pour que la grille s'étende et se centre
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

draw_grid()

# boucle principal
root.mainloop()