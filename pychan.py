import os
import urllib
import urllib2
from sys import argv
from bs4 import BeautifulSoup

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

# Start the filename counting at 1
filename = 1

# Find the thread title, just to print something
thread_title = div_thread.find('span', {'class':'subject'})
print "Board:\t\t" + "/" + board + "/"
print "URL:\t\t" + str(thread_url)
print "Subject:\t" + str(thread_title.string) 

# Get all of the HTML a tags with class="fileThumb", get the href tag
image_hrefs = div_thread.find_all('a', {'class':'fileThumb'})

# For each HTML a tag with class="fileThumb", get the href tag
for href in image_hrefs:
	# Adjust to get the URL of the image
	image_url = "http:" + href.get('href')
	# Adding a prefix to save_filename preserves the order of posting
	filename_prefix = str(filename).rjust(3, '0')
	# Get the original filename by splitting URL at '/' and getting the last segment
	# of it with [-1]
	filename_suffix = image_url.split('/')
	save_filename = str(filename_prefix) + '-' + filename_suffix[-1]
	urllib.urlretrieve(image_url, save_filename)
	# This length is incorrect
	print "[" + str(filename_prefix) + "/" + str(len(image_hrefs)).rjust(3, '0') + "] - SAVED" 
	filename += 1