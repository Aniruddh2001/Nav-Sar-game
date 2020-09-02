from tkinter import *   
  
top = Tk()  
  
top.geometry("760x360")  

#creating a simple canvas  
c = Canvas(top,bg = "black",height = "760",width = 360)  
# image = (popimage/PhotoImage)
# sstreet=Image.open("c://path")
# imagewidth=sstreet.width(100)
# photo = PhotoImage(file= 'C:\Users\aniru\OneDrive\Desktop')
def about():
    messagebox.showinfo("How To Play ?", "* Each player has 9 pieces, placed on the first 3 lines. First turn decided by toss.\n\n* Both players alternate their turns, to make a move tap on the piece that tap on theplace where you want to move.\n\n* A piece may move onto any vacount adjacent point along a line, A piece may capture an oppossing piece by short leap as in draughts.\n\n* The pice must be adjacent to the opposing piece, and leap over it onto a vacant point immediately beyond. The lap must be in straight line and follow the pattern on the board. Captures are not mandatory. A piece can turn. The capture piece (or pieces) is removed from the board.\n\n* The player who capture all of the other plyer's pieces wins 🏆🏆🏆🏆")
def window():
    wind = Toplevel(top)
    wind.geometry("760x360")

     
    # c = Canvas(top,bg = "black",height = "760",width = 360)
    
bluebutton = Button(top, text = "Single Player",command = window,fg = "blue", height = "1",width = 30 ).place(x = 656,y = 460)
bluebutton = Button(top, text = "Multi Player",fg = "blue", height = "1",width = 30 ).place(x = 656,y = 520)
bluebutton = Button(top, text = "Online Game",fg = "blue", height = "1",width = 30 ).place(x = 656,y = 580)

bluebutton = Button(top, text = "Share",fg = "blue", height = "1",width = 5 ).place(x = 656,y = 640)

bluebutton = Button(top, text = "About",command = about,fg = "blue", height = "1",width = 5 ).place(x = 738,y = 640)

bluebutton = Button(top, text = "Setting",fg = "blue", height = "1",width = 5 ).place(x = 832,y = 640)

Label(top, text = 'NAV SAR',fg = "white",bg = "black",font =( 
  'Comic Sans MS', 20)).place(x = 700,y = 5)

   

c.pack()  
  
top.mainloop()