import game
player = game.player
world = game.world

room_spawn = world.Room('Spawn', 
                       [
                            ["#", "?", "#", "#", "#"],
                            ["#", ".", ".", ".", "#"],
                            ["#", ".", "#", ".", "#"],
                            ["#", ".", ".", ".", "#"],
                            ["#", "#", "#", "#", "#"]
                       ]
                       )

room_closet = world.Room('Closet', 
                       [
                            ["#", "?", "#", "#"],
                            ["#", ".", ".", "#"],
                            ["#", ".", ".", "#"],
                            ["#", "#", "#", "#"]
                       ]
                       )

TestChar = player.Character("TestChar",room_spawn,1,1)
#print(type(TestChar))
#print(dir(TestChar)) 
# Room Initialize
room_spawn.add_door(1,0,room_closet,1,1)
room_closet.add_door(1,0,room_spawn,1,1)


while True:
    TestChar.move(input())
    print(TestChar.position())
    for i in TestChar.look():
        print(i)