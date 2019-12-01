from sys import *
import os
import logging as lg
lg.basicConfig(filename='log_10_2.txt',level=lg.DEBUG)
def change_file_extension(path,ext,cext):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	#print(path)
	exst=os.path.exists(path)
	
	if exst:
		c=1
		for fd,sbd,fl in os.walk(path):
			
			for i in fl:
				if i.split(".")[1]==ext:
					fn=i.split(".")[0]
					fn+="."+cext
					abs=fd+"\\"
					os.rename(abs+i,abs+fn)
					c=0
		if c==1:lg.info("No files with defined extension found")
	else:
		lg.info("Invalid path given/Directory not Exists")
	
def main():
	if(len(argv)!=4):
		lg.info("Give Proper Input,eg-(Directory name, exsting file extension(.doc,.txt),changed file extension)")
		exit()
	
	try:
		ext=argv[2].replace(".","")
		cext=argv[3].replace(".","")
		change_file_extension(argv[1],ext,cext)
	except ValueError:
		lg.warning("Invlaid Input Datatype")
	except Exception as e:
		lg.warning(e)

if __name__=="__main__":
	main()