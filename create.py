import sys

def create():
	print("Creating new file")
	name=raw_input ("enter the name of the file:")
	extension=raw_input ("enter extension of file:")
	try:
		name=name+"."+extension
		file=open(name,'a')
		
		file.close()
	except:
			print("error occured")
			sys.exit(0)
			
create()