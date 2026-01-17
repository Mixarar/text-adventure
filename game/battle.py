import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.playerturn = True
        
        print(f"\n--- BATTLE STARTED: {player.name} vs {enemy.name} ---")
        self.start_battle()

    def start_battle(self):
        while self.player.alive and self.enemy.alive:
            print(f"\n{self.player.name} HP: {self.player.health} | {self.enemy.name} HP: {self.enemy.health}")
            
            if self.playerturn:
                action = input("Your turn! (attack/heal/skip): ").lower()
                if action == "attack":
                    self.doTurn()
                    self.playerturn = False
                elif action == "heal":
                    print(self.player.use("SmallPotion"))
                    self.playerturn = False
                elif action == "skip":
                    self.playerturn = False
                else:
                    print("Invalid command.")
            else:
                print(f"{self.enemy.name} attacks!")
                self.doDamage(self.player, self.enemy)
                self.playerturn = True

        if self.player.alive:
            print(f"You defeated {self.enemy.name}!")
        else:
            print("You have been defeated...")

    def doTurn(self):
        self.doDamage(self.enemy, self.player)
    
    def doDamage(self, target, attacker):
        damage = 0
        
        if hasattr(attacker, 'dmgmult'):
            base_val = 10 # Base player strength
            damage = int(base_val * attacker.dmgmult)
        else:
            damage = attacker.damage

        actual_damage = random.randint(damage - 2, damage + 2)
        if actual_damage < 0: actual_damage = 0

        print(f"{attacker.name} hit {target.name} for {actual_damage} damage!")
        target.take_damage(actual_damage)