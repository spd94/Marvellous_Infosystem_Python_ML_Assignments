from sys import *
import os
import logging as lg
lg.basicConfig(filename='log_10_4.txt',level=lg.DEBUG)
def copy_file_filter(path,ndir,ext):
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
					c=0
		if c==1:lg.info("No files with defined extension found/No Directory created")
		else:
			import shutil as sh
			n_dir = os.path.dirname(ndir)
			if not os.path.exists(n_dir):
				os.makedirs(ndir)
			npath=os.path.abspath(ndir)
			for fd,sbd,fl in os.walk(path):
				for i in fl:
					if i.split(".")[1]==ext:
						sh.copy(fd+"\\"+i,npath)
		
	else:
		lg.info("Invalid path given/Directory not Exists")
	
def main():
	if(len(argv)!=4):
		lg.info("Give Proper Input,eg-(Directory name, new Directory name,file extension for filter(.doc,.txt))")
		exit()
	
	try:
		ext=argv[3].replace(".","")
		copy_file_filter(argv[1],argv[2],ext)
	except ValueError:
		lg.warning("Invlaid Input Datatype")
	except Exception as e:
		lg.warning(e)

if __name__=="__main__":
	main()

#==============================
#Marvellous_Infosystem_Python_ML_Assignments\Marvellous_Infosystem_Assignment_10>python Assignment10_4.py Demo temp .doc
#==============================