from tkinter import *
from operator import itemgetter,attrgetter
from tkinter.filedialog import askopenfilename
from tkinter import ttk

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
list_draw_edge = []
edge = []
list_read_node = []
count_readed_node = [0]
output_edge = []
node_set = set()

def paint(event):
	#python_green = "#476042"
	node = Node(event.x,event.y)
	node_set.add((int(node.x),int(node.y)))
	print(node_set)
	list_node.clear()
	for i in node_set:
		list_node.append(Node(int(i[0]),int(i[1])))
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
	x1, y1 = (int(edge.node1.x),int(edge.node1.y))
	x2, y2 = (int(edge.node2.x),int(edge.node2.y))
	x_mid = (x1+x2)/2
	y_mid = (y1+y2)/2
	if (x2-x1) == 0 and (y2-y1) != 0:
		return Edge(Node(0,(y2+y1)/2),Node(600,(y2+y1)/2))
	if (y2-y1) == 0 and (x2-x1) != 0:
		return Edge(Node((x2+x1)/2,0),Node((x2+x1)/2,600))
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
	list_draw_edge.clear()
	node_set.clear()

def draw_node():
	list_node.sort(key= lambda s: s.x)
	print("resorted!!")
	for i in list_node:
		x1, y1 = int(i.x)-1, int(i.y)-1
		x2, y2 = int(i.x)+1, int(i.y)+1
		w.create_oval(x1, y1, x2, y2, fill='black')
def draw_edge(edge):
	w.create_line(edge.node1.x, edge.node1.y, edge.node2.x, edge.node2.y)
	print("Edge plot: (" + str(edge.node1.x) + "," + str(edge.node1.y) + ") to (" + str(edge.node2.x) + "," + str(edge.node2.y) + ")")

def gen_edge(node):
	for i in range(0,len(list_node)-1):
		list_edge.append(Edge(node,list_node[i]))

def run():
	list_edge.clear()
	output_edge.clear()
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
	e1 = cal_distance(node1,node2)
	e2 = cal_distance(node2,node3)
	e3 = cal_distance(node1,node3)

	if e1 == e2+e3:
		return Node((node1.x+node2.x)/2,(node1.y+node2.y)/2)

	if e2 == e1+e3:
		return Node((node3.x+node2.x)/2,(node3.y+node2.y)/2)

	if e3 == e2+e1:
		return Node((node1.x+node3.x)/2,(node1.y+node3.y)/2)



	if node1.x == node2.x and node2.x == node3.x:
		return Node('-1','-1')
	if node1.y == node2.y and node2.y == node3.y:
		return Node('-1','-1')
	edge1 = plumb(Edge(node1,node2))
	edge2 = plumb(Edge(node1,node3))
	if edge1.node1.x == edge1.node2.x:
		a1 = 0
	else:
		a1 = (edge1.node1.y - edge1.node2.y)/(edge1.node1.x - edge1.node2.x)
	b1 = edge1.node1.y - (edge1.node1.x * a1)
	if edge2.node1.x == edge2.node2.x:
		a2 = 0
	else:
		a2 = (edge2.node1.y - edge2.node2.y)/(edge2.node1.x - edge2.node2.x)
	b2 = edge2.node1.y - (edge2.node1.x * a2)
	if a1 == a2:
		return Node(-1,-1)
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

	if node_cir.x != '-1':
		emax = max(e1,e2,e3)
		if e1 == emax:
			if e2+e3 < e1:
				edge1 = Edge(node_cir,Node(node1.x+600*(node_cir.x-node1.x),node1.y+600*(node_cir.y-node1.y)))
			elif e2+e3 == e1:
				edge1 = Edge(node_cir,Node(600*(node_cir.x-nodec.x),600*(node_cir.y-nodec.y)))
			else:
				edge1 = Edge(node_cir,Node(node1.x+600*(node1.x-node_cir.x),node1.y+600*(node1.y-node_cir.y)))
		else:
			edge1 = Edge(node_cir,Node(node1.x+600*(node1.x-node_cir.x),node1.y+600*(node1.y-node_cir.y)))
		if e2 == emax:
			if e1+e3 < e2:
				edge2 = Edge(node_cir,Node(node2.x+600*(node_cir.x-node2.x),node2.y+600*(node_cir.y-node2.y)))
			elif e1+e3 == e2:
				edge2 = Edge(node_cir,Node(600*(node_cir.x-nodea.x),600*(node_cir.y-nodea.y)))
			else:
				edge2 = Edge(node_cir,Node(node2.x+600*(node2.x-node_cir.x),node2.y+600*(node2.y-node_cir.y)))
		else:
			edge2 = Edge(node_cir,Node(node2.x+600*(node2.x-node_cir.x),node2.y+600*(node2.y-node_cir.y)))
		if e3 == emax:
			if e2+e1 < e3:
				edge3 = Edge(node_cir,Node(node3.x+600*(node_cir.x-node3.x),node3.y+600*(node_cir.y-node3.y)))
			elif e2+e1 == e3:
				edge3 = Edge(node_cir,Node(600*(node_cir.x-nodeb.x),600*(node_cir.y-nodec.y)))
			else:
				edge3 = Edge(node_cir,Node(node3.x+600*(node3.x-node_cir.x),node3.y+600*(node3.y-node_cir.y)))
		else:
			edge3 = Edge(node_cir,Node(node3.x+600*(node3.x-node_cir.x),node3.y+600*(node3.y-node_cir.y)))

		list_edge.append(edge1)
		list_edge.append(edge2)
		list_edge.append(edge3)
		list_edge.sort(key=attrgetter('node1.x','node1.y','node2.x','node2.y'))
		draw_edge(edge1)
		draw_edge(edge2)
		draw_edge(edge3)
		for i in list_edge:
			output_edge.append(i)



	else:
		emax = max(e1,e2,e3)
		if e1 == emax:
			print('')
		else:
			list_draw_edge.append(plumb(Edge(nodea,nodeb)))
		if e2 == emax:
			print('')
		else:
			list_draw_edge.append(plumb(Edge(nodeb,nodec)))
		if e3 == emax:
			print('')
		else:
			list_draw_edge.append(plumb(Edge(nodea,nodec)))
		for item in list_draw_edge:
			draw_edge(item)
			output_edge.append(item)


