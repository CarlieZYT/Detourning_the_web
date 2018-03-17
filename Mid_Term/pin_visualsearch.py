'''
to run:
    python pin_visualsearch.py pin_number pin_width pin_height
'''

import requests
import sys
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver

def download_file(url, local_filename):
	# local_filename = url.split('/')[-1]

	# NOTE the stream=True parameter
	r = requests.get(url, stream=True)
	with open(local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
				#f.flush() commented by recommendation from J.F.Sebastian
	# return local_filename

def search(pin, x, y, w, h):
	base_url = 'https://www.pinterest.com/pin/'
	url = base_url+str(pin)+'/visual-search/?x='+str(x)+'&y='+str(y)+'&w='+str(w)+'&h='+str(h)
	driver.get(url)

	time.sleep(2)
	html = driver.page_source
	soup = BeautifulSoup(html, "html.parser")
	images = soup.select('.pinWrapper img')

	# if len(images) == 0:
	# 	exit()

	output = []

	for image in images:
		srcset = image.get('srcset')
		src = srcset.split("2x, ",1)[1]
		src = src.split(" 3x",1)[0]

		descrip = image.get('alt')
		local_filename = src.split('/')[-1]
		filename = 'imgs/'+str(w)+'*'+str(h)+'x='+str(x)+'y='+str(y)+'_'+local_filename
		# print src
		# print descrip
		download_file(src, filename)
		# call(['convert', localname, '-solarize', '50', localname + '.solarized.jpg'])
		# call(['open', localname + '.solarized.jpg'])
		# call(['say', descrip])
		item = {
            'filename': filename,
            'descrip': descrip
        }

		output.append(item)

	return output

# invisible option setting for chrome
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome()

# login pinterest first
driver.get('https://www.pinterest.com/login/?referrer=home_page')
username = driver.find_elements_by_css_selector('#email')
password = driver.find_elements_by_css_selector('#password')

username[0].send_keys(my_account)
password[0].send_keys(my_password)
driver.find_elements_by_css_selector("[type=submit]")[0].click()
time.sleep(5)

posX = 0
posY = 0
width = int(sys.argv[2])/20
width = int(width)
height = int(sys.argv[3])/20
height = int(height)
print width
print height

all_results = []

while posY < int(sys.argv[3])-height:
	while posX < int(sys.argv[2])-width:
		results = search(sys.argv[1], posX, posY, width, height)
		all_results = all_results + results
		print 'X: ' + str(posX) + ', Y: ' + str(posY)
		posX = posX + width
	posX = 0
	posY = posY + height

outfile = open('result_imgs.json', 'w')
json.dump(all_results, outfile, indent=2)
outfile.close()


driver.quit()











