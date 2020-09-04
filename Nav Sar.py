from tkinter import *   
from PIL import ImageTk,Image
top = Tk()  
  
top.geometry("760x360")  

#creating a simple canvas  
c = Canvas(top,bg = "black",height = "760",width = 360)  
Photo = PhotoImage(file="nav.png")
PhotoImage = Label(image= Photo,bg = "black",height = "250",width = 318).place(x = 610,y = 120)
# imagewidth=sstreet.width(100)

def about():
    messagebox.showinfo("How To Play ?", "* Each player has 9 pieces, placed on the first 3 lines. First turn decided by toss.\n\n* Both players alternate their turns, to make a move tap on the piece that tap on theplace where you want to move.\n\n* A piece may move onto any vacount adjacent point along a line, A piece may capture an oppossing piece by short leap as in draughts.\n\n* The pice must be adjacent to the opposing piece, and leap over it onto a vacant point immediately beyond. The lap must be in straight line and follow the pattern on the board. Captures are not mandatory. A piece can turn. The capture piece (or pieces) is removed from the board.\n\n* The player who capture all of the other plyer's pieces wins 🏆🏆🏆🏆")



    
def window():
    global c
    global one
    global two
    top= Toplevel()
    top.title('Game Area') 
    c = Canvas(top,bg = "black",height = "760",width = 360)
    one = c.create_line(180,280,80,80,280,80,180,280,fill='blue',width=5)
    
    two = c.create_line(200,300,100,100,300,100,200,300,fill='red',width=5)
    
    
    yellowbutton = Button(top, text = "EXIT",command = exit_window,bg = "black",fg = "yellow", height = "1",width = 5 ).place(x = 590,y = 5)
    
    c.pack() 
    
    
    
    
def exit_window():
    global c
    top = Toplevel()
    top.title('Quit Window')
    c = Canvas(top,bg = "black",height = "760",width = 360)
    a = Label(top, text = 'QUIT',fg = "yellow",bg = "black",font =( 'Comic Sans MS', 50)).place(x = 659,y = 260)
    yellowbutton = Button(top, text = "YES",command = window, bg = "black" ,fg = "yellow", height = "1",width = 30).place(x = 656,y = 460)
    yellowbutton = Button(top, text = "NO", bg = "black" ,fg = "yellow", height = "1",width = 30).place(x = 656,y = 520)
    c.pack()
     
    
    
bluebutton = Button(top, text = "Single Player",command = window, bg = "black" ,fg = "yellow", height = "1",width = 30 ).place(x = 656,y = 460)
bluebutton = Button(top, text = "Multi Player", bg = "black" ,fg = "yellow", height = "1",width = 30 ).place(x = 656,y = 520)
bluebutton = Button(top, text = "Online Game", bg = "black" ,fg = "yellow", height = "1",width = 30 ).place(x = 656,y = 580)

bluebutton = Button(top, text = "Share", bg = "black" ,fg = "yellow", height = "1",width = 5 ).place(x = 656,y = 640)

bluebutton = Button(top, text = "About",command = about, bg = "black" ,fg = "yellow", height = "1",width = 5 ).place(x = 738,y = 640)

bluebutton = Button(top, text = "Setting", bg = "black" ,fg = "yellow", height = "1",width = 5 ).place(x = 832,y = 640)

Label(top, text = 'NAV SAR',fg = "yellow",bg = "black",font =( 
  'Comic Sans MS', 20, 'bold')).place(x = 700,y = 5)

   

c.pack()  
  
top.mainloop()
