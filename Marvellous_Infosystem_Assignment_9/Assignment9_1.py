import os
def Directory_checker(path):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	exst=os.path.isdir(path)
	
	if exst:
		for fd,sbd,fl in os.walk(path):
			print("Folder.:",fd)
						
			for i in sbd:
				print("Sub-Folder.:",i)
			for i in fl:
				print("|\n| ")
				print("Files.:",i)
			print("")
	else:
		print("Invalid Directory path")
	
def main():
	c=input("Give Directory Name.:")
	try:
		Directory_checker(c)
	except ValueError:
		print("Invlaid Input Datatype")
	except Exception:
		print("Invlaid Input")

if __name__=="__main__":
	main()