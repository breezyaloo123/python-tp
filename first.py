
def main():
    #on ouvre le fichier en mode lecture
    #with open("C:/Users/HP/Documents/setup/projet/python/test.txt","r") as aloo:
        #for ligne in aloo:
           #print(ligne)
    
    aloo = open("C:/Users/HP/Documents/setup/projet/python/test.txt","r")
    #la methode readlines() permet de lire un fichier du debut a la fin
    #Par contre la methode readline() permet de lire un mot caractere par caractere dans un fichier
    ligne = aloo.readline()
    while ligne != "":
        print(ligne)
        ligne = aloo.readline()

   
    
    animaux = ['vache', 'souris', 'levure', 'bacterie']
    #on ecrit dans le fichier par le mode w
    with open("C:/Users/HP/Documents/setup/projet/python/file.txt","w") as aloo:
        for ligne in animaux:
            aloo.write("{}\n".format(ligne))
           

    #the method append() add an element to the end of the list
    animaux.append("mouton")

    for animal in animaux:
        print(animal)
    
    print("the boss")

    for i in range(len(animaux)):
        print(animaux[i])

    print("the king")
    i = 0
    while i < len(animaux):
        print(animaux[i])
        i = i + 1

    #triangle
    number = int(input("Donner le nombre de *: "))
    for i in range(number):
        print("*" * i)

 




if __name__ == "__main__":
        main()
        