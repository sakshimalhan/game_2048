import random
def start():
	grid=[[0 for i in range(4)] for j in range(4)]
	random_generator(grid)
	random_generator(grid)
	return grid



def random_generator(grid):
	x=random.randint(0,3)
	y=random.randint(0,3)
	while (grid[x][y]!=0):
		x=random.randint(0,3)
		y=random.randint(0,3)
	grid[x][y]=2
	return grid


def check_curr_state(grid):
	for i in range(4):
		for j in range(4):
			if (grid[i][j]==16):
				return "WON!"
	for i in range(4):
		for j in range(4):
			if (grid[i][j]==0):
				return "continue"
	for i in range(3):
		for j in range(3):
			if(grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1]):
				return "continue"
		for j in range(3):
			if(grid[3][j]==grid[3][j+1]):
				return "continue"
		for i in range(3):
			if(grid[i][3]==grid[i+1][3]):
				return "continue"	
	return "LOST"
def transpose(grid):
	for i in range(4):
		for j in range(4):
			if(i>j):
				grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
			
def reverse(grid):
	for i in range(4):
		for j in range(2):
			grid[i][j],grid[i][3-j]=grid[i][3-j],grid[i][j]


def move(grid):
	flag=False
	arr=[]
	for i in range(4):
		k=0
		for j in range(4):
			if(grid[i][j]!=0):
				arr.append(grid[i][j])

		j=0
		k=0
		while(k<len(arr)-1):
			if(arr[k]!=arr[k+1]):
				if(arr[k]!=grid[i][j]):
					flag=True
				grid[i][j]=arr[k]
				j+=1
				k+=1
			else:
				grid[i][j]=2*arr[k]
				flag=True
				j+=1
				k=k+2
		if(k<len(arr)):
			if(arr[k]!=grid[i][j]):
					flag=True
			grid[i][j]=arr[k]
			j+=1
		while(j<4):
			grid[i][j]=0
			j+=1
		arr.clear()			
	return flag		
		
def move_left(grid):
	flag=move(grid)
	if flag:
		random_generator(grid)

	return grid	

def move_right(grid):
	reverse(grid)
	flag=move(grid)
	reverse(grid)
	if flag:
		random_generator(grid)
	return grid		

def move_up(grid):
	transpose(grid)
	flag=move(grid)
	transpose(grid)
	if flag:
		random_generator(grid)	
	return grid	

def move_down(grid):
	transpose(grid)
	reverse(grid)
	
	flag=move(grid)
	reverse(grid)
	transpose(grid)
	if flag:
		random_generator(grid)	
	return grid	

	




	

