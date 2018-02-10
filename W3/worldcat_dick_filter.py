import json

infile = open('dick_books.json', 'r')
books = json.load(infile)

filtered_books = []

for book in books:
	if ' Dick' in book['title']:
		print book['title']
		continue
	elif 'Dick ' in book['title']:
		print book['title']
		continue
	elif 'dick' in book['title']:
		filtered_books.append(book)
	elif 'Dick' in book['title']:
		filtered_books.append(book)
	else:
		print book['title']
		continue

infile.close()

outfile = open('filtered_books.json', 'w')
json.dump(filtered_books, outfile, indent=2)
outfile.close()

# for k in myDict:
# 	for v in myDict[k]:
# 		if 'Mary' in v:
# 			return k
# return None

