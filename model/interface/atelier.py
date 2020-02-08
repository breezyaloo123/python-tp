#Annuaire

user_choice = int(input("Taper 1 ajouter un contact : \nTapez 2 pour rechercher : \nTapez 3 pour supprimer : \nTapez 4 pour afficher l'annuaire : \nTapez 5 pour quitter : \n"))

prenomtab = []
nomtab = []
numbertab = []


while user_choice != '':
    if user_choice == 1:
        prenom = str(input("Donner le prenom: "))
        nom = str(input("Donner le nom: "))
        number = int(input("Donner le numero: "))
        prenomtab.append(prenom)
        nomtab.append(nom)
        numbertab.append(number)
        print("\nPrenom\t\tNom de Famille\tTelephone")
        print("{}\t\t{}\t\t{}".format(prenom,nom,number))
        user_choice = int(input("Taper 1 ajouter un contact : \nTapez 2 pour rechercher : \nTapez 3 pour supprimer : \nTapez 4 pour afficher l'annuaire : \nTapez 5 pour quitter : \n"))
    if user_choice == 2:
        search_item = input("Tapez le prenom a rechercher: ")
        if search_item in prenomtab:
            index= prenomtab.index(search_item)
            prenom = prenomtab[index]
            nom = nomtab[index]
            number = numbertab[index]
            print("Prenom: {}, Nom: {}, Numero: {}".format(prenom,nom,number))
        else:
            print("Ce contact n'existe pas")

        user_choice = int(input("Taper 1 ajouter un contact : \nTapez 2 pour rechercher : \nTapez 3 pour supprimer : \nTapez 4 pour afficher l'annuaire : \nTapez 5 pour quitter : \n"))

        if user_choice == 3:
            deleted_item = input("Tapez le prenom du contat que vs allez supprimer : ")
            index = prenomtab.index(deleted_item)
            prenomtab.remove(prenomtab[index])
            nomtab.remove(nomtab[index])
            numbertab.remove(numbertab[index])

            print(str(deleted_item) + "a ete bien supprime de vos contacts ")
        
        else:
            print("Ce contact n'existe pas")
        
        user_choice = int(input("Taper 1 ajouter un contact : \nTapez 2 pour rechercher : \nTapez 3 pour supprimer : \nTapez 4 pour afficher l'annuaire : \nTapez 5 pour quitter : \n"))

        if user_choice == 4:
            if len(prenomtab) != 0:
                for i in range(len(prenomtab)):
                    print("\nPrenom\t\tNom de Famille\t\tNumero de Telephone")
                    print("{}\t\t\t{}\t\t\t{}".format(prenomtab[i],nomtab[i],numbertab[i]))
            else:
                print("L'annuaire est vide")

        user_choice = int(input("Taper 1 ajouter un contact : \nTapez 2 pour rechercher : \nTapez 3 pour supprimer : \nTapez 4 pour afficher l'annuaire : \nTapez 5 pour quitter : \n"))

        if user_choice == 5:
            print("Thanks !!!")
            user_choice = ''





        

        




        
