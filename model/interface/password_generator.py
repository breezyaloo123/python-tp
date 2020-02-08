import string
#the method randint allow to give number 
from random import randint, choice
from tkinter import *


#methode pour generer le mot de passe

def generate_passwd():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


Window = Tk()
Window.title("Generateur de mot de passe")
Window.geometry("720x480")
Window.config(background='#4065A4')

#frame principal
frame = Frame(Window, bg='#4065A4')

#creation d'image
width = 300
height = 300
image= PhotoImage(file="C:/Users\HP\Documents\setup\projet\python\model\interface\laptop.png")
#Canvas permet d'avoir une zone ou va dessiner l'image
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image = image,)
canvas.grid(row=0,column=0,sticky=W)

#creer une sous boite
right_frame = Frame(frame, bg='#4065A4')

#creer un titre
label_title = Label(right_frame, text='Mot de passe', bg='#4065A4', font=("Helvetica",20), fg='white')
label_title.pack()

#creer une entree par une methode Entry()
password_entry = Entry(right_frame, bg='#4065A4', font=("Helvetica",20), fg='white')
password_entry.pack()

#creer un bouton
send_button = Button(right_frame, text='Generate', bg='#4065A4', font=("Helvetica",20), fg='white',command=generate_passwd)
send_button.pack(pady=25,fill=X)

right_frame.grid(row=0, column=1, sticky=W)
#Afficher le frame
frame.pack(expand = YES)

#Creation d'un Menu

menu_bar = Menu(Window)

#creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label = "Nouveau", command = generate_passwd)
#permet de separer des sous menus
file_menu.add_separator()
file_menu.add_command(label = "Quitter", command= Window.quit)
menu_bar.add_cascade(label="Fichier", menu = file_menu)

menu22 = Menu(menu_bar, tearoff = 0)
menu22.add_command(label="Copier")
menu22.add_separator()
menu22.add_command(label = "Coller")
menu22.add_separator()
menu22.add_command(label="Couper")

menu_bar.add_cascade(label="Options", menu= menu22)

menu12 = Menu(menu_bar, tearoff = 0)
menu12.add_command(label = "Check update")
menu12.add_command(label = "Aide")
menu12.add_command(label = "A propos")

menu_bar.add_cascade(label = "Outils", menu = menu12)

#Configurer la fenetre pour afficher le menu
Window.config(menu=menu_bar)



#Afficher la fenetre
Window.mainloop()