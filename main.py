import re
with open("books/frankie.txt") as txtf:
	fcontent = txtf.read()
	count = 0
	fwords = fcontent.split()
	for word in fwords:
		count = count+1
	print(fwords)
	print(f"WORDS IN FILE: {count}")
