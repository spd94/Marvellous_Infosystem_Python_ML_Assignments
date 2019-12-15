import os;
from sys import *
import psutil;
import logging as lg
lg.basicConfig(filename='log_12_2.txt',level=lg.DEBUG)
def ProcessDisplay(psname):
	plist = psutil.process_iter()
	pname=[]
	pid=[]
	pun=[]
	pcm=[]
	for p in plist:
		psn=str(p.name()).lower()
		
		if psname.lower()==psn:
			pname.append(str(p.name()))
			pid.append(str(p.pid))
			try:
				pun.append(str(p.username()))
			except Exception:
				pun.append("Access Denied")				
			try:
				pcm.append(str(p.memory_percent()))
			except Exception:
				pcm.append(str("Unable to get memory_percent"))
		
	if(len(pid)>0):
		fp=open("Process_Info.txt",'w')
		for (i,j,k,l) in zip(pname,pid,pun,pcm):
			fp.writelines(i+","+j+","+k+","+l+"\n")
		fp.close()
	else:
		lg.info("Either Process not running OR process name not matched")
		
	

def main():
	if(len(argv)!=2):
			lg.info("Give proper input,like process name eg-notepad.exe")
			exit()
	
	try:
		#ext=argv[2].replace(".","")
		ProcessDisplay(argv[1])
		
	except ValueError as e:
		print(e)
		lg.warning("Invlaid Input Datatype")
		
	except Exception as e:
		lg.warning(e)

if __name__ == "__main__":
    main()