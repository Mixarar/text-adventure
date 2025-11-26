import game
player = game.player
world = game.world

room_spawn = world.Room('Spawn', 
                       [
                            ["#", "#", "#", "#", "#"],
                            ["#", ".", ".", ".", "#"],
                            ["#", ".", "#", ".", "#"],
                            ["#", ".", ".", ".", "#"],
                            ["#", "#", "#", "#", "#"],
                       ]
                       )

TestChar = player.Character("TestChar",room_spawn,1,1)

print(TestChar.position())
TestChar.move('down')
print(TestChar.position())
for i in TestChar.look():
    print(i)