# Mihir Gupta
# student id - 101172281
# student email - mihirgupta@cmail.carleton.ca

#I have added comments for the movies(distinguishing factors) near the question for the printing particular movies. I have printed the list of movies after the sub-genre. Please see the comments. Thanks for your time.

#starting with the expert system.
print("\t""Expert program for guessing your movie.")
#asking for instructions.
print("\n""There will be certain instructions on how to use this expert system")
instruction = input("Would you like to read instructions?""(yes or no)")
if instruction in ['yes','Yes','YES']:
	print("\n""This program works by asking user the subgenre for the movie you want the expert program to guess. I have provided to sub genres in my program. The first one is ""ESCAPE"" and the other one is ""HORROR COMEDY"". Select your sub-genre and user will be given some questions and you need to answer them in yes or no. This expert system will proceed you to your desire movie.The questions will be on the distinguishing features of the different movies.")
else:
	print("\n""Since you selected no instructions.You will be on your own.")

#giving sub-genre to user
sub_genre1 = "Escape"

#List of movies
#(1)The great Escape(20th century)
#(2)Stalag 17 (20th century)
#(3)Escape from alcatraz(20th century)
#(4)The island(21st century)
#(5)Chicken run(20th century)
#(6)Rescue Dawn(21st century)
#(7)Maze runner(21st century)
#(8)Zombie Island(20th century)
#(9)Now you see me(21st century))
#(10) The Escapist(21st century))
sub_genre2 = "Horror Comedy"

#   20th CENTURY MOVIES
#(1)Little shop of horrors
#(2)Ghostbusters
#(3)Fright Night
#(4)Abbott and castello meet frankenstein
#(5)Bettlejuice

#   21st CENTURY MOVIES
#(1)I.T
#(2)Scary Movie
#(3)Final Girls
#(4)The babysitter
#(5)Get out
print("\n""\t""Chose your sub-genre.""\n""(1) Escape""\n""(2) Horror Comedy")
while True:
	sub_genre = input("\n""What is your sub-genre? ")
	if sub_genre in ['1','Escape','escape']:
		ques_1 = input("is the movie is from 20th century? ")
		if ques_1 in ['yes','Yes',"YES"]:
			ques_2 = input("Has movie used animated graphics? ")
			#animated movies in 20th century.
			#zombie island 
			#chicken run	
			if ques_2 in ['yes','Yes',"YES"]:
				ques_3 = input("Is main actor in movie is Woody Harrelson? ")
				#Woody Harrelson is main actor is zombie island.
				if ques_3 in ['yes','Yes',"YES"]:
					print("ZOMBIE ISLAND is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
							
				else:
					print("CHICKEN RUN is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
			else:
				ques_4 = input("Is movie based on real story? ")
				#Escape from alcatraz and The Great escape is 						based on real incidences.
				if ques_4 in ['yes','Yes',"YES"]:
					print("ESCAPE FROM ALCATRAZ is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
				else:
					ques_5 = input("Is movie based on comedy genre also? ")
					#Stalag 17 has comedy genre too.
					if ques_5 in ['yes','Yes',"YES"]:
						print("STALAG17 is the movie title.")
						run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
					else:
						print("THE GREAT ESCAPE is a movie 							title.") 
						break
	
		else:
			ques_6 = input("Is the movie has some science fiction involved? ")
			#"The island" and "maze runner" both have scientific usage.
			if ques_6 in ['yes','Yes',"YES"]:
				ques_7 = input("Does movie have an extremely large and dangerous animals? ")
				#Maze runner involves extremely large and dangerous animals.
				if ques_7 in ['yes','Yes',"YES"]:
					print("THE MAZE RUNNER is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
				else:
					print("THE ISLAND is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
			else:
				ques_8 = input("Does movie is based on magic tricks? ")
				#"now you see me" involves magic tricks.
				if ques_8 in ['yes','Yes',"YES"]:
					print("NOW YOU SEE ME is the movie title")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
				else:
					ques_9 = input("Is a film based on biography of Dieter Dengler? ")
					#Rescue Dawn is based on true story of Dieter Dengler.
					if ques_9 in ['yes','Yes',"YES"]:
						print("RESCUE DAWN is the movie title.")
						run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
					else:
						print("THE ESCAPIST is the movie title.")
						run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
			
				
	elif sub_genre in ['2','Horror Comedy','horror comedy']:
		ques_10 = input("is the movie is from 20th century? ")
		if ques_10 in ['yes','Yes',"YES"]:
			ques_11 = input("Is movie about little kid left at home alone? ")
			#I.T. and the babysitter is movie with kids left at home alone.
			if ques_11 in ['yes','Yes',"YES"]:
				ques_12 = input("Is main actor in movie is Joker? ")
				#Joker is main actor in I.T.
				if ques_12 in ['yes','Yes',"YES"]:
					print("I.T. is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
				else:
					print("THE BABYSITTER is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
			else:
				ques_13 = input("Is movie distributed by universal studios? ")
				#Get out is distributed by universal studios
				if ques_13 in ['yes','Yes',"YES"]:
					print("GET OUT is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
				else:
					ques_14 = input("Does the movie is made originally from its book? ")
					#Final girls is made from its book.
					if ques_14 in ['yes','Yes',"YES"]:
						print("FINAL GIRLS is the movie title.")
						run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
					else:
						print("SCARY GIRLS is a movie title.") 
						run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
	
		else:
			ques_15 = input("Is the movie distributed by Warner bros? ")
			#Beetle juice and little shop of horror is distributed by warner bros.
			if ques_15 in ['yes','Yes',"YES"]:
				ques_16 = input("Is movie used the genre scientfic fiction also? ")
				#Little shops of horror used sci-fi genre.
				if ques_16 in ['yes','Yes',"YES"]:
					print("LITTLE SHOP OF HORRORS is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
				else:
					print("BEETLE JUICE is the movie title.")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
			else:
				ques_17 = input("Is the movie first horror comedy film? ")
				#Abbott and costello Meet Frankenstien is first horror comedy movie.
				if ques_17 in ['yes','Yes',"YES"]:
					print("ABBOTT AND COSTELLO MEET FRANKENSTIEN is the movie title")
					run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
				else:
					ques_18 = input("Does movie involves zombies? ")
					#Fright Night involves zombies in it.
					if ques_18 in ['yes','Yes',"YES"]:
						print("FRIGHT NIGHT is the movie title.")
						run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
					else:
						print("GHOSTBUSTERS is the movie title.")
						run_program_again = input("\n""Do you want to run the program again? ")
					if run_program_again in ['no','No',"NO"]:
						break
	else:
		print("Please enter valid option")
		run_program_again = input("\n""Do you want to run the program again? ")
		if run_program_again in ['no','No',"NO"]:
			break
			
		
		

