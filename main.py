from os import path
from sys import exit

iExists:bool = False
oExists:bool = False
oOverWrite:bool = False

iExists = path.exists("./input.txt")

if not iExists:
	print("Must have 1 input file called \"input.txt\"")
	exit()

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
	cleansed:list = []
	for line in lines:
		cLine:str = line
		if line[-1] == "\n":
			cLine = line[:-1]
		cleansed.append(cLine)
	return cleansed

print(cleanseLines(lines=data))
