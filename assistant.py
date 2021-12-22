import time
import sys
import os
import random
import threading

path = os.getcwd()
data_path = path + "/data"
info_file_path = data_path + "/info.txt"
choices = ["Change name", "Tell joke", "Calculate", "Stopwatch", "Bye"]
nonChosenJokesList = list(range(0, 15))

class ConsoleTools:
	def typewrite(message: "message to be printed", waitTime: "wait time in between each character") -> int:
		try:
			for i in range(len(message)):
				sys.stdout.write(message[i])
				sys.stdout.flush()
				time.sleep(waitTime)
			return 0
		except:
			return 1

	def typewriteJoke(message: "message to be printed", waitTimeChar: "wait time in between each character", waitTimeLine: "wait time in between each line") -> int:
		try:
			for i in range(len(message)):
				if message[i] == '\n':
					time.sleep(waitTimeLine)
				sys.stdout.write(message[i])
				sys.stdout.flush()
				time.sleep(waitTimeChar)
			return 0
		except:
			return 1

	def clearScreen():
		try:
			os.system("cls")
		except:
			os.system("clear")


class Stopwatch:
	hasExitedStopwatch = False;

	def WaitForInput():
		global hasEntered
		userInput = input("")
	
		if userInput == "x" or userInput == "X":
			Stopwatch.hasExitedStopwatch = True
		else:	
			Stopwatch.WaitForInput()

	def Stopwatch():
		print("Press Enter to record time\nSelect window by clicking with mouse to pause stopwatch\nPress Enter to unpause stopwatch when paused\nPress X and then Enter to end stopwatch\n")
		centiseconds = 0
		deciseconds = 0
		seconds = 0
		minutes = 0
	
		hasEntered = False;
		thread = threading.Thread(target=Stopwatch.WaitForInput)
		thread.start()

		start_perf = time.perf_counter()
		while not Stopwatch.hasExitedStopwatch:
			delta_time = time.perf_counter() - start_perf

			converted_time = Stopwatch.convert_Time(delta_time)

			print(f"{converted_time[0]}:{converted_time[1]}:{converted_time[2]}{converted_time[3]}", end="\r")
			sys.stdout.flush()
			

		Stopwatch.hasExitedStopwatch = False

	def convert_Time(delta_time: "Time in seconds") -> "[minutes, seconds, centiseconds, deciseconds]":
		seconds = seconds = round(delta_time // 1)
		centiseconds = round((delta_time - seconds) // 0.1)
		deciseconds = round((delta_time - seconds - (centiseconds / 10)) * 100)
		
		minutes = round(seconds // 60)
		seconds -= 60 * minutes
	
		return [minutes, seconds, centiseconds, deciseconds]


def TellJoke():
	with open(path + "/data/jokes.txt") as f:
		if not nonChosenJokesList:
			ConsoleTools.typewrite("Sorry, I ran out of jokes.\n", 0.05)
			return 0
		randomNumber = random.choice(nonChosenJokesList)
		nonChosenJokesList.remove(randomNumber)

		jokes = f.readlines()
		joke = jokes[randomNumber]

		proccessed_joke = bytes(joke, "utf-8").decode("unicode_escape")

	ConsoleTools.typewriteJoke(proccessed_joke, 0.01, 1)
	
def ChangeName():
	ConsoleTools.typewrite("What would you like to be called? ", 0.025)
	name = input()
	with open(info_file_path, "w") as infoFile:
		infoFile.write(name)
	ConsoleTools.typewrite(f"Sucessfully changed name to {name}.\n", 0.025)

def Assist():
	while True:
		for i, choice in enumerate(choices, start=1):
			ConsoleTools.typewrite(f"{i}. {choice}\n", 0.01)
		choice = input()
		lower_choice = choice.lower()

		if lower_choice == "name" or lower_choice == "1" or lower_choice == "change name":
			ChangeName()
		elif lower_choice == "joke" or lower_choice == "2" or lower_choice == "tell joke":
			TellJoke()

		elif lower_choice == "calc" or lower_choice == "3" or lower_choice == "calculate":
			ConsoleTools.typewrite("Enter expression to calculate: ", 0.025)
			expression = input()
			try:
				ConsoleTools.typewrite(f"Answer: {eval(expression)}\n", 0.025)
			except Exception:
				ConsoleTools.typewrite("Invalid expresssion\n", 0.025)
		elif lower_choice == "stopwatch" or lower_choice == "4":
			Stopwatch.Stopwatch()

		elif lower_choice == "bye" or lower_choice == "5":
			ConsoleTools.typewrite("Bot was not an impostor", 0.1)
			ConsoleTools.clearScreen()
			exit()
		else:
			ConsoleTools.typewrite("I do not understand.", 0.025)
			time.sleep(1)
			print()
def FirstTime():
	ConsoleTools.typewrite("Hello there! ", 0.025)
	ConsoleTools.typewrite("What should I call you? ", 0.025)
	name = input()
	try:
		os.mkdir(data_path)
	except OSError:
		ConsoleTools.typewrite("Error making directory", 0.25)

	with open(info_file_path, "a+") as dataFile:
		dataFile.write(name)
		ConsoleTools.typewrite(f"Hello, {name}! Here is what I can do:\n", 0.025)
	# make jokes file
	with open(data_path + "/jokes.txt", "w") as jokesFile:
		jokesFile.write(r"""A cop pulls over an old lady driving very slowly on the highway...\n...and sees three other old ladies in the car, all of whom are terrified.\nCop: I pulled you over because you were driving 35 miles per hour on the highway.\nOld Lady: Well, that's because the speed limit is 35.\nCop: No, this is HIGHWAY 35. The speed limit is 65. By the way, why are these other three women looking so terrified?\nOld Lady: Ohhh, that's because we just got off of highway 145.
Coronavirus has been copying the Black Death\nPlaguearism
What's a tiger running a copying machine called?\nA copycat
What do you call a pig chef?\nA pork chop
Larry Tesler, inventor of the cut, copy, and paste commands, dies at 74\nLarry Tesler, inventor of the cut, copy, and paste commands, dies at 74
If you were to ask Rick Astley for his copy of the movie UP\nHe would "never give you up".\nIn doing so, he would let you down.\nThus creating the rickroll paradox.
The government will send a martial artist after you if you violate copyright law:\nIP Man
My granddad always used to say, "As one door closes another one opens."\nLovely man.\nTerrible cabinet maker.
Today I decided to go visit my childhood home. I asked the residents if I could come inside because I was feeling nostalgic, but they refused and slammed the door in my face.\nMy parents are the worst.
Hear about the new restaurant called Karma?\nThere's no menu: You get what you deserve.
Why do we tell actors to break a leg?\nBecause every play has a cast.
Did you hear about the racing snail who got rid of his shell?\nHe thought it would make him faster, but it just made him sluggish.
What do you call an animal you keep in your car?\nA carpet.
What is the hardest shape to get out of?\nThe trap-azoid.
One night a viking named Rudolph the Red was looking out the window when he said, "It's going to rain."\nHis wife asked, "How do you know?"\nHe said, "Because Rudolph the Red knows rain, dear.\"
Why did the police arrest the turkey?\nThey suspected fowl play.""")

	Assist()

def StartUp():
	if os.path.exists(info_file_path):
		with open(info_file_path, "r") as dataFile:
			name = dataFile.read()
			ConsoleTools.typewrite(f"Hello, {name}! How may I assist you?\n", 0.025)
		Assist()

	else:
		FirstTime()

if __name__ == "__main__":
	StartUp()