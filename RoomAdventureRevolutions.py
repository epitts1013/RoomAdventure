###########################################################################################
# Name: Eric Pitts
# Date: 3/21/18
# Description: Room Adventure Revolutions
###########################################################################################
###IMPORTS#################################################################################
from Tkinter import *

###CLASSES#################################################################################
# the room class
# serves as template for individual rooms
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
        # the exit is a string (e.g., "north")
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

# the event class
# serves as a template for [use] events
# accepts the room, trigger item, item trigger is used on, and a string that will be executed when the event is called
class Event(object):
        #Constructor
        def __init__(self, location, trigger, dObject, effect):
              self.location = location #the room the event occurs in
              self.trigger = trigger #item used to trigger event
              self.dObject = dObject #item in room that trigger is used on
              self.effect = effect #effect of the action written as a string

        #accessors and mutators
        #location
        @property
        def location(self):
                return self._location

        @location.setter
        def location(self, val):
                self._location = val

        #triggerItem
        @property
        def trigger(self):
                return self._trigger

        @trigger.setter
        def trigger(self, val):
                self._trigger = val

        #dObject
        @property
        def dObject(self):
                return self._dObject

        @dObject.setter
        def dObject(self, val):
                self._dObject = val

        #effect
        @property
        def effect(self):
                return self._effect

        @effect.setter
        def effect(self, val):
                self._effect = val

# the game class
# inherits from the Frame class of Tkinter
# sets up game and GUI
class Game(Frame):
        #Constructor
        def __init__(self, parent):
                # call the constructor in the superclass
                Frame.__init__(self, parent)

        # creates the rooms
        def createRooms(self):
                #create room objects
                front = Room("Front Yard", "front.gif")
                exercise = Room("Exercise Room", "exercise.gif")
                foyer = Room("Foyer", "foyer.gif")
                garage = Room("Garage", "garage.gif")
                kitchen = Room("Kitchen", "kitchen.gif")
                living = Room("Living Room", "living.gif")
                laundry = Room("Laundry Room", "laundry.gif")
                guest = Room("Guest Bedroom", "guest.gif")
                bed = Room("Bedroom", "bed.gif")
                bath = Room("Bathroom", "bath.gif")
                secret = Room("Secret Room", "secret.gif")

                #create room exits
                exercise.addExit("north", kitchen)
                exercise.addExit("east", foyer)

                foyer.addExit("north", living)
                foyer.addExit("west", exercise)

                garage.addExit("north", laundry)

                kitchen.addExit("north", guest)
                kitchen.addExit("east", living)
                kitchen.addExit("south", exercise)

                living.addExit("north", bed)
                living.addExit("east", laundry)
                living.addExit("south", foyer)
                living.addExit("west", kitchen)

                laundry.addExit("north", bath)
                laundry.addExit("south", garage)
                laundry.addExit("west", living)

                guest.addExit("south", kitchen)

                bed.addExit("south", living)
                bed.addExit("east", bath)

                bath.addExit("south", laundry)
                bath.addExit("west", bed)

                #create room items
                exercise.addItem("weight-rack", "A rack with several dumbells of various weights placed on it.")
                exercise.addItem("treadmill", "A ten speed treadmill with incline controls.")
                exercise.addItem("elliptical", "Simulates walking up stairs without the high impact.")
                exercise.addItem("punching-bag", "For when you need to let all that anger out. A few pairs of boxing gloves sit next to it.")
                exercise.addItem("mini-fridge", "It's full of Gatorade.")
                exercise.addItem("scale", "For weighing yourself after exercise, not that there is any immediate effect. I wonder how much the dumbells weigh?")

                foyer.addItem("rug", "It's fairly plush under your feet.")
                foyer.addItem("door-mat", "It's covered in dirt, I suppose that is its purpose.")
                foyer.addItem("door", "It's where you came in from, but you shouldn't leave yet.")

                garage.addItem("car", "It's a Dodge Charger.")
                garage.addItem("truck", "It's a Dodge Ram.")
                garage.addItem("work-bench", "It has several tools on it, like hammers and wrenches.")
                garage.addItem("breaker-box", "Contains several switches for controlling the power.")
                garage.addItem("garage-door", "It seems to be locked tight, not getting out this way.")

                kitchen.addItem("table", "A dining table, with several dishes on it. A ham rests on top of it.")
                kitchen.addItem("ham", "A smoked ham. A knife rests next to it, perhaps you could cut off a piece.")
                kitchen.addItem("fridge", "A refrigerator full of boring foods.")
                kitchen.addItem("oven", "An electric oven, looks like it has been recently used.")
                kitchen.addItem("stove", "An electric stove.")

                living.addItem("sofa", "A comfy sofa, it sits in front of the fireplace.")
                living.addItem("fireplace", "A fire burns, it casts a warm glow across the room.")
                living.addItem("television", "A 32\" flatscreen. A remote rests in front of it.")
                living.addItem("recliner", "A La-Z-Boy recliner, looks comfortable.")
                living.addItem("floor-rug", "Covers a large portion of the floor, but I don't care for the color.")
                living.addItem("dvd-rack", "Has a wide array of movies, one dvd looks more important though.")

                laundry.addItem("washing-machine", "A front loading washing machine with a clear window. Its fun to watch these things sometimes.")
                laundry.addItem("dryer", "Used for drying clothes. Loud. Less fun to watch than a washing machine.")
                laundry.addItem("laundry-basket", "Could be used to hold clothes, but the clothes are in the washer already.")
                laundry.addItem("shelf", "Shelves many items, such as detergent.")

                guest.addItem("bed", "A comfy looking double bed with two pillows.")
                guest.addItem("dresser", "A dresser with clothes in it and a mirror on top.")
                guest.addItem("coat-rack", "A lone jacket rests on it, a key sits in the pocket.")
                guest.addItem("tv", "A small box television, nothing fancy.")

                bed.addItem("bed", "A bed in the bedroom, who would have guessed?")
                bed.addItem("wardrobe", "Full of clothes.")
                bed.addItem("ceiling-fan", "Large, spinning, wooden blades for moving the air around.")
                bed.addItem("desk", "Contains papers and writing utinsils. On the top rests a laptop, but the battery is dead.")
                bed.addItem("safe", "A locked safe.")
                bed.addItem("night-stand", "A lamp rests on top, in the drawer is a battery.")

                bath.addItem("toilet", "An uninspired, white, porcelain bowl full of water and [expletive].")
                bath.addItem("shower", "A shower sounds nice, but God only knows how to operate this thing.")
                bath.addItem("sink", "It seems to be clogged.")

                #create room grabbables
                exercise.addGrabbable("boxing-gloves")
                exercise.addGrabbable("dumbell")
                exercise.addGrabbable("gatorade")

                garage.addGrabbable("hammer")
                garage.addGrabbable("wrench")

                kitchen.addGrabbable("knife")

                living.addGrabbable("remote")
                living.addGrabbable("dvd")

                laundry.addGrabbable("detergent")

                guest.addGrabbable("key")

                bed.addGrabbable("battery")

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
                                        Game.currentRoom =  Game.currentRoom.exits[noun]
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
