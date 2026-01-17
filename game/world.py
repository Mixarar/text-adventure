class Room:
    def __init__(self, name, interior=[]):
        self.name = name
        self.interior = interior
        self.players = []
        self.doors = {}
        self.chests = {}
        self.npcs = {}
    
    def add_door(self,x,y,to_room,to_x,to_y):
        self.doors[(x,y)] = (to_room,to_x,to_y)
    
    def add_chest(self, x, y, chest):
        self.chests[(x, y)] = chest

    def add_player(self,player):
        self.players.append(player)
    
    def add_npc(self, x, y, npc):
        self.npcs[(x, y)] = npc

    def remove_player(self,player):
        self.players.remove(player)

    def display(self):
        display_grid = [row[:] for row in self.interior]
        for (x, y), chest in self.chests.items():
            if not chest.looted: display_grid[y][x] = '$'
        
        for (x, y), npc in self.npcs.items():
            display_grid[y][x] = '!'
        
        for player in self.players:
            x, y = player.x, player.y
            display_grid[y][x] = player.name[0]

        return display_grid

    def valid(self, player, dir):
        interior = self.interior
        x, y = player.position()

        if dir == "up" and y > 0 and interior[y-1][x] != '#':
            return True
        elif dir == "down" and y < len(interior) - 1 and interior[y+1][x] != '#':
            return True
        elif dir == "right" and x < len(interior[0]) - 1 and interior[y][x+1] != '#':
            return True
        elif dir == "left" and x > 0 and interior[y][x-1] != '#':
            return True
        else:
            return False
        
    def get_chest_at(self, pos):
        return self.chests.get(pos)