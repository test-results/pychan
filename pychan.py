import os
import urllib
import urllib2
from sys import argv
from bs4 import BeautifulSoup
from colorama import init, Fore, Back
init()

script, board, thread = argv

# Create URL from user inputs
thread_url = "http://boards.4chan.org/%s/thread/%s" % (board, thread)

# Request URL, open and give to BeautifulSoup
req = urllib2.Request(thread_url)
req.add_header('User-agent', 'Mozilla 5.10')
thread_html = urllib2.urlopen(thread_url)
soup = BeautifulSoup(thread_html)

# Find the div with class="thread" where all the images are contained
div_thread = soup.find('div', {'class':'thread'})

# Find the thread title, just to print something
thread_title = div_thread.find('span', {'class':'subject'})
thread_name = soup.find('link', {'rel':'canonical'}).get('href').split('/')[-1]
print Fore.GREEN + "   Board:\t" + "/" + board + "/"
print Fore.GREEN + "     URL:\t" + str(thread_url)
print Fore.GREEN + " Subject:\t" + str(thread_title.string)
print Fore.GREEN + "   Title:\t" + thread_name

# Get all of the HTML a tags with class="fileThumb", get the href tag
image_hrefs = div_thread.find_all('a', {'class':'fileThumb'})

# Create folder based on the board and thread_id

thread_save_directory = str(thread) + '-' + thread_name 
save_directory = os.path.join(board, thread_save_directory)
if not os.path.exists(save_directory): os.makedirs(save_directory)

# To do the little counter on the side of the print
image_count = 1

# For each HTML a tag with class="fileThumb", get the href tag
for href in image_hrefs:
	# Adjust to get the URL of the image
	image_url = "http:" + href.get('href')
	# Adding a prefix to save_filename preserves the order of posting
	# 	filename_prefix = str(filename).rjust(3, '0')
	# Get the original filename by splitting URL at '/' and getting the last segment
	# of it with [-1]
	filename_suffix = image_url.split('/')
	save_filename = os.path.join(save_directory, filename_suffix[-1])
	if os.path.exists(save_filename):
		print Fore.RESET + "[" + str(image_count).rjust(3, '0') + "/" + str(len(image_hrefs)).rjust(3, '0') + "] " + str(filename_suffix[-1]) + Fore.YELLOW + "\t-"
		image_count += 1
	else:
		urllib.urlretrieve(image_url, save_filename)
		# Print that the image was saved
		print Fore.RESET + "[" + str(image_count).rjust(3, '0') + "/" + str(len(image_hrefs)).rjust(3, '0') + "] " + str(filename_suffix[-1]) + Fore.GREEN + "\t+" + Fore.RESET + " (" + Fore.RESET + str(os.path.getsize(save_filename)/1000) + " KB)"
		image_count +=1
	
