
bookfile = "books/frankenstein.txt"
with open(bookfile) as txtfile:
	fcontent = txtfile.read()
	characters = list(fcontent)
	words = fcontent.split()
	wordCount = 0
	for word in words:
		wordCount = wordCount + 1
	characterDict = {}
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for character in characters:
		if character in letters:
			character = character.lower()
			if character not in characterDict:
				characterDict[character] = 1
			else:
				characterDict[character] = characterDict[character] + 1
print("\n--- Begin report of books/frankenstein.txt ---\n")
print(f"\n{wordCount} words were found in {bookfile}\n")

for character in characterDict:
	print(f"Character {character} was found {characterDict[character]} times")
print("\n--- End report ---\n")
