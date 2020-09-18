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
plumb_edge = []

def paint(event):
	python_green = "#476042"
	list_node.append(Node(event.x,event.y))
	#x1, y1 = (event.x - 1), (event.y - 1)
	#x2, y2 = (event.x + 1), (event.y + 1)
	#w.create_oval(x1, y1, x2, y2, fill=python_green)
	draw_node()
	print("x = "+str(list_node[len(list_node)-1].x)+",y = "+str(list_node[len(list_node)-1].y))
	#if len(list_node) > 1:
	#	gen_edge(list_node[len(list_node)-1])
	#	draw_node()
	#	for edge in list_edge:
	#		draw_plumb_edge(edge)

def plumb(edge):
	x1, y1 = (edge.node1.x,edge.node1.y)
	x2, y2 = (edge.node2.x,edge.node2.y)
	x_mid = (x1+x2)/2
	y_mid = (y1+y2)/2
	if (x2-x1) == 0 or (y2-y1) == 0:
		return Edge(Node(0,0),Node(0,0))
	old_k = (y2-y1)/(x2-x1)
	m = -(x2-x1)/(y2-y1)
	if m == 0:
		return Edge(Node(0,0),Node(0,0))
	b = y_mid - m*x_mid
	if (-b)/m < 0:
		node1 = Node(600,600*m+b)
	else:
		node1 = Node((-b)/m,0)
	if b < 0:
		node2 = Node((600-b)/m,600)
	else:
		node2 = Node(0,b)
	plumb_edge = Edge(node1,node2)
	return plumb_edge


def clean():
	w.delete('all')
	list_node.clear()
	list_edge.clear()

def draw_node():
	for i in range(0,len(list_node)):
		x1, y1 = (list_node[i].x-1), (list_node[i].y-1)
		x2, y2 = (list_node[i].x+1), (list_node[i].y+1)
		w.create_oval(x1, y1, x2, y2, fill='black')
	
def draw_plumb_edge(edge):
	plumb_edge = plumb(edge)
	w.create_line(plumb_edge.node1.x, plumb_edge.node1.y, plumb_edge.node2.x, plumb_edge.node2.y)
	print("Edge plot: (" + str(plumb_edge.node1.x) + "," + str(plumb_edge.node1.y) + ") to (" + str(plumb_edge.node2.x) + "," + str(plumb_edge.node2.y) + ")")

def gen_edge(node):
	for i in range(0,len(list_node)-1):
		list_edge.append(Edge(node,list_node[i]))

def run():
	list_edge.clear()
	print("clear the list_edge")
	for i in range(0,len(list_node)-1):
		for j in range(i+1,len(list_node)):
			list_edge.append(Edge(list_node[i],list_node[j]))
			draw_plumb_edge(list_edge[len(list_edge)-1])

master = Tk()
master.title("Points")
master.resizable(0,0)
w = Canvas(master,width=canvas_width,height=canvas_height,bg='white')
w.pack(expand=YES, fill=BOTH)
w.bind("<ButtonRelease-1>", paint)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)

btn_clear = Button(master, text="clear",command=clean)
btn_clear.pack()

btn_run = Button(master, text="Run",command = run)
btn_run.pack()

mainloop()
