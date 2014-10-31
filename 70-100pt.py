#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="light green")

# Create your "enemies" here, before the class
enemy1 = drawpad.create_rectangle(300,250,340,270, fill="light blue")
enemy1Speed = 5
enemy2Speed = 8
enemy3Speed = -3

enemy2 = drawpad.create_rectangle(400,350,440,370, fill="light pink")

enemy3 = drawpad.create_rectangle(740,50,800,70, fill="purple")

def enemy1Animation():
    global enemy1Speed
    x1, y1, x2, y2 = drawpad.coords(enemy1)
    if x2 > drawpad.winfo_width(): 
        drawpad.move(enemy1,-800,0)
    drawpad.move(enemy1,enemy1Speed,0)
    drawpad.after(1,enemy1Animation) 
enemy1Animation()

def enemy2Animation():
    global enemy2Speed
    x1, y1, x2, y2 = drawpad.coords(enemy2)
    if x2 > drawpad.winfo_width(): 
        drawpad.move(enemy2,-800,0)
    drawpad.move(enemy2,enemy2Speed,0)
    drawpad.after(1,enemy2Animation) 
enemy2Animation()

def enemy3Animation():
    global enemy3Speed
    x1, y1, x2, y2 = drawpad.coords(enemy3)
    if x2 < 0: 
        drawpad.move(enemy3,800,0)
    drawpad.move(enemy3,enemy3Speed,0)
    drawpad.after(1,enemy3Animation) 
enemy3Animation()

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    
       	    self.button1 = Button(self.myContainer1)
	    self.button1.configure(text="Left", background= "yellow")
	    self.button1.grid(row=0,column=1)
	    self.button1.bind("<Button-1>", self.button1Click)
	    
	    self.button2 = Button(self.myContainer1)
	    self.button2.configure(text="Right", background = "red")
	    self.button2.grid(row=0,column=2)
	    self.button2.bind("<Button-1>", self.button2Click)
	    
	    self.button3 = Button(self.myContainer1)
	    self.button3.configure(text="Down", background = "blue")
	    self.button3.grid(row=0,column=3)
	    self.button3.bind("<Button-1>", self.button3Click)
	    
		
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    	
		
	def button1Click(self, event):
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	def button2Click(self, event):
	   global oval
	   global player
	   drawpad.move(player,20,0)
	  
	def button3Click(self, event):
	   global oval
	   global player
	   drawpad.move(player,0,20)
	    
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
		
app = MyApp(root)
root.mainloop()