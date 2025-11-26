class Character:
    def __init__(self, name, room, x=0, y=0):
        self.name = name
        self.room = room
        if self.room.interior[x][y]=='.':
            self.x = x
            self.y = y
            self.room.add_player(self)
        else:
            print(f"Wrong position at {x},{y}!")

    def move(self,dir):
        if self.room.valid(self, dir):
            old_x, old_y = self.x, self.y
            if dir == "up":
                self.x, self.y = old_x, old_y - 1
            elif dir == "down":
                self.x, self.y = old_x, old_y + 1
            elif dir == "right":
                self.x, self.y = old_x + 1, old_y
            elif dir == "left":
                self.x, self.y = old_x - 1, old_y
    def position(self):
        return (self.x, self.y)
    
    def look(self):
        view = self.room.display()
        view[self.x][self.y] = '@'
        return view