from sys import *
import os
import shutil as sh
import logging as lg
lg.basicConfig(filename='log_10_3.txt',level=lg.DEBUG)
def copy_directory(path,ndir):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	exst=os.path.exists(path)
	
	if exst:
		sh.copytree(path,ndir)
	else:
		lg.info("Invalid path given/Directory not Exists")
	
def main():
	if(len(argv)!=3):
		lg.info("Give Proper Input,eg-(Directory name, new Dirctory name )")
		exit()
	
	try:
		#ext=argv[2].replace(".","")
		#cext=argv[3].replace(".","")
		copy_directory(argv[1],argv[2])
	except ValueError:
		lg.warning("Invlaid Input Datatype")
	except Exception as e:
		lg.warning(e)

if __name__=="__main__":
	main()