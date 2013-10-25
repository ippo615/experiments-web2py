#!/usr/bin/python

# Only for adding a slight delay to the demonstration
import time

# These are the important imports
import os, threading

# This can be any function that takes a while to complete and that
# you would like to stream the results
def count_to_x(x,pipeOut):
	"""Writes the numbers from 0 to x into pipeOut"""
	for i in range(x):
		pipeOut.flush()
		pipeOut.write(str(i)+'\n')
		time.sleep(0.01)  # For demonstation only
	pipeOut.close()
	 
def index():
	# Create an pipe, it gives 2 handles, 1 for read, 1 for write
	(readHandle, writeHandle) = os.pipe()
	# Opend the corresponding handles for reading and writing
	r = os.fdopen(readHandle, 'r')
	w = os.fdopen(writeHandle, 'w')
	# Tell the browser that we are sending raw text/html
	response.headers['Content-Type'] = 'text/html'
	# Create a new thread which will perform the long task
	# This thread requires the handle to write the pipe
	worker = threading.Thread(target=count_to_x,args=(1000,w))
	worker.start()

	# Tell web2py that we are going to stream the contents and
	# push the updates after every 6 characters
	return response.stream(r, 6)

