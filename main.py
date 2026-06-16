import tkinter

#Creer la fenetre du jeu
root = tkinter.Tk()
def place_symbol(row,column):
    print("click",row,column)
def draw_grid():
   for row in range(3):
       for column in range(3):
           button = tkinter.Button(root
                ,font=("Arial",50),
                width=2,height=1,
                command=lambda r=row,c=column:place_symbol(r,c))

           button.grid(row=row, column=column)
           # Ajout des marges (padx, pady) et de l'étirement (sticky)
           button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

#personnalisation de la fenetre
root.title("Tic Tac Toe")
root.minsize(500,500)
#  donner une couleur de fond à la fenêtre pour faire ressortir l'espacement
root.configure(bg="#333333")
# Configurer la fenêtre pour que la grille s'étende et se centre
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)
draw_grid()

#boucle principal
root.mainloop()