def draw_2point(nodea,nodeb):
	edge = plumb(Edge(nodea,nodeb))
	output_edge.append(edge)
	draw_edge(edge)
def cal_distance(node1,node2):
	x = (node1.x - node2.x) ** 2
	y = (node1.y - node2.y) **2
	return x + y

def r_test_file():
	clean()
	count_readed_node.clear()
	count_readed_node.append(0)
	node_set.clear()
	list_read_node.clear()
	filename = askopenfilename()
	read_node_num = 0
	print(filename)
	fp = open(filename,"r")
	lines = fp.readlines()
	fp.close()
	len_lines = len(lines)
	flag = 0
	count = 0
	for i in range(0,len_lines):
		if lines[i][0] == '0':
			break
		if lines[i][0] != "#" and lines[i][0] != '\n' and flag == 0:
			list_node.clear()
			node_set.clear()
			num = lines[i].split('\n',1)
			num_node = int(num[0])
			flag = num_node + 1
			for x in range(1,num_node+1):
				temp = lines[x+i].split(' ',2)
				temp1 = temp[1].split('\n',1)
				node_set.add((int(temp[0]),int(temp1[0])))
				#list_node.append(Node(int(temp[0]),int(temp1[0])))
			for j in node_set:
				list_node.append(Node(j[0],j[1]))
			temp = list_node.copy()

			list_read_node.append(temp)
		elif flag != 0:
			flag = flag - 1
	for i in range(len(list_read_node)):
		print("---------------------------------")
		for item in list_read_node[i]:
			print("("+str(item.x)+","+str(item.y)+")")
	draw_input(0)

def next_input():
	clean()
	if count_readed_node[0] < len(list_read_node) - 1:
		count_readed_node[0] = count_readed_node[0] + 1

	print(count_readed_node[0])
	draw_input(count_readed_node[0])

def previous_input():
	clean()
	if count_readed_node[0] > 0:
		count_readed_node[0] = count_readed_node[0] - 1

	print(count_readed_node[0])
	draw_input(count_readed_node[0])

def draw_input(c):
	list_node.clear()
	w.delete('all')
	for item in list_read_node[c]:
		list_node.append(item)
	for item in list_node:
		print("("+str(item.x)+","+str(item.y)+")")
	draw_node()

def output_file():
	out = open('out.txt',"w")
	list_node.sort(key=attrgetter('x','y'))
	output_edge.sort(key=attrgetter('node1.x','node1.y','node2.x','node2.y'))
	for i in list_node:
		out.write("P "+str(i.x)+" "+str(i.y)+"\n")

	for i in output_edge:
		out.write("E "+str(i.node1.x)+" "+str(i.node1.y)+" "+str(i.node2.x)+" "+str(i.node2.y)+"\n")

	out.close()


def r_graph():
	clean()
	filename = askopenfilename()
	f = open(filename,"r")
	lines = f.readlines()
	f.close()
	for i in lines:
		if i[0] == 'P':
			item = i.split(" ",2)
			list_node.append(Node(int(item[1]),int(item[2])))

		if i[0] == 'E':
			item = i.split(" ",4)
			list_draw_edge.append(Edge(Node(item[1],item[2]),Node(item[3],item[4])))
	for i in list_draw_edge:
		draw_edge(i)
	draw_node()

master = Tk()
master.title("Points")
master.resizable(0,0)
w = Canvas(master,width=canvas_width,height=canvas_height,bg='white')
w.pack(expand=YES, fill=BOTH)
w.bind("<ButtonRelease-1>", paint)

message = Label(master, text="Press and Drag the mouse to draw")
message.pack()

btn_clear = Button(master, text="clear",command=clean)
btn_clear.pack()

btn_run = Button(master, text="Run",command = run)
btn_run.pack()

btn_open_file = Button(master,text="Open",command = r_test_file)
btn_open_file.pack()

next_input = Button(master, text="next input", command = next_input)
next_input.pack()
previous_input = Button(master, text="previous input", command = previous_input)
previous_input.pack()

out_btn = Button(master,text='Output file',command = output_file)
out_btn.pack()

r_graph_btn = Button(master, text='Read Graph',command = r_graph)
r_graph_btn.pack()

mainloop()
