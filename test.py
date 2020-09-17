from tkinter import *

class Node:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Edge:
	def __init__(self,node1,node2):
		self.node1 = node1
		self.node2 = node2

canvas_width = 600
canvas_height = 600
list_node = []
list_edge = []

def paint(event):
    python_green = "#476042"
    list_node.append(Node(event.x,event.y))
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_green)
    print("x = "+str(list_node[len(list_node)-1].x)+",y = "+str(list_node[len(list_node)-1].y))
    if len(list_node) > 1:
	    list_edge.append(Edge(list_node[len(list_node)-2],list_node[len(list_node)-1]))
	    w.create_line(list_edge [len ( list_edge) - 1].node1.x,list_edge[len(list_edge)-1].node1.y,list_edge[len(list_edge)-1].node2.x,list_edge[len(list_edge)-1].node2.y)
	    print("Edge append: (" + str( list_edge [len ( list_edge) - 1].node1.x) + "," + str(list_edge[len(list_edge)-1].node1.y) + "),(" + str(list_edge[len(list_edge)-1].node2.x) + "," + str(list_edge[len(list_edge)-1].node2.y) + ")")

master = Tk()
master.title("Points")
master.resizable(0,0)
w = Canvas(master,
           width=canvas_width,
           height=canvas_height,bg='white')
w.pack(expand=YES, fill=BOTH)
w.bind("<ButtonRelease-1>", paint)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

btn = Button(master, text="btn")
btn.pack()

mainloop()
