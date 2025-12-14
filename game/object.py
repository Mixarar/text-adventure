from game.inventory import Inventory

class Chest:
    def __init__(self, contents: dict):
        self.inventory = Inventory()
        self.looted = False

        for item, amount in contents.items():
            if item in self.inventory.storage:
                self.inventory.storage[item] = amount

    def loot(self, player):
        if self.looted:
            return "The chest is empty."

        for item, amount in self.inventory.storage.items():
            for _ in range(amount):
                player.inventory.add_item(item)

        self.looted = True
        return "You looted the chest."
