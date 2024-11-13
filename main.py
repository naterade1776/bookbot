import re
#import os
with open("books/frankie.txt") as txtf:
	fcontent = list(txtf.read())
	characterDict = {}
	print("Processing...")
	for character in fcontent:
#		os.system("clear")
#		print("Processing...")
		if character not in characterDict:
			characterDict[character] = 1
		else:
			characterDict[character] = characterDict[character] + 1
#	print(fcontent)
	count = 0
#	fwords = fcontent.split()
#	for word in fwords:
#		count = count+1
	print(characterDict)
#	print(f"WORDS IN FILE: {count}")
