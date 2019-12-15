import os;
from sys import *
import psutil;
import logging as lg
lg.basicConfig(filename='log_12_3.txt',level=lg.DEBUG)
def ProcessDisplay(dir_name):
	
	if not os.path.exists(dir_name):
			os.makedirs(dir_name)
	fpath=dir_name+"//"+"Running_process.txt"
	fobj = open(fpath,'w')
    #print("Running processess")
	fobj.writelines("Process_Name"+","+"P_id"+","+"Process_Username"+"\n")
	for pobj in psutil.process_iter():
			#print(pobj.username())
			#ps=str(pobj.name())+"\t"+str(pobj.pid)+"\t"#+str(pobj.Process(pobj.pid).username)
			pname=(pobj.name())
			pid=(pobj.pid)
			try:
				pun=(pobj.username())
			except Exception:
				pun="Access Denied"
			fobj.writelines(str(pname)+","+str(pid)+","+str(pun)+"\n")

	fobj.close()

def main():
	if(len(argv)!=2):
		lg.info("Give proper input,like process name eg-notepad.exe")
	try:
		#ext=argv[2].replace(".","")
			ProcessDisplay(argv[1])
		
	except ValueError as e:
			lg.warning("Invlaid Input Datatype.:",e)
	except Exception as e:
			lg.warning(e)
if __name__ == "__main__":
    main()