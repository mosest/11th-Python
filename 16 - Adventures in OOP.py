#Tara Moses
#Assignment 16: Adventures in OOP
#April 10, 2013

class Room:
    def __init__(self,title,description,coin_message=None):
        self.title=title
        self.description=description
        self.coin_message=coin_message
        
        self.north=None
        self.south=None
        self.west=None
        self.east=None

        self.hasBeenVisited=False

    def visit(self):
        print "You walk into "+self.title+". "+self.description
        if self.coin_message!=None:
            print self.coin_message
        direction=raw_input("Which way next? ")

        if direction=="south" and self.south==bus and guest_bed.hasBeenVisited==True and attic.hasBeenVisited==True and library.hasBeenVisited==True and study.hasBeenVisited==True and master_bed.hasBeenVisited==True:
            print "Yay! You finally have enough change! You made it to the bus! Thanks for playing."
            return
        
        if direction=="east" and self.east:
            self.east.hasBeenVisited=True
            self.east.visit()
            return
        elif direction=="west" and self.west:
            self.west.hasBeenVisited=True
            self.west.visit()
            return
        elif direction=="north" and self.north:
            self.north.hasBeenVisited=True
            self.north.visit()
            return
        elif direction=="south" and self.south:
            self.south.hasBeenVisited=True
            self.south.visit()
            return
        else:
            print "You walk into a wall. Dazed, you turn around and kick yourself for being so stupid."
            self.visit()
            return
        
#create rooms
master_bed=Room("the master bedroom","You check the 'savings' jar in your sock drawer.","You found two quarters and a penny.")
bath=Room("the bathroom","You wonder if there's anything in the medicine cabinet.","Nope, not one coin.")
narnia=Room("Narnia","What the fuck? Severely freaked out, you mug some half-horse dude offering you tea and get the hell out of there.","All he had on him was a weird flute.")
closet=Room("the coat closet","You rifle through the pockets of your old jackets. Nothing.",)
study=Room("the study","You rifle through the pages of the unfinished manuscript on your desk.","You found a penny! ...No, wait, it's a dime! That needs washing!")
library=Room("the library","You see a shiny something in the finance bookshelf! You knew buying those self-help books was a good idea.","You found a John Adams dollar!")
kitchen=Room("the kitchen","Nothing to check here; you keep it too tidy.","You grab a bottle of juice and move on.")
living_room=Room("the living room","You found something under the tv set!","It's... a dead spider and a hairball.")
attic=Room("the attic","You completely forgot about this place! You check under the cushions of the couch in the corner.","Two nickels and a dime!")
torture_room=Room("the torture room","No coins here.")
south_hall=Room("the south hallway","Nothing here but the door that leads outside.")
sunroom=Room("the sunroom","Nothing to check here.")
guest_bed=Room("the guest bedroom","You check the dresser.","Three pennies! Neato.")
bus=Room("the bus stop","The sign reads, 'exact change only'.")

master_bed.south=study
master_bed.east=bath
bath.west=master_bed
bath.east=guest_bed
study.north=master_bed
study.south=library
study.west=attic
study.east=living_room
library.north=study
library.west=attic
attic.north=study
attic.east=library

guest_bed.north=torture_room
guest_bed.west=bath
guest_bed.east=closet
closet.west=guest_bed
closet.east=narnia
narnia.west=closet

kitchen.south=living_room
living_room.north=kitchen
living_room.west=study
living_room.east=torture_room
living_room.south=south_hall
torture_room.west=living_room
torture_room.east=guest_bed
south_hall.north=living_room
south_hall.east=sunroom
south_hall.south=bus
bus.north=south_hall
sunroom.west=south_hall


#start program
print "You need $1.84 for bus fare, but the driver only takes exact change!"
print "You decide to collect spare change lying around the house. Good luck!\n"
master_bed.visit()
