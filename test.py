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
edge = []

def paint(event):
	python_green = "#476042"
	node = Node(event.x,event.y)
	list_node.append(node)
	#x1, y1 = (event.x - 1), (event.y - 1)
	#x2, y2 = (event.x + 1), (event.y + 1)
	#w.create_oval(x1, y1, x2, y2, fill=python_green)
	draw_node()
	#print("x = "+str(node.x)+",y = "+str(node.y))
	#if len(list_node) > 1:
	#	gen_edge(list_node[len(list_node)-1])
	#	draw_node()
	#	for edge in list_edge:
	#		draw_edge(edge)

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
	edge = Edge(node1,node2)
	return edge


def clean():
	w.delete('all')
	list_node.clear()
	list_edge.clear()

def draw_node():
	list_node.sort(key= lambda s: s.x)
	print("resorted!!")
	for i in range(0,len(list_node)):
		print("x = "+str(list_node[i].x)+",y = "+str(list_node[i].y))
		x1, y1 = (list_node[i].x-1), (list_node[i].y-1)
		x2, y2 = (list_node[i].x+1), (list_node[i].y+1)
		w.create_oval(x1, y1, x2, y2, fill='black')
	
def draw_edge(edge):
	w.create_line(edge.node1.x, edge.node1.y, edge.node2.x, edge.node2.y)
	print("Edge plot: (" + str(edge.node1.x) + "," + str(edge.node1.y) + ") to (" + str(edge.node2.x) + "," + str(edge.node2.y) + ")")

def gen_edge(node):
	for i in range(0,len(list_node)-1):
		list_edge.append(Edge(node,list_node[i]))

def run():
	list_edge.clear()
	print("clear the list_edge")
	if len(list_node) == 2:
		draw_2point(list_node[0],list_node[1])
	elif len(list_node) == 3:
	
		for i in range(0,len(list_node)-2):
			for j in range(i+1,len(list_node)-1):
				for k in range(j+1,len(list_node)):
					draw_3point(list_node[i],list_node[j],list_node[k])
					node = cal_Circumscribed(list_node[i],list_node[j],list_node[k])
					w.create_oval(node.x-5,node.y-5,node.x+5,node.y+5,fill="red")
			#list_edge.append(Edge(list_node[i],list_node[j]))
			#draw_edge(list_edge[len(list_edge)-1])

def cal_Circumscribed(node1,node2,node3):
	edge1 = plumb(Edge(node1,node2))
	edge2 = plumb(Edge(node1,node3))
	a1 = (edge1.node1.y - edge1.node2.y)/(edge1.node1.x - edge1.node2.x)
	b1 = edge1.node1.y - (edge1.node1.x * a1)
	a2 = (edge2.node1.y - edge2.node2.y)/(edge2.node1.x - edge2.node2.x)
	b2 = edge2.node1.y - (edge2.node1.x * a2)
	node = Node((b2-b1)/(a1-a2),a1*(b2-b1)/(a1-a2)+b1)
	return node

def draw_3point(nodea,nodeb,nodec):
	node_cir = cal_Circumscribed(nodea,nodeb,nodec)
	node1 = Node((nodea.x+nodeb.x)/2,(nodea.y+nodeb.y)/2)
	node2 = Node((nodec.x+nodeb.x)/2,(nodec.y+nodeb.y)/2)
	node3 = Node((nodea.x+nodec.x)/2,(nodea.y+nodec.y)/2)

	e1 = cal_distance(nodea,nodeb)
	e2 = cal_distance(nodeb,nodec)
	e3 = cal_distance(nodea,nodec)

	emax = max(e1,e2,e3)
	if e1 == emax:
		if e2+e3 < e1:
			edge1 = Edge(node_cir,Node(node1.x+600*(node_cir.x-node1.x),node1.y+600*(node_cir.y-node1.y)))
		else:
			edge1 = Edge(node_cir,Node(node1.x+600*(node1.x-node_cir.x),node1.y+600*(node1.y-node_cir.y)))
	else:
		edge1 = Edge(node_cir,Node(node1.x+600*(node1.x-node_cir.x),node1.y+600*(node1.y-node_cir.y)))

	if e2 == emax:
		if e1+e3 < e2:
			edge2 = Edge(node_cir,Node(node2.x+600*(node_cir.x-node2.x),node2.y+600*(node_cir.y-node2.y)))
		else:
			edge2 = Edge(node_cir,Node(node2.x+600*(node2.x-node_cir.x),node2.y+600*(node2.y-node_cir.y)))
	else:
		edge2 = Edge(node_cir,Node(node2.x+600*(node2.x-node_cir.x),node2.y+600*(node2.y-node_cir.y)))

	if e3 == emax:
		if e2+e1 < e3:
			edge3 = Edge(node_cir,Node(node3.x+600*(node_cir.x-node3.x),node3.y+600*(node_cir.y-node3.y)))
		else:
			edge3 = Edge(node_cir,Node(node3.x+600*(node3.x-node_cir.x),node3.y+600*(node3.y-node_cir.y)))
	else:
		edge3 = Edge(node_cir,Node(node3.x+600*(node3.x-node_cir.x),node3.y+600*(node3.y-node_cir.y)))


	draw_edge(edge1)
	draw_edge(edge2)
	draw_edge(edge3)

def draw_2point(nodea,nodeb):
	edge = plumb(Edge(nodea,nodeb))
	draw_edge(edge)
	
def cal_distance(node1,node2):
	x = (node1.x - node2.x) ** 2
	y = (node1.y - node2.y) **2
	return x + y

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
