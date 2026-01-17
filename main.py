import os
import game
player = game.player
world = game.world
inventory = game.inventory
obj = game.object
npc = game.npc


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If computer is running windows use cls
        command = 'cls'
    os.system(command)

# Set up the evironment

# The main spawn
room_spawn = world.Room('Spawn', 
                       [
                            ["#", "?", "#", "#", "#"],
                            ["#", ".", ".", ".", "#"],
                            ["#", ".", "#", ".", "#"],
                            ["#", ".", ".", ".", "#"],
                            ["#", "#", "#", "#", "#"]
                       ]
                       )
# Closet room
room_closet = world.Room('Closet', 
                       [
                            ["#", "?", "#", "#"],
                            ["#", ".", ".", "#"],
                            ["#", ".", ".", "#"],
                            ["#", "#", "#", "#"]
                       ]
                       )

TestChar = player.Character("TestChar",room_spawn,1,1)
# Door Initialization
room_spawn.add_door(1,0,room_closet,1,1)
room_closet.add_door(1,0,room_spawn,1,1)

# Chests Initialization
chest = obj.Chest({
    "Coin": 5,
    "SmallPotion": 1
})

# Npcs Initialization
badguy = npc.Enemy("Badguy", health=30, damage=5)
room_spawn.add_npc(3, 3, badguy)

room_closet.add_chest(2, 2, chest)

print("Useful commands are: inventory, loot, use")
print("To move, type the direction, up/left/right/down")
print(f"Current room: {TestChar.room.name}")
for i in TestChar.look():
    print(i)
try:
     while True:
          if TestChar.alive:
            i = input()
            clearConsole()
          if i == "inventory":
               print(TestChar.invsee())
          elif i == "loot":
               print(TestChar.loot())
          elif i.startswith("use "):
                try:
                    item = i.split()[1]
                    print(TestChar.use(item))
                except IndexError:
                    print("Use what? (Example: use SmallPotion)")
          else:
               TestChar.move(i)
          
          if TestChar.alive:
               print(f"Current room: {TestChar.room.name}")
               for i in TestChar.look():
                    print(i)
          else:
              break
except KeyboardInterrupt:
     print("Closing program...")