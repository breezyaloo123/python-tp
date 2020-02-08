#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:15:53 2019

@author: sadiosan
"""

contact_firstName = []
contact_lastName = []
contact_phone = []

user_choice = input("- Tapez 1, pour ajouter un contact : \n- Tapez 2, pour rechercher un contact : , \n- Tapez 3, pour supprimer un contact : \n- Tapez 4, pour afficher votre annuaire : \n- Tapez 5, pour quitter le programme : ")
print(user_choice)

while user_choice != '':
    if int(user_choice) == 1:
        first_name = input("Entrez le prénom : ")
        last_name = input("Entrez le nom de famille : ")
        phone = input("Entrez le numéro de téléphone : ")
        contact_firstName.append(first_name)
        contact_lastName.append(last_name)
        contact_phone.append(phone)
        
        print("\nPrénom\t\tNom de famille\t\tTéléphone")
        print("{}\t\t{}\t\t{}".format(first_name, last_name, phone))
        #user_choice = ''
        user_choice = input("- Tapez 1, pour ajouter un contact : \n- Tapez 2, pour rechercher un contact : , \n- Tapez 3, pour supprimer un contact : \n- Tapez 4, pour afficher votre annuaire : \n- Tapez 5, pour quitter le programme : ")
    if int(user_choice) == 2:
        search_item = input("Entrez le prénom que vous cherchez : ")
        #index = contact_firstName.index(search_item)
        if search_item in contact_firstName:
            index = contact_firstName.index(search_item)
            first_name = contact_firstName[index]
            last_name = contact_lastName[index]
            phone_number = contact_phone[index]
            print("Prénom : {}, Nom : {}, Téléphone : {}".format(first_name, last_name, phone_number))
            #user_choice = input('- Tapez 1, pour ajouter un contact \n- Tapez 2, pour chercher un contact \n- Tapez 3, pour supprimer \n- Tapez 4, pour quitter')
        else:
            print("Ce contact n'existe pas")
        #user_choice = ''
        user_choice = input("- Tapez 1, pour ajouter un contact : \n- Tapez 2, pour rechercher un contact : , \n- Tapez 3, pour supprimer un contact : \n- Tapez 4, pour afficher votre annuaire : \n- Tapez 5, pour quitter le programme : ")
    if int(user_choice) == 3:
        deleted_item = input("Tapez le prénom du contact que vous voulez supprimer : ")
        if deleted_item in contact_firstName:
            index = contact_firstName.index(deleted_item)
            contact_firstName.remove(contact_firstName[index])
            contact_lastName.remove(contact_lastName[index])
            contact_phone.remove(contact_phone[index])
            print(str(deleted_item) + " a été bien supprimé de vos contacts")
            
        else:
            print("Ce contact n'existe pas")
        #user_choice = ''
        user_choice = input("- Tapez 1, pour ajouter un contact : \n- Tapez 2, pour rechercher un contact : , \n- Tapez 3, pour supprimer un contact : \n- Tapez 4, pour afficher votre annuaire : \n- Tapez 5, pour quitter le programme : ")
    if int(user_choice) == 4:
        print("\nPrénom\t\t\tNom de famille\t\t\tNuméro de téléphone\n")
        print("La taille du tableau des prénom = " + str(len(contact_firstName)))
        if len(contact_firstName) != 0:
            
            for i in range(len(contact_firstName)):
                print(i)
                print("{}\t\t\t{}\t\t\t{}".format(contact_firstName[i], contact_lastName[i], contact_phone[i]))
        else:
            print("Votre annuaire est vide")
        #user_choice = ''
        user_choice = input("- Tapez 1, pour ajouter un contact : \n- Tapez 2, pour rechercher un contact : , \n- Tapez 3, pour supprimer un contact : \n- Tapez 4, pour afficher votre annuaire : \n- Tapez 5, pour quitter le programme : ")
    if int(user_choice) == 5:
        print("Merci au revoir !")
        user_choice = ''
        

