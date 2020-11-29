#Name :Mihir Gupta
#Student id = 101172281


# creating the user input for 8 rows and 8 collumns. This function checks the input if it meats the requirements or not. This function also checks the length of the input.ie. if the length is 8 or not. if it is not 8 it prints invalid input and gives you chance to print it again.This funciton has none@param and list2@return.
def user_input():
	character = ["K","k","Q","q","R","r","N","n","B","b","P","p","-"]
	list2 = []
	for j in range(8):
		list1 = []

		# this loop validate the correct and the length of the row.
		validate = True
		while validate:
			validate = False
			input_1 = input("Enter row's "+str(j+1)+" elements. ")
			if len(input_1) != 8:
				print("Invalid input")
				validate = True
				continue
			for x in input_1:
				if x in character:
					continue			
				else:
					print("Invalid input")
					validate = True
					break
					
		for i in range(8):
			list1.append(input_1[i])
		list2.append(list1)

	# we print it out to the terminal
	for list1 in list2:
		for col in list1:
			print(col, end="")
		print()
	#print(list2)
	return list2





#this function that stores the values of the characters in the lisT. This funciton has list2@param and values@return.
def get_value_list(list2):
	character = ["K","k","Q","q","R","r","N","n","B","b","P","p","-"]
	value_character = [0.0,0.0,10.0,10.0,5.0,5.0,3.5,3.5,3.0,3.0,1.0,1.0,0.0]
	values = []
	for x in list2:
		row_value = []
		for y in x:
			for i in range(len(character)):
				if character[i] == y:
					row_value.append(value_character[i])
		values.append(row_value)
	#print(values)
	return values
				
		
			  



#This function calculates the score count of the white team and the black team.This funciton has list2@param and none@return.
def score_count(list2):
	sum_white= 0
	sum_black= 0
	for i in list2:
		for j in i:
			#calculate score count for the white team.
			if j == "q":
				sum_white += 10
			if j == "b":
				sum_white += 3
			if j == "n":
				sum_white += 3.5
			if j == "r":
				sum_white += 5
			if j == "p":
				sum_white += 1
			#calculating score count for the black team. 
			if j == "Q":
				sum_black += 10
			if j == "B":
				sum_black += 3
			if j == "N":
				sum_black += 3.5
			if j == "R":
				sum_black += 5
			if j == "P":
				sum_black += 1
	print("Total score of the white team is", sum_white)
	print("\n""Total score of the black team is", sum_black)
	# deciding the winner by checking who have more score.
	if sum_white > sum_black:
		print("\n""Currently White is winning.")
	elif sum_white < sum_black:
		print("\n""Currently Black is winning.")
	else:
		print("\n""Both black and white team have equal score.")




	
#This function gives instruction to the user on how to use this program.This funciton has none@param and none@return
def instructions():
	instruction = input("Do you want to read the instructions for how this program works?(type yes or no) ""\n")
	if instruction in ["no", "No", "nO", "NO"]:
		print("There you go""\n")
		pause = input("Press Enter key to continue.""\n")
	else:
		print("This program is a model of chess game. This program tells the user who is winning the game i.e. either the black team or the white team. This program calculates the score of the team by calculating the sum of number chess pieces available. This program uses lowercase letters for the white pieces and uppercase letters for the black pieces, and this program uses the hyphen """"-"""" for an empty space and the following abbreviations – (K)ing, (Q)ueen, (B)ishop, k(N)ight, (R)ook, and (P)awn. The values of each of the chess piece is given below.")
		print()
		print("\t", "(K)ing = 0","\n","\t", "(Q)ueen = 10","\n","\t", "k(N)ight = 3.5","\n","\t", "(R)ook = 5","\n","\t", "(P)awn = 1","\n")
		pause1 = input("press Enter key to continue.""\n")



#This function makes the moves of the chess board you entered above. This function have x cordinate as the row number and y co-ordinate as the column of the respective row.This funciton has list2@param and none@return.
def chess_move(list2):
	while True:
		print("\n""Here are the instructions on how to move a piece. So X co-ordinate is the row number(row increases downwards from 1 to 8) and Y co-ordinate is the column number of that particular row (column increases from left to right starting from 1 and ends at 8.")
		x_piece = int(input("\n""Enter x co-ordinate for the piece you wish to move."))
		y_piece = int(input("Enter y co-ordinate for the piece you wish to move."))
		x_new = int(input("\n""Enter x co-ordinate where you wish your piece should to be placed."))
		y_new = int(input("Enter y co-ordinate where you wish your piece should to be placed.")) 
		if list2[x_piece-1][y_piece-1] == "-":
			print("\n""There is no piece at ("+str(x_piece)+","+str(y_piece)+") co-ordinates.")
			print("\n""Add new input")
			continue	
		else:
			temp=list2[x_piece-1][y_piece-1]
			list2[x_new-1][y_new-1] = temp
			list2[x_piece-1][y_piece-1] = "-"
			for list1 in list2:
				for col in list1:
					print(col, end="")
				print()
			break

#This function is the main heart of the whole program.This funciton has none@param and none@return
def main():
	instructions()
	while True:
		chess_board = user_input()
		score = score_count(chess_board)
		value_list = get_value_list(chess_board)
		print("\n""A: If you want to add new chess board.")
		print("B: If you want to make a move in your existing chess board.")
		print("C/Q: If you want to quit the programme.")
		print()
		options = input("Chose one of the above options you want to proceed with.")
		print()
		if options in ["A","a"]:
			print("You have to correct this.")
			continue
		elif options in ["B", "b"]:
			while True:
				chess_move(chess_board)
				chose = input("Do you want to make other move? ")
				if chose in ["no","NO","No","nO"]:
						print("goodbye")
						break
					
			break
		elif options in ["C","c","Q","q"]:
			print("Goodbye")
			break
	
			

main()
	
