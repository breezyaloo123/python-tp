#Classe Batiment

class Batiment:

    #constructeur
    def __init__(self,address,nb_etage):
        self.address = address
        self.nb_etage = nb_etage

    #les getters
    def get_address(self):
        return self.address
    
    def get_nb_etage(self):
        return self.nb_etage


#la classe Immeuble herite de la classe Batiment
class Immeuble(Batiment):
    
    #constructeur
    def __init__(self,address,nb_etage,nb_balcons):
        super().__init__(address,nb_etage)
        self.nb_balcon = nb_balcons

    #les getters
    def get_address(self):
        return super().get_address()

    def get_nb_etage(self):
        return super().get_nb_etage()
    
    def get_nb_balcon(self):
        return self.nb_balcon


#la classe Banque herite de la classe Batiment

class Banque(Batiment):
    
    #Constructeur
    def __init__(self, address, nb_etage,nom,nb_coffre):
        super().__init__(address, nb_etage)
        self.nom = nom
        self.nb_coffre = nb_coffre

    #les getters

    def get_address(self):
        return super().get_address()
    def get_nb_etage(self):
        return super().get_nb_etage()
    def get_nom(self):
        return self.nom
    def get_nb_coffre(self):
        return self.nb_coffre
    

#La classe Supermarche herite de la classe Batiment

class Supermarche(Batiment):

    #Constructeur
    def __init__(self, address, nb_etage,nb_rayon):
        super().__init__(address, nb_etage)
        self.nb_rayon = nb_rayon

    
    #les getters

    def get_address(self):
        return super().get_address()
    def get_nb_etage(self):
        return super().get_nb_etage()
    def get_nb_rayon(self):
        return self.nb_rayon


address = ''
batiment = ['Immeuble','Supermarche','Banque']

for i in batiment:
    address = str(input("Donner l'adresse de "+str(i)+ " : "))
    if i == 'Immeuble':
        immeuble1 = Immeuble(address,5,4)
    if i == 'Supermarche':
        supermarket = Supermarche(address,1,30)
    if i == 'Banque':
        bank = Banque(address,12,"IPRES",1000)

print("Adresse de l'Immeuble:",immeuble1.get_address(),"\nNombre d'etage:",immeuble1.get_nb_etage(),"\nNombre balcon:",immeuble1.get_nb_balcon())

print("Adresse du Supermarche:",supermarket.get_address(),"\nNombre d'etage:",supermarket.get_nb_etage(),"\nNombre de Rayon:",supermarket.get_nb_rayon())

print("Adresse de la Banque:",bank.get_address(),"\nNombre d'etage:",bank.get_nb_etage(),"\nNombre de coffre:",bank.get_nb_coffre(),"\nNom de la Banque:",bank.get_nom())




