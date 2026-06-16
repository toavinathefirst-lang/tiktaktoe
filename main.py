import tkinter

# Creer la fenetre du jeu
root = tkinter.Tk()

# Stockage global
buttons = []
current_player ="X"
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
        if current_player == "O":
            print("player 2  has won")
        else:
            print("player 1 has won")

    count= 0
    for i in range(3):
        current_button = buttons[clicked_column][i]
        if current_button['text'] == current_player:
            count+=1
    if count == 3:
        print("Joueur 1 a gagné verticalemment")
    #diagonalement
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print("Joueur 1 a gagné diagonalement")

    #inverse diagonal
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print("Joueur 1 a gagné diagonalement inversé")

def place_symbol(row, column):
    print("click", row, column)

    # On utilise bien [column][row] comme tu le souhaitais !
    clicked_buttons = buttons[column][row]
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