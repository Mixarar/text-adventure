# Semester Project
A simple text adventure game with the following features implemented:
Fighting system, Inventory system, HP system, map movement system, moving and etc.

No requirements are needed, as stated in the requirements.txt
To start the game just run main.py
All of the commands that are needed to control the game are stated in the game itself.


## Classes and code structure:
I am using main.py for the main control over the map and where the main loop runs in.
I decided to split the functionality of classes in to different files, specificaly battle.py for the battle system, inventory.py for inventory and etc.
Each class is imported from it's file by the main python file that imports all other files.
I also made it modular, meaning that changing some logic in the inventory or in chests will be quite easy and would not require changing the logic in the whole code.
The map can be made to be randomly generated in the future as map creation is also done in the main.py without affecting anything in the objects.
Adding more NPCs or chests works similarly and does not require changing the code of the program, rather just the definitions in the main.py

## Example usage:
Try to walk around, maybe collect some items, fight NPCs dunno, anything. Start with command 'up', if you truly need help.