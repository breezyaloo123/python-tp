from model.player import Player
from model.weapon import Weapon

knife = Weapon("Couteau",3)

player1 = Player("Aloo",12,4)

#print("Pseudo: ",player1.get_pseudo())
#player1.damage(3)

#print("Il vous reste ",player1.get_health() ,"Points de vie")

player2 = Player("Sall",20,5)

player1.attack_player(player2)

print(player1.get_pseudo(), "attaque",player2.get_pseudo())

print("Bienvenu au joueur ",player1.get_pseudo(),"/ Points de vie:",player1.get_health(),"/ Attaque:",player1.get_attack())

print("Bienvenu au joueur ",player2.get_pseudo(),"/ Points de vie:",player2.get_health(),"/ Attaque:",player2.get_attack())