from sys import *
import os
import hashlib
import logging as lg
import time
lg.basicConfig(filename='log_11_4.txt',level=lg.DEBUG)

def Dup_Del_by_chksum_Time(path):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	#print(path)
	exst=os.path.exists(path)
	
	if exst:
		c=1
		file_chk=dict()
		for fd,sbd,fl in os.walk(path):
			for i in fl:
				#if i.split(".")[1]==ext:
					#print(i)
				abs=fd+"\\"+i
				vl=(hashlib.md5(open(abs, 'rb').read()).hexdigest())
				file_chk[i]=vl
				c=0
				
		flipped = {}
		for key, value in file_chk.items(): 
				if value not in flipped: 
					flipped[value] = [key] 
				else: 
					flipped[value].append(key)
		f=open("Log4.txt","w+")	
		#print(str(flipped))
		for i in flipped:
			v=flipped[i]
			if len(v)>1:
				for i in v:
					f.write("Deleted file\n")
					fp=os.path.abspath(path+"\\"+i)
					#print(fp)
					os.remove(fp)
					f.write(i+"\n")
				s="-"*5
				f.write(s+"\n")
		f.close()
				
				
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
		start_time = time.time()
		Dup_Del_by_chksum_Time(argv[1])
		x=time.time() - start_time
		print("Execution time.:",x,"Seconds")
		
	except ValueError:
		lg.warning("Invlaid Input Datatype")
		
	except Exception as e:
		lg.warning(e)
		

if __name__=="__main__":
	main()