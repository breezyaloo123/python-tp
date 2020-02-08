from tkinter import *

#Methode pour enregistrer les coordonnees de la personne
def person():
     with open("C:/Users/HP/Documents/setup/projet/python/backup.txt","a") as file:
        file.write("Prenom")
        #la methode get() permet de recuperer le text du input
        file.write("\n{}\n".format(firstname.get()))
        file.write("Nom de la Famille")
        file.write("\n{}\n".format(lastname.get()))
        firstname.delete(0, END)
        lastname.delete(0, END)

#creer une fenetre window
window = Tk()

#personnaliser cette fenetre
window.title("My Application")
window.geometry("720x480")
window.iconbitmap("C:/Users\HP\Documents\setup\projet\python\model\interface\loo.ico")
window.config(background='#41B77F')

#frame principal
frame = Frame(window,bg='#41B77F',relief = SUNKEN)

#firstname label
label_title = Label(frame, text='Prenom ', font=("Helvetica",20), fg='blue')
label_title.pack()

#firstname entry
firstname = Entry(frame, bg='#4065A4', font=("Helvetica",20), fg='white')
firstname.pack()

#lastname label
lastname_title = Label(frame, text = 'Nom ', font = ("Helvetica",20), fg='blue')
lastname_title.pack()
#lastname entry
lastname = Entry(frame, bg='#4065A4', font=("Helvetica",20), fg='white')
lastname.pack()

#Ajouter le frame dans le window
frame.pack(expand = YES)

#creer une bouton
send_button = Button(frame, text='Envoyer', bg='#4065A4', font=("Helvetica",20), fg='white',command = person)
send_button.pack(pady=25,fill=X)

#Afficher la fenetre
window.mainloop()