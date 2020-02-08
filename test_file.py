#Creons un programme qui permet de demander un utilisateur ces coordonnees ensuite on les sauvegarde dans un fichier

def main():

    first_name = str(input("Tapez votre prenom: "))
    last_name = str(input("Tapez votre nom: "))

    #while first_name !="":
       # first_name_array.append(first_name)
        #with open("C:/Users/HP/Documents/setup/projet/python/backup.txt","a") as file:
            #for line in first_name_array:
                #file.write("Prenom")
                #file.write("\n{}\n".format(line))
        #first_name=""
    #le mode a permet d'ajouter des donnees dans un fichier mais a la fin de ce dernier
    with open("C:/Users/HP/Documents/setup/projet/python/backup.txt","a") as file:
        file.write("Prenom")
        file.write("\n{}\n".format(first_name))
        file.write("Nom de la Famille")
        file.write("\n{}\n".format(last_name))




   



if __name__ == "__main__":
    main()