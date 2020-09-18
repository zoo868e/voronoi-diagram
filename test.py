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
		plot = plumb(list_edge[len(list_edge)-1])
		w.create_line(plot.node1.x,plot.node1.y,plot.node2.x,plot.node2.y)
		print("Edge plot: (" + str(plot.node1.x) + "," + str(plot.node1.y) + ") to (" + str(plot.node2.x) + "," + str(plot.node2.y) + ")")
		#w.create_line(list_edge [len ( list_edge) - 1].node1.x,list_edge[len(list_edge)-1].node1.y,list_edge[len(list_edge)-1].node2.x,list_edge[len(list_edge)-1].node2.y)
		#print("Edge append: (" + str( list_edge [len ( list_edge) - 1].node1.x) + "," + str(list_edge[len(list_edge)-1].node1.y) + "),(" + str(list_edge[len(list_edge)-1].node2.x) + "," + str(list_edge[len(list_edge)-1].node2.y) + ")")

def plumb(edge):
	x1, y1 = (edge.node1.x,edge.node1.y)
	x2, y2 = (edge.node2.x,edge.node2.y)
	x_mid = (x1+x2)/2
	y_mid = (y1+y2)/2
	old_k = (y2-y1)/(x2-x1)
	m = -(x2-x1)/(y2-y1)
	b = y_mid - m*x_mid
	node1 = Node((-b)/m,0)
	node2 = Node(0,b)
	plumb_edge = Edge(node1,node2)
	return plumb_edge

master = Tk()
master.title("Points")
master.resizable(0,0)
w = Canvas(master,width=canvas_width,height=canvas_height,bg='white')
w.pack(expand=YES, fill=BOTH)
w.bind("<ButtonRelease-1>", paint)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

btn = Button(master, text="btn")
btn.pack()

mainloop()
