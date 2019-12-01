import os
def file_create_copy(path,fname):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	print(path)
	exst=os.path.exists(path)
	
	if exst:
		f = open(path, 'r')
		ctn=f.read()
		f.close()
		f=open(fname,'w+')
		f.write(ctn)
		f.close()
	else:
		print("Invalid file or path given for existing file ")
	
def main():
	fname=input("Give new File to create.: ")
	c=input("Give Existing file Name to copy to new file.:")
	try:
		file_create_copy(c,fname)
	except ValueError:
		print("Invlaid Input Datatype")
	except Exception as e:
		print(e)

if __name__=="__main__":
	main()