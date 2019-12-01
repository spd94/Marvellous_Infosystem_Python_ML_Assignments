from sys import *
import os
import logging as lg
lg.basicConfig(filename='log_10_1.txt',level=lg.DEBUG)
'''logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
'''

def change_file_extension(path,ext):
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
					lg.info(i)
					c=0
		if c==1:
			lg.info("No files with defined extension found")
			
	else:
		lg.debug("Invalid path given/Directory not Exists")
	
def main():
	if(len(argv)!=3):
		lg.info("Give Proper Input,eg-(Directory name, file extension(.doc,.txt))")
		exit()
	
	try:
		ext=argv[2].replace(".","")
		change_file_extension(argv[1],ext)
		
	except ValueError:
		lg.warning("Invlaid Input Datatype")
		
	except Exception as e:
		lg.warning(e)
		

if __name__=="__main__":
	main()