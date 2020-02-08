
class Player:
    #constructer
    def __init__(self,pseudo,health,attack):
        self.pseudo = pseudo
        self.health = health
        self.attack =attack
    
        print("Bienvenu au joueur",self.pseudo)
    #getters
    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
    
    def damage(self,damage):
        self.health -= damage
        #print("Aie vous avez subi",damage, "degats!")

    def attack_player(self,target_player):
        #target_player.damage(self.attack)
        target_player.damage(self.attack)





class Warrior(Player):
    #constructer
    def __init__(self,pseudo,health,attack):
        #Appel du constructeur de la classe Player
        super().__init__(pseudo,health,attack)
        self.armor = 3
        print("Bienvenu au guerrier",self.pseudo)
    #getters
    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
    
    def damage(self,damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
            #Appel a la methode damage() de Player
        super().damage(damage)


    def attack_player(self,target_player):
        #target_player.damage(self.attack)
        target_player.damage(self.attack)

    def blade(self):
        self.armor = 3

    def get_armor_points(self):
        return self.armor



player = Player("Breezy",40,2)
player.damage(3)

warrior = Warrior("Aloo",20,5)
warrior.damage(4)
print("Vie: ",warrior.get_health(),"Armure: ",warrior.get_armor_points())

warrior.damage(4)
print("Vie: ",warrior.get_health(),"Armure: ",warrior.get_armor_points())

warrior.damage(4)
print("Vie: ",warrior.get_health(),"Armure: ",warrior.get_armor_points())

#la methode issubclass() permet de verifier si l'heritage maarche bien entre deux classes
if issubclass(Warrior, Player):
    print("Le Guerrier est bien une specialisation de la classe Player !!!")
       
    
