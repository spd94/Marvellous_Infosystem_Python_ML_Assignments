from sys import *
import os
import hashlib
import logging as lg
lg.basicConfig(filename='log_11_1.txt',level=lg.DEBUG)

def gen_chksum(path):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	#print(path)
	exst=os.path.exists(path)
	
	if exst:
		c=1
		for fd,sbd,fl in os.walk(path):
			for i in fl:
				#if i.split(".")[1]==ext:
					#print(i)
				abs=fd+"\\"+i
				lg.info(hashlib.md5(open(abs, 'rb').read()).hexdigest())
				c=0
		if c==1:
			lg.info("No files found")
			
	else:
		lg.debug("Invalid path given/Directory not Exists")
	
def main():
	if(len(argv)!=2):
		lg.info("Give Proper Input,eg-(Directory name)")
		exit()
	
	try:
		#ext=argv[2].replace(".","")
		gen_chksum(argv[1])
		
	except ValueError:
		lg.warning("Invlaid Input Datatype")
		
	except Exception as e:
		lg.warning(e)
		

if __name__=="__main__":
	main()