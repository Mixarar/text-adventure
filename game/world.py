class Room:
    def __init__(self, name, interior=[]):
        self.name = name
        self.interior = interior
        self.players = []
        #self.doors = {} future door logic
    
    def add_player(self,player):
        self.players.append(player)

    def remove_player(self,player):
        self.players.remove(player)

    def display(self):
        display_grid = [row[:] for row in self.interior]
        for player in self.players:
            x, y = player.x, player.y
            display_grid[x][y] = player.name[0]

        return display_grid

    def valid(self,player,dir):
        interior = self.interior
        x,y=player.position()
        if dir == "up" and interior[x][y-1]=='.':
            return True
        elif dir == "down" and interior[x][y+1]=='.':
            return True
        elif dir == "right" and interior[x+1][y]=='.':
            return True
        elif dir == "left" and interior[x-1][y]=='.':
            return True
        else:
            return False
        
    def teleport(self, new_room, x, y):
        if new_room.interior[x][y] == '.':
            self.room.remove_player(self)
            self.room = new_room
            self.x = x
            self.y = y
            self.room.add_player(self)
        else:
            print(f"Cannot teleport to invalid position ({x},{y}) in room {new_room.name}.")
