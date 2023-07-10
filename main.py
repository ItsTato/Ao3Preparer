from os import path
from sys import exit
from json import load

iExists:bool = False
oExists:bool = False
oOverWrite:bool = False
scExists:bool = False
specialChars:dict = {}

iExists = path.exists("./input.txt")

if not iExists:
	print("Must have 1 input file called \"input.txt\"")
	exit()

scExists = path.exists("./special-chars.json")

if not scExists:
	print("Missing critical configuration file \"special-chars.json\"!")
	exit()

with open("./special-chars.json","r") as file:
	specialChars:dict = load(file)
	file.close()

oExists = path.exists("./output.html")

if oExists:
	val:str = input("\"output.html\" is already present.\n> Overwrite? [Yes/No] (No) ")
	if val.lower() in ["","n","no"]:
		oOverWrite = False
	else:
		oOverWrite = True

with open("./input.txt","r") as file:
	data:list = file.readlines()
	file.close()

def cleanseLines(lines:list) -> list:
	"""
	Prepares a list made up of strings by removing any "\\n" added in by the file reading function and instead correctly inclosing it in <p> elements.
	"""
	cleansed:list = []
	for line in lines:
		cLine:str = line
		if line[-1] == "\n":
			cLine = line[:-1]
		cLine = f"<p>{cLine}</p>"
		if cLine in ["<p></p>", "<p> </p>", "", " "]:
			cLine = "<p>&nbsp;</p>"
		cleansed.append(cLine)
	return cleansed

def replaceSpecialSigns(lines:list) -> list:
	"""
	Replaces the special character set with the corresponding html counter-parts.
	
	Uses special-chars.json for configuration.
	"""
	ready:list = []
	for line in lines:
		cLine = line
		for index in specialChars:
			cLine:str = cLine.replace(index,specialChars[index])
		ready.append(cLine)
	return ready

def listToString(lines:list) -> str:
	ready = """"""
	for index, line in enumerate(lines):
		if index == 0:
			ready = line
			continue
		ready = f"{ready}\n{line}"
	return ready

cleansed:list = cleanseLines(data)
specialSignReady:list = replaceSpecialSigns(cleansed)
forFile:str = listToString(specialSignReady)

with open("./output.html","w+") as file:
	file.write(forFile)
	file.close()
