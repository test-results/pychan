#pychan

pychan is a Python script to automatically download all of the full-resolution images from a 4chan thread.

##Features
* Saves all files including images (.jpg, .gif, .png) and video formats (.webm)

##Usage
1. Run the script with the following arguments:
`python pychan.py board thread`
 * `board` is the 4chan board with no other formatting.
 * `thread` is the string of numbers following `/thread/` in the URL.
2. All of the images will saved in a folder named after the string of numbers of `thread`.

###Example Usage
1. For a thread located at `http://boards.4chan.org/v/thread/0123456789/subject`
2. Use `python pychan.py v 0123456789`
3. All images from the thread will be saved to a folder `0123456789` (in the location of `pychan.py`).

##About Me
I am a beginner programmer, starting with Python and using some of these projects as experience. Do **not** expect anything spectacular.
