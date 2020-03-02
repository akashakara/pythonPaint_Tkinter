import sys 
from Tkinter import *

canvas_width = 500
canvas_height = 150

def paint(event):
	     x1,y1 = (event.x-1),(event.y-1)
	     x2,y2 = (event.x-1),(event.y-1)
	     canvas1.create_oval(x1,y1,x2,y2,fill='red',outline='red' ,width=2)

root = Tk();
canvas1 = Canvas(root,width=canvas_width,height=canvas_height)
canvas1.pack(expand= YES,fill = BOTH)
canvas1.bind("<B1-Motion>",paint)

mainloop()
