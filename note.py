#programme qui permet de savoir ceux qui sont admis ou recales apres un exam

def entry_note():
    
    for i in range(5):
        student_mark = float(input("Donnez la note de l'Etudiant: "))
        if student_mark >= 10.0:
            with open("C:/Users/HP/Documents/setup/projet/python/filenote.txt","a") as mark:
                mark.write("\n{} admis\n".format(student_mark))
                
        else:
            with open("C:/Users/HP/Documents/setup/projet/python/filenote.txt","a") as mark:
                mark.write("\n{} recale\n".format(student_mark))
        
            


def showed_note():
    with open("C:/Users/HP/Documents/setup/projet/python/filenote.txt","r") as readen_mark:
        for i in readen_mark:
            print(i)
            

            




entry_note()
showed_note()