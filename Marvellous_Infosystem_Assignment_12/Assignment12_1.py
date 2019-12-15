import os;
import sys;
import psutil;
import logging as lg
lg.basicConfig(filename='log_12_1.txt',level=lg.DEBUG)
def ProcessDisplay():
	fobj = open('Running_process.txt','w')
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
    ProcessDisplay()

if __name__ == "__main__":
    main()