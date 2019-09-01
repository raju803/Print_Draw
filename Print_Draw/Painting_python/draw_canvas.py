from tkinter import *

def paint(event):
    color='green'
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    c.create_oval(x1,y1,x2,y2,fill=color,outline=color)

master = Tk()
master.title("Painting in Python")
message1=Label(master,text='Developer By Raju......')
message1.pack(side=TOP)

c=Canvas(master,width=600,height=450,bg='white')
c.pack(expand=YES,fill=BOTH)
c.bind('<B1-Motion>',paint)

message=Label(master,text='Press and Drag to draw')
message.pack(side=BOTTOM)

master.mainloop()
