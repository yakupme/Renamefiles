
import os


""" Python script to rename multiple files in the same directory """

file_path =  os.getcwd()
file_names = os.listdir(file_path)

try: 
	for file_name in file_names:
	    os.rename(file_name, file_name.replace("Masterold", "Masternew"))
	    
except OSError as e:
	print e

print 'Files names are changed successfuly'