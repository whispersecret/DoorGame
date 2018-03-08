import tkinter
from tkinter import *

#only press return once
okToPressReturn = True

#the player's attributes.
health = 100

inventory = []
rooms = {   
            0 : {"name" : "Haunted Castle",
                 
                 "Go Inside": 1},
           1 : {"name" : "Room of Darkness",
                 "east" : 2,
                 "south": 3,
                 "item" : "Sword of Bleeding Hearts" },
            2: {"name" : "Corridor of Odysseys",
                "west" : 1,
                "south" : 3,
                "item" : "Heart of the Wizard" },
            3: {"name" : "Garden of Illusions",
                "north" : 2,
                "south": 4,
                "item" : "Mirror of Truth" },
            4 : { "name" : "Kitchen of Eternal Silence",
                  "north" : 3,
                  "west": 5,
                  "south" : 6,
                  "item" : "Knife of Life and Strife" },
            5 : {"name" : "Cinema of Ghosts",
                 "east" : 4,
                 "item" : "Camera of Time Travel" },
            6 : {"name" : "Virtual Reality Maze",
                 "north" : 4,
                 "east" : 7,
                 "item" : "girl from Big Bang Theory" },
            7 : {"name" : "Mermaid Pool",
                 "west" : 6,
                 "item" : "Mirror of Escape" }, 

            }


currentRoom = 0





#-------------------------------------------------------------------

def startGame(event):

    global okToPressReturn

    if okToPressReturn == False:
        pass    
        
    
    else:
        #update the time left label.
  
        #start updating the values
        updateHealth()
       
        updateDisplay()
        

        #startLabel = tkinter.Label(root, text=" ", font=('Helvetica', 12))
        
        okToPressReturn = False

#-------------------------------------------------------------------


def updateDisplay():

    #use the globally declared variables above.
    global health
    
    


    
    #update the time left label.
    healthLabel.config(text="health: " + str(health))
    

    startLabel = tkinter.Label(root, text="Press 'Enter' to start playing!", font=('Helvetica', 12))
    

   

#-------------------------------------------------------------------

def updateHealth():

    #use the globally declared variables above.
    global health

    #decrement the hunger.
    health -= 1

    if isAlive():
        #run the function again after 500ms.
        healthLabel.after(1000, updateHealth)
        healthLabel.after(100, updateDisplay)

#-------------------------------------------------------------------

def isAlive():

    global health
    
    if health <= 0 and len(inventory) < 7:
        #update the start info label.
        startLabel.config(text="GAME OVER!")     
        return False
    else:
        return True
        
#-------------------------------------------------------------------
def moveTo():
    global health
    global rooms
    global currentRoom

    move = ent.get()
    
    if move in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][move]
        roomLabel.config(text = "You are in the " + rooms[currentRoom]["name"] + ". You see the " + rooms[currentRoom]["item"] )
        if rooms[currentRoom]["name"] == "Corridor of Odysseys":
            bedPic.config(image = corridorphoto)
        if rooms[currentRoom]["name"] == "Room of Darkness":
            bedPic.config(image = bedphoto)
        if rooms[currentRoom]["name"] == "Garden of Illusions":
            bedPic.config(image = gardenphoto)
        if rooms[currentRoom]["name"] == "Kitchen of Eternal Silence":
            bedPic.config(image = kitchenphoto)
        if rooms[currentRoom]["name"] == "Cinema of Ghosts":
            bedPic.config(image = cinemaphoto)
        if rooms[currentRoom]["name"] == "Virtual Reality Maze":
            bedPic.config(image = mazephoto)
        if rooms[currentRoom]["name"] == "Mermaid Pool":
            bedPic.config(image = mermaidphoto)
           
           
    else:
        roomLabel.config(text ="You can't go that way!")

#-------------------------------------------------------------------
def toTake():
    global health
    global rooms
    global currentRoom
    global inventory

    item = ent2.get()
    
    if item in rooms[currentRoom]["item"]:
        inventory += rooms[currentRoom]["item"]
        itemLabel.config(text = "You have retrived the " + rooms[currentRoom]["item"])

    else:
        itemLabel.config(text ="Cannot retrive " + item + "!")


root = tkinter.Tk()
#set the title.
root.title("Haunted Caste")
#set the size.
root.geometry("700x800")
root.configure(background="grey")


startLabel = tkinter.Label(root, text="You are at the Haunted Castle. Press enter and 'Go Inside' if you want to live...", font=('Helvetica', 12), bg="grey")
startLabel.pack()

healthLabel = tkinter.Label(root, text="health: " + str(health), font=('Helvetica', 12), bg="grey")
healthLabel.pack()

lbl = tkinter.Label(root, text ="Where would you like to go?", font=('Helvetica', 12), bg="grey")
lbl.pack()
ent = tkinter.Entry(root)
ent.pack()
btn = tkinter.Button(root, text="Button", command=moveTo, bg="grey")
btn.pack()

lbl2 = tkinter.Label(root, text ="What would you like to take?", font=('Helvetica', 12), bg="grey")
lbl2.pack()
ent2 = tkinter.Entry(root)
ent2.pack()
btn2 = tkinter.Button(root, text="Enter", command=toTake, bg="grey")
btn2.pack()
root.bind('<Return>', startGame)

roomLabel = tkinter.Label(root, text="You are in the " + rooms[currentRoom]["name"], font=('Helvetica', 16), bg="grey")
roomLabel.pack()
itemLabel = tkinter.Label(root, text=" ", font=('Helvetica', 16), bg="grey")
itemLabel.pack()


housephoto = tkinter.PhotoImage(file="hauntedhouse.gif")
bedphoto = tkinter.PhotoImage(file="scaryroom.gif")
corridorphoto = tkinter.PhotoImage(file="corridor.gif")
gardenphoto = tkinter.PhotoImage(file="garden.gif")
kitchenphoto = tkinter.PhotoImage(file="kitchen.gif")
cinemaphoto = tkinter.PhotoImage(file="cinema.gif")
mazephoto = tkinter.PhotoImage(file="maze.gif")
mermaidphoto = tkinter.PhotoImage(file="mermaid.gif")

bedPic = tkinter.Label(root, image=housephoto)
bedPic.pack()





#start the GUI
root.mainloop()

#startLabel = tkinter.Label(root, text=" ", font=('Helvetica', 12))

