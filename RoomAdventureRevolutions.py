###########################################################################################
# Name: Eric Pitts
# Date: 3/21/18
# Description: Room Adventure Revolutions
###########################################################################################
###IMPORTS#################################################################################
from Tkinter import *

###CLASSES#################################################################################
# the room class
class Room(object):
        #Constructor
        def __init__(self, name, image):
                # rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
                # (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
                # and grabbables (things that can be taken into inventory)
                self.name = name
                self.image = image
                self.exits ={}
                self.items = {}
                self.grabbables = []

        #Accessors and Mutators
        #name
        @property
        def name(self):
                return self._name

        @name.setter
        def name(self, value):
                self._name = value

        #image
        @property
        def image(self):
                return self._image

        @image.setter
        def image(self, value):
                self._image = value

        #exits
        @property
        def exits(self):
                return self._exits

        @exits.setter
        def exits(self, value):
                self._exits = value

        #items
        @property
        def items(self):
                return self._items

        @items.setter
        def items(self, value):
                self._items = value

        #grabbables
        @property
        def grabbables(self):
                return self._grabbables

        @grabbables.setter
        def grabbables(self, value):
                self._grabbables = value

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addExit(self, exit, room):
                # append the exit and room to the appropriate dictionary
                self._exits[exit] = room

        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
        def addItem(self, item, desc):
                # append the item and description to the appropriate dictionary
                self._items[item] = desc

        # adds a grabbable item to the room
        # the item is a string (e.g., key)
        def addGrabbable(self, item):
                # append the item to the list
                self._grabbables.append(item)

        # removes a grabbable item from the room
        # the item is a string (e.g., key)
        def delGrabbable(self, item):
                # remove the item from the list
                self._grabbables.remove(item)

        # returns a string description of the room
        def __str__(self):
                # first, the room name
                s = "You are in {}.\n".format(self.name)

                # next, the items in the room
                s += "You see: "
                for item in self.items.keys():
                        s += item + " "
                s += "\n"

                # next, the exits from the room
                s += "Exits: "
                for exit in self.exits.keys():
                        s += exit + " "

                return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
        #Constructor
        def __init__(self, parent):
                # call the constructor in the superclass
                Frame.__init__(self, parent)

        # creates the rooms
        def createRooms(self):
                #create room objects
                exercise = Room("Exercise Room", None)
                foyer = Room("Foyer", "room1.gif")
                garage = Room("Garage", None)
                kitchen = Room("Kitchen", None)
                living = Room("Living Room", None)
                laundry = Room("Launcdry Room", None)
                guest = Room("Guest Bedroom", None)
                bed = Room("Bedroom", None)
                bath = Room("Bathroom", None)
                secret = Room("Secret Room", None)

                #create room exits


                #create room items


                #create room grabbables

                #set foyer as current room at beginning of the game
                Game.currentRoom = foyer

                #initialize inventory
                Game.inventory = []
        
        # sets up the GUI
        def setupGUI(self):
                #organize the GUI
                self.pack(fill=BOTH, expand=1)

                #setup input box (Tkinter Entry)
                #binds return key to the process function
                #fills bottom row of GUI, is focused automatically
                Game.player_input = Entry(self, bg="white")
                Game.player_input.bind("<Return>", self.process)
                Game.player_input.pack(side=BOTTOM, fill=X)
                Game.player_input.focus()

                #setup image on left side (Tkinter label)
                #image doesn't determine widget size
                img = None
                Game.image = Label(self, width=WIDTH / 2, image=img)
                Game.image.image = img
                Game.image.pack(side=LEFT, fill=Y)
                Game.image.pack_propagate(False)

                #setup console output on right
                #text will be placed in a frame
                text_frame = Frame(self, width=WIDTH / 2)
                #Tkinter Text
                #disabled by default
                #widget doesn't control frame size
                Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
                Game.text.pack(fill=Y, expand=1)
                text_frame.pack(side=RIGHT, fill=Y)
                text_frame.pack_propagate(False)
                
        # sets the current room image
        def setRoomImage(self):
                if (Game.currentRoom == None):
                        #if dead, set to skull
                        Game.img = PhotoImage(file="skull.gif")
                else:
                        #otherwise set to image of current room
                        Game.img = PhotoImage(file=Game.currentRoom.image)

                #display the image on the left of GUI
                Game.image.config(image=Game.img)
                Game.image.image = Game.img
                
        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
                #enable text widget, clear it, set it, and disable it
                Game.text.config(state=NORMAL)
                Game.text.delete("1.0", END)
                if (Game.currentRoom == None):
                        #if dead, don't withold this vital information from the player and their loved ones
                        Game.text.insert(END, "You are dead. The only thing you can do now is quit.\n")
                else:
                        #otherwise, display status
                        Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(Game.inventory) + "\n\n" + status)
                        Game.text.config(state=DISABLED)

        # plays the game
        def play(self):
        # add the rooms to the game
                self.createRooms()
                # configure the GUI
                self.setupGUI()
                # set the current room
                self.setRoomImage()
                # set the current status
                self.setStatus("")

        # processes the player's input
        def process(self, event):
                #grab player input from input field
                action = Game.player_input.get()
                #set user input to lower case
                action = action.lower()
                #set default response
                response = "I don't understand. Try [verb][noun]. Valid verbs are go, look, and take."

                #exit game if player wants to quit (quit actions are "quit" or "exit"
                if (action == "quit" or action == "exit"):
                        exit(0)

                #if player is dead
                if (Game.currentRoom == None):
                        #clear player input
                        Game.player_input.delete(0, END)
                        return

                #split user input into words
                words = action.split()

                #the game only understands two word inputs
                if (len(words) == 2):
                        #isolate verb and noun
                        verb = words[0]
                        noun = words[1]

                        #if verb is go
                        if (verb == "go"):
                                #set default response
                                response = "Invalid exit."

                                #check for valid exits in current room
                                if (noun in Game.currentRoom.exits):
                                        #if room found, change currentRoom to specified room
                                        Game.cuurrentRoom =  Game.currentRoom.exits[noun]
                                        #set response if successful
                                        response = "Room changed."

                        #if verb is look
                        elif(verb == "look"):
                                #set default response
                                response = "I don't see that item."

                                #check for valid items in current room
                                if (noun in Game.currentRoom.items):
                                        #if found, set response to item description
                                        response = Game.currentRoom.items[noun]

                        #if verb is take
                        elif(verb == "take"):
                                #set a default response
                                response = "I don't see that item."

                                #check for valid grabbables in room
                                for grabbable in Game.currentRoom.grabbables:
                                        #if valid grabbable is found
                                        if (noun == grabbable):
                                                #add grabbable item to players inventory
                                                Game.inventory.append(grabbable)
                                                #remove grabbable from room
                                                Game.currentRoom.delGrabbable(grabbable)
                                                #set response if successful
                                                response = "Item grabbed."
                                                #no need to check for more grabbables
                                                break
                        #display response on right of GUI
                        #display room image on left of GUI
                        #clear input
                        self.setStatus(response)
                        self.setRoomImage()
                        Game.player_input.delete(0, END)
                
###FUNCTIONS################################################################################

###MAIN#####################################################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
