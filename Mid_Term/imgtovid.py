import json

infile = open('result_imgs.json', 'r')
imgs = json.load(infile)

f = open('vidsequence.txt','w')

line1 = "file 'resized_imgs/0_Van_Gogh.jpg'\n"
line2 = "duration 2\n"
f.write(line1)
f.write(line2)

for img in imgs:
	path = img['filename']
	path = path.replace('.jpg', '_thumbnail.jpg')
	path = path.replace('imgs/', 'resized_imgs/')
	line1 = "file '" + str(path) + "'\n"
	line2 = "duration 1\n"
	f.write(line1)
	f.write(line2)

line1 = "file 'resized_imgs/0_Van_Gogh.jpg'\n"
line2 = "duration 2\n"
line3 = "file 'resized_imgs/0_Van_Gogh.jpg'\n"
f.write(line1)
f.write(line2)
f.write(line3)

infile.close()
f.close()
