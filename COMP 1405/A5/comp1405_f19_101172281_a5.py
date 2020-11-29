# name = Mihir Gupta
#STudent Id = 101172281



#defining translated_phrase

def translated_string(string):
	#defining punctuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	# remove punctuation from the string
    no_punct = ""
    for char in string:
    	if char not in punctuations:
    		no_punct = no_punct + char
    #display the unpunctuated string
    #print(no_punct)

	#Defining dictonary for capital conversion.
    dictionary = {' ':' ','a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X', 'y':'Y', 'z':'Z' }
    output = ""
    for i in no_punct:
    	output += dictionary[i]	
    print("The translated string is""\n",output)
    return output
	


#defining change phrase variable
def change_phrase(output):
	while True:
		dictionary1 = {'BY THE WAY':'BTW',"TALK TO YOU LATER":"TTYL","GOT TO GO":"GTG","BE RIGHT BACK":"BRB"}
		
		string = input("Do you want to replace phrases? ")
		if string in ['no','NO','nO','No']:
			pass
			break
		elif string in ['yes','YES','Yes']:
			for i in ["BY THE WAY","TALK TO YOU LATER","BE RIGHT BACK","GOT TO GO"]:
				output1 = ""
				end=0
				start=0
				end=output.find(i)
				if end!=-1:
					output1=output[0:end]+dictionary1[i]
				else:
					output1=output
				
			
				while(end!=-1):
					
					start=end+len(i)
					end=output.find(i,start)
					if end!=-1:
						output1+=output[start:end]+dictionary1[i]
					else:
						output1+=output[start:]
				output=output1
			print("After replacing phrases new output is""\n",output1)
			return output1
			break
		else:
			wrong = input("Press enter to repeat again")

			
#defining replace words variable.
def replace_words(output1):
	while True:
		dictionary2 = {"PLEASE":"PLZ","WHAT":"WHT","ACCORDING":"ACC","NEVERMIND":"NVM"}
		
		string = input("Do you want to replace words? ")
		if string in ['no','NO','nO','No']:
			pass
			break
		elif string in ['yes','YES','Yes']:
			for i in ["NEVERMIND", "PLEASE", "WHAT", "ACCORDING"]:
				output2 = ""
				end=0
				start=0
				end=output1.find(i)
				if end!=-1:
					output2=output1[0:end]+dictionary2[i]
				else:
					output2=output1
				
				while(end!=-1):
					
					start=end+len(i)
					end=output1.find(i,start)
					if end!=-1:
						output2+=output1[start:end]+dictionary2[i]
					else:
						output2+=output1[start:]
				output1=output2
			print("After replacing words the new output is""\n",output2)
			return output2
			break
		else:
			wrong = input("Press enter to repeat again")
			
#defining letters change
def replace_letters(output2):
	while True:
		dictionary2 = {"A":"4","K":"|<","L":"|_","E":"3","S":"5","O":"0","B":"13","V":"\/"}
		string = input("Do you want to replace letters? ")
		if string in ['no','NO','nO','No']:
			pass
			break
		elif string in ['yes','YES','Yes']:
			for i in ["A","K","L","E","S","O","B","V"]:
				output3 = ""
				end=0
				start=0
				end=output2.find(i)
				if end!=-1:
					output3=output2[0:end]+dictionary2[i]
				else:
					output3=output2
				
				while(end!=-1):
					
					start=end+len(i)
					end=output2.find(i,start)
					if end!=-1:
						output3+=output2[start:end]+dictionary2[i]
					else:
						output3+=output2[start:]
				output2=output3
			print("After replacing letter new output is""\n",output3)
			return output3
			break
		else:
			wrong = input("Press enter to repeat again")
#main function whenre every other function is called	
def main():
	while True:
		string = input("Type the string to be translated: ")
		punc_str=translated_string(string)
		phrase_str=change_phrase(punc_str)
		words_str=replace_words(phrase_str)
		letters_str=replace_letters(words_str)
		repeat = input("Do you want to translate the new string? ")
		if repeat in ["no","NO","No","nO"]:
			print("Goodbye")
			break
			
			

		

main()



