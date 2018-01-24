a = [2,2,2,2,2,2,2,2,2]
flag = 0
pos = 0
counter = 0
p1 = 0

def board2():
	#print("flag: ",flag)
	print()
	print(a[6],' ',a[7],' ',a[8])
	print(a[3],' ',a[4],' ',a[5])
	print(a[0],' ',a[1],' ',a[2])
	playerMove()

def lose():
	print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
	print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      YOU WON     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
	print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

def win():
	print('#####################################################################################')
	#print('#############CONGRATULATIONS YOU PROVED YOUR WORTH i.e NOTHING#######################')
	print('###############################   YOU LOSE   ########################################')
	print('#####################################################################################')
def draw():
	print('*****************************************************************************************')
	print("************************************IT'S A DRAW******************************************")
	print('*****************************************************************************************')

def systemMove():
	global flag,p1
	#print("the value of p1",p1)
	if flag == 0:         #move to take if no one is winning
		if p1 == 1:
			if a[4]==2:
				a[4]=5

			elif a[6]==3 and a[4]==5:
				a[2]=5

			elif a[6]==5 and a[4]==3:
				a[0]=5

			elif a[4]!=2:
				if a[0] == 2:
					a[0] = 5
				elif a[2] == 2:
					a[2] = 5
				elif a[8] == 2:
					a[8] = 5
		elif p1 == 2:
			#print("entered the p1 == 2")
			if a[0] == 2:
				a[0] = 5
			elif a[8] != 2 and a[2] == 2:
				a[2] = 5
			elif a[8] != 2 and a[6] == 2:
				a[6] = 5
			elif a[8] == 2:
				a[8] = 5
			else:
				print("error in systemMove")
		else:
			print("error in system move else")

		board2()

	elif flag == 2 or flag == 1:       #move to take if system is in winning or loosing state
		if pos == 1:
			if a[0] == 2:
				a[0] = 5
			elif a[1] == 2:
				a[1] = 5
			elif a[2] == 2:
				a[2] = 5

		elif pos == 2:
			if a[3] == 2:
				a[3] = 5
			elif a[4] == 2:
				a[4] = 5
			elif a[5] == 2:
				a[5] = 5

		elif pos == 3:
			if a[6] == 2:
				a[6] = 5
			elif a[7] == 2:
				a[7] = 5
			elif a[8] == 2:
				a[8] = 5

		elif pos == 4:
			if a[0] == 2:
				a[0] = 5
			elif a[3] == 2:
				a[3] = 5
			elif a[6] == 2:
				a[6] = 5

		elif pos == 5:
			if a[1] == 2:
				a[1] = 5
			elif a[4] == 2:
				a[4] = 5
			elif a[7] == 2:
				a[7] = 5

		elif pos == 6:
			if a[2] == 2:
				a[2] = 5
			elif a[5] == 2:
				a[5] = 5
			elif a[8] == 2:
				a[8] = 5

		elif pos == 7:
			if a[0] == 2:
				a[0] = 5
			elif a[4] == 2:
				a[4] = 5
			elif a[8] == 2:
				a[8] = 5
				
		elif pos == 8:
			if a[2] == 2:
				a[2] = 5
			elif a[4] == 2:
				a[4] = 5
			elif a[6] == 2:
				a[6] = 5

		if flag == 2:
			win()
		elif flag == 1:
			flag = 3
			board2()
	else:
		for i in range (0,9):
			if(a[i]==2):
				a[i]=5
				break
		board2()


def calc():
	global flag , pos
	row1 = a[0]*a[1]*a[2]	# pos = 1
	row2 = a[3]*a[4]*a[5]	# pos = 2 
	row3 = a[6]*a[7]*a[8]	# pos = 3      
	col1 = a[0]*a[3]*a[6]	# pos = 4
	col2 = a[1]*a[4]*a[7]	# pos = 5
	col3 = a[2]*a[5]*a[8]	# pos = 6
	dig1 = a[0]*a[4]*a[8]	# pos = 7
	dig2 = a[2]*a[4]*a[6]	# pos = 8
	
	#this is checking for the chance if the system is winning
	if row1 == 50:
		flag = 2
		pos = 1
	elif row2 == 50:
		flag = 2
		pos = 2
	elif row3 == 50:
		flag = 2
		pos = 3
	elif col1 == 50:
		flag = 2
		pos = 4
	elif col2 == 50:
		flag = 2
		pos = 5
	elif col3 == 50:
		flag = 2
		pos = 6
	elif dig1 == 50:
		flag = 2
		pos = 7
	elif dig2 == 50:
		flag = 2
		pos = 8

	#this is checking for the chance if player is winning
	elif row1 == 18:
		flag = 1
		pos = 1
	elif row2 == 18:
		flag = 1
		pos = 2
	elif row3 == 18:
		flag = 1
		pos = 3
	elif col1 == 18:
		flag = 1
		pos = 4
	elif col2 == 18:
		flag = 1
		pos = 5
	elif col3 == 18:
		flag = 1
		pos = 6
	elif dig1 == 18:
		flag = 1
		pos = 7
	elif dig2 == 18:
		flag = 1
		pos = 8
	
	if row1 == 27 or row2 == 27 or row3 == 27 or col1 == 27 or col2 == 27 or col3 == 27 or dig1 == 27 or dig2 == 27:
		lose()
		'''print('flag:',flag)
		print('pos:',pos)'''
	else:
		systemMove()


def board1(move):										# prints the board for player 1 move
	a[move] = 3
	print()
	print(a[6],' ',a[7],' ',a[8])
	print(a[3],' ',a[4],' ',a[5])
	print(a[0],' ',a[1],' ',a[2])
	global counter
	counter = counter + 1
	if counter == 5:
		draw()
	else:
		calc()

def playerMove():
	move = int(input("Enter the poition you want to play: "))
	move = move - 1
	board1(move)
def main():
	global p1
	print("This is a game of tik tak toe")
	print("Enjoy!")
	p1 = int(input("press 1 if you want to play first, else press 2: "))
	if p1 == 1:
		print("you are the player first")
		playerMove()
	elif p1 == 2:
		print("you are second player")
		systemMove()
	else:
		print("error the right no.")
		main()


if __name__ == '__main__':
	main()