import tkinter

#Creer la fenetre du jeu
root = tkinter.Tk()

def draw_grid():
    button = tkinter.Button(root)
    button.grid(row=0, column=0)
#personnalisation de la fenetre
root.title("Tic Tac Toe")
root.minsize(500,500)

draw_grid()

#boucle principal
root.mainloop()