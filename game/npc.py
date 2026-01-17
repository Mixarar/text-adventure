class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.maxhealth = health
        self.health = health
        self.damage = damage
        self.alive = True

    def take_damage(self, damage):
        if not self.alive:
            return False
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self):
        self.alive = False
        print(f"{self.name} has died.")