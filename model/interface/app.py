#cette librairie permet d'avoir une interface graphique
from tkinter import *
#cette librairie permet d'ouvrir des pages web
import webbrowser

#methode pour declencher le navigateur
def open_web():
    webbrowser.open_new("http://www.google.com")

#creer une premiere fenetre
window = Tk()

#personnaliser cette fenetre

window.title("My Application")

window.geometry("1080x720")
window.minsize(460, 360)
window.iconbitmap("C:/Users\HP\Documents\setup\projet\python\model\interface\loo.ico")
window.config(background='#41B77F')

#Ajouter une frame

frame = Frame(window, bg='#41B77F', relief=SUNKEN)

#Ajouter un premier texte
label_title = Label(frame, text="Bienvenu sur l'Application", font=("Courrier 40") ,bg='#41B77F', fg='white')
label_title.pack()
#Ajouter un sous-titre
label_subtitle = Label(frame, text='Hello Guys', bg='#41B77F', font=("Courrier, 20"), fg='white')
label_subtitle.pack()

#ajouter le frame dans le window
frame.pack(expand=YES)

#Ajouter un premier bouton

link = Button(frame, text="Ouvrir Youtube", bg='white', font=("Courrier, 20"), fg='#41B77F', command=open_web)
link.pack(pady=25,fill=X)

#afficher la fenetre
window.mainloop()