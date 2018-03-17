import os, sys
from PIL import Image

size = 360, 480

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "_thumbnail.jpg"
    outfile = outfile.replace('imgs/', 'resized_imgs/')
    # outfile = 'resized_imgs/' + outfile
    if infile != outfile:
    	# im = Image.open(infile)
    	# im.thumbnail(size, Image.ANTIALIAS)
    	# im.save(outfile, "JPEG")
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
