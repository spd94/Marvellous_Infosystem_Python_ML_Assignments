import os
def file_display(path):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	print(path)
	exst=os.path.exists(path)
	
	if exst:
		f = open(path, 'r')
		print(f.read())
		f.close()
	else:
		print("Invalid file path")
	
def main():
	c=input("Give File Name.:")
	try:
		file_display(c)
	except ValueError:
		print("Invlaid Input Datatype")
	except Exception:
		print("Invlaid Input")

if __name__=="__main__":
	main()