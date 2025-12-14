class Inventory:
    def __init__(self):
        self.storage = {
            "SmallPotion": 0,
            "BigPotion": 0,
            "Coin": 0,
            "WoodSword": 0,
            "IronSword": 0
        }

    def add_item(self,item):
        if item not in self.storage:
            return "No such item"
        else:
            self.storage[item]+=1
    def remove_item(self,item):
        if item not in self.storage:
            return "No such item"
        elif self.storage[item]>0:
            self.storage[item]-=1
        else:
            return "Ran out of item"

    def use(self, item):
        if self.storage[item]<=0: return False
        self.remove_item(item)
        match item:
            case "SmallPotion":
                return "You used a small potion!"
            case "BigPotion":
                return "You used a big potion!"
            case "Coin":
                return "The coin is shiny!"
            case "WoodSword":
                #if ## change sword
                return "You equipped the Wooden sword!"
            case "IronSword":
                #if ## change sword
                return "You equipped the Iron sword!"
