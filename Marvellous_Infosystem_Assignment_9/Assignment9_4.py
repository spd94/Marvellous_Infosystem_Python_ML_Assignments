import os
def file_compare(path,fname):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	#print(path)
	exst=os.path.exists(path)
	
	if exst:
		f = open(path, 'r')
		ctn1=f.read()
		f.close()
		f=open(fname,'r')
		ctn2=f.read()
		f.close()
		#print(type(ctn2))
		if ctn1==ctn2:
			print("Success")
		else:
			print("Failure")
	else:
		print("Invalid file or path given for existing file ")
	
def main():
	fname=input("Give First File name.: ")
	c=input("Give Second File name to compare to first.:")
	try:
		file_compare(fname,c)
	except ValueError:
		print("Invlaid Input Datatype")
	except Exception as e:
		print(e)

if __name__=="__main__":
	main()