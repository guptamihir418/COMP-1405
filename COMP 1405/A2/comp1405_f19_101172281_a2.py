#Mihir Gupta
#Student ID - 101172281
#CU email - mihirgupta@cmail.carleton.ca


#roller coaster ride game

#heading of the game
print("\n""Lets have the roller coaster ride to NEVERLAND, this ride is going to be really exciting and thrilling. There are many kind of people who chooses this ride, some of them are mentioned below. Make your selection from below." "\n") 

#choices given to user.
print(" (1) You are a professor or teacher accompanying students.", "\n","(2) You are student of a school or university." ,"\n","(3) You are a person who is on holiday with family." ,"\n", "(4) You are a part of group which is on holiday." "\n")

#users choice is stored in variable.
players_choice = input( "What is your selection?" "\n")
players_choice1 = "You are a professor or teacher accompanying students."
players_choice2 = "You are student of a school or uninversity."
players_choice3 = "You are a person who is on holiday with family."
players_choice4 = "You are a part of group which is on holiday."

#starting with player choice.
if players_choice == "1":
	players_choice = players_choice1

elif players_choice == "2":
	players_choice = players_choice2

elif players_choice == "3":
	players_choice = players_choice3

elif players_choice == "4":
	players_choice = players_choice4

else:
	print("\t","\Invalid Input")

#starting second question:- name of members
print("       Enter your four players you want in your team." "\n")

team_player1 = input("What is the name of your first team player? ")
team_player2 = input("What is the name of your second team player? ")
team_player3 = input("What is the name of your third team player? ")
team_player4 = input("What is the name of your fourth team player? ")

#printing your players
print("Your four team players are:-" "\n")
print("(1)",team_player1)
print("(2)",team_player2)
print("(3)",team_player3)
print("(4)",team_player4)

#printing your chosen choice
print("\t" "\n" , players_choice)

#moving to next
Break = input("Press Enter to move further")


#starting with the things to buy
print("\n","Before going to the ride you need to know about some rules about the ride. This ride is going to be tough, with a lot of risk, you will face many dangerous animals. So you need to buy some tools to protect yourself. See the list below and make your selection." "\n")
print("              Welcome to Ben's shop" "\t")
print(" (1)Gun = $100(each)","\t", "        (2)Ammo = $20(1 bundle)","\n", "(3)flamethrower = $400","\t","(4)knife = $20(each)","\n","(5)chainsaw = $250" "\n")

#making input for guns selection.
print("           You have 2000$ for your use.""\t" "\n") 	
selection = input("What is your selection?")
gun = "Gun $100 each"
ammo = "Ammo $20 per bundle"
flamethrower = "flamethrower $400"
knife = "knife $20 each"
chainsaw = "chainsaw $250"

#making loop for weapons 
cost = 0
while selection != "none":

	if selection == "1":
		selection = gun
		units_of_guns = int(input("how many guns you want? "))
		bill_of_guns = (units_of_guns * 100)
		print("\n""Your bill for guns is" , bill_of_guns, "$")
		cost = cost + bill_of_guns
		print("Bill so far is",cost,"\n")
	elif selection == "2":
		selection = ammo
		units_of_ammo = int(input("How many bundles of ammunination you want? "))
		bill_of_ammo = (units_of_ammo * 20)
		print("\n""Your bill for ammo is" ,bill_of_ammo, "$")
		cost = cost + bill_of_ammo
		print("Bill so far is",cost,"\n")
	elif selection == "3":
		selection = flamethrower
		units_of_flamethrower = int(input("How many flamthrowers you want? "))
		bill_of_flamethrower = (units_of_flamethrower * 400)
		print("\n""Your bill for flamethrower is", bill_of_flamethrower, "$")
		cost = cost + bill_of_flamethrower
		print("Bill so far is",cost,"\n")
	elif selection == "4":
		selection = knife
		units_of_knives = int(input("How many knives you want? "))
		#print(units_of_knives)
		bill_of_knives = (units_of_knives * 20)
		print("\n""Your bill for knives is" ,bill_of_knives,"$")
		cost = cost + bill_of_knives
		print("Bill so far is",cost,"\n")
	elif selection == "5":
		selection = chainsaw
		units_of_chainsaw = int(input("How many chainsaws you want ?"))
		bill_of_chainsaw = (units_of_chainsaw * 250)
		print("\n""Your bill for chainsaw is" ,bill_of_chainsaw,"$")
		cost = cost + bill_of_chainsaw
		print("Bill so far is",cost,"\n")
	else:
		print("\n","\t","Invalid selection")
		
	selection = input("Enter your another selection(Type none to end your selection) 	")



print("\n","\t","Your total cost for the weapons is",cost,"$")

#money left with you
if cost < 2000:
	print()
	print("\n","Your money left is",2000 - cost,"$")
	print("\n","\t","GOOD LUCK WITH YOUR RIDE!""\n")

else:
	print("\n","You have exceeded over 2000$","\n","\t","You can't buy these items.")
	print("\n","\t","RUN AGAIN.""\n")













 
