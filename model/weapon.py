class Weapon:

    def __init__(self,name,damage):
        super().__init__()
        self.name= name
        self.damage = damage

    #getters
    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.damage

    

