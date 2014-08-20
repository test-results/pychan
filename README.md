#pychan

##Usage
Run the script with the following arguments:
`python pychan.py board thread_id`
* `board` is the 4chan board with no other formatting.
* `thread_id` is the string of numbers following `/thread/` in the URL.

###Example Usage
For a thread located at `http://boards.4chan.org/v/thread/0123456789/subject` you would use `python pychan.py v 0123456789`. All images from the thread would then be saved to the same location as the script (`pychan.py`).
