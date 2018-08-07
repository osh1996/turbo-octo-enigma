botName = 0
def defBot():
	
	global botName
	
	while(not(botName == 750 or botName == 850 or botName == 720)):
		if(botName == 750):
			botName = 750
		elif(botName == 850):
			botName = 850
		elif(botName == 720):
			botName = 720
		else:
			botName = int(raw_input("Choose one: 720/750/850 "))

	print "You have chosen: " + str(botName) + "!!!"

def main():

	defBot()


if __name__ == '__main__':

	main()

