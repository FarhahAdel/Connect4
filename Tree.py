from functions import *
class Node:
    def __init__(self,state , depth,parent):
        self . state = state 
        self.depth = depth
        self.children = []
        self.parent = parent
        self .score = 0
        self.column = 0

tree = list()
def expandTree(board,depth):

	root = Node(board , 0,None)
	tree.append(root)
	validLocations = get_valid_locations(root.state)
	
	for location in validLocations :
			row = get_next_open_row(root.state,location)
			copyBoard = root.state.copy()
			drop_piece(copyBoard, row,location, ai.getPiece())
			childNode = Node(copyBoard ,1,root)
			childNode.column = location
			root.children.append(childNode)
			tree.append(childNode)
			
	turn = player.getTurn()
	
	newNode = tree[1]

	validLocations = get_valid_locations(newNode.state)
	children = len(tree)-1
	d = 2
	i = 1
	j = 0
	for v in range (1,depth):
		while children :
			valid = 0
			for location in validLocations :
				valid = 1
				row = get_next_open_row(newNode.state,location)
				copyBoard = newNode.state.copy()
				if turn == player.getTurn():
					drop_piece(copyBoard, row,location, player.getPiece())
				else :
					drop_piece(copyBoard, row,location, ai.getPiece())
				childNode = Node(copyBoard ,d,newNode)
				childNode.column = location
				newNode.children.append(childNode)
				tree.append(childNode)
				j = j+1
			# print("I==",i)
			if valid :
				i = i+1
			else :
				return root
			newNode = tree[i]
			validLocations = get_valid_locations(newNode.state)
			children = children - 1
		d = d+1
		if turn == ai.getTurn() :
			turn = player.getPiece()
		else :
			turn = ai.getTurn()
		children = j
		j = 0

	return root 


def setScores(depth):
	for node in tree:
		if node.depth == depth:
			# print_board(node.state)
			
				node.score = score_position(node.state,ai.getPiece())

	i = len(tree)-1
	while i >=0 :
		node = tree[i]
		i = i-1
		if node.depth != depth :
			if node.depth % 2 ==0:
				node.score = -math.inf
			else :
				node.score = math.inf
		
			for child in node.children:
				
				if node.depth %2 == 0:
					if node.score < child.score :
						node.score = child.score 
				
				else :
				
					if node.score > child.score :
						node.score = child.score 
			# print("FINAL SCORE = ",node.score)
	  
def clearFile():
		f = open("C:/Users/hania/Downloads/assignment2-FinalEdit/assignment2/output.txt", "w")
		f.close()	  

def now():
	clearFile()
	f = open("C:/Users/hania/Downloads/assignment2-FinalEdit/assignment2/output.txt", "a")
	d = 0
	k =0
	neighbours = 0
	parent = tree[0]
	f.write("--------MINIMAX TREE----------")
	f.write("\n")
	print("-------------MINIMAX TREE-------------")
	for i in range(0,len(tree)):
	
		if tree[i].depth == 0:
			f.write("-------------LEVEL 0-------------")
			f.write("\n")
		
			# print(tree[i].score)
			f.write(str(tree[i].score))
			f.write("\n")
			
	
		elif tree[i].depth == d :
			
			if neighbours == 0:
				f.write("\t\t")
				neighbours = len(tree[i].parent.children)
		    
			f.write(str(tree[i].score))
			f.write("(")
			f.write(str(tree[i].column))
			f.write(")")
			f.write(" ")
			neighbours = neighbours -1
			
			# k = k+1
			# if k == 7:
			# 	f.write("\n")
			# 	k =0
			
		else :
		    
			# k = 1
			f.write("\n")
			f.write("--------LEVEL ")
			f.write(str(d+1))
			f.write("-----------------")
			f.write("\n")
			d = d+1
			# print("\n")
			f.write("\n")
			
			f.write(str(tree[i].score))
			f.write("(")
			f.write(str(tree[i].column))
			f.write(")")
			f.write(" ")
			neighbours = len(tree[i].parent.children)-1
			# print("N= ",neighbours)
	
		
	# print("\n")
	f.close()
	
