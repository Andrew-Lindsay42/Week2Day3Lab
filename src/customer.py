class Customer:
    def __init__(self, name, stomach, wallet, age, drunkeness):
        self.name = name
        self.stomach = stomach
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness 

    def can_afford_drink(self, drink):
        if self.wallet >= drink.price:
            return True 
        else:
             return False 
    
    def can_afford_food(self, food):
        if self.wallet >= food.price:
            return True 
        else:
             return False 

    def get_drunkeness(self):
        return self.drunkeness 

    def down_drink(self, drink):
        self.drunkeness += drink.units
        self.stomach.append(drink)

    def eat_food(self, food):
        self.drunkeness -= food.sober_effect