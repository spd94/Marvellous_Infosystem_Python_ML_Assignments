import os
def file_word_occurance(path,c):
	flg=os.path.isabs(path)
	if flg == False:
		path=os.path.abspath(path)
	#print(path)
	exst=os.path.exists(path)
	
	if exst:
		f = open(path, 'r')
		ctn=f.read()
		f.close()
		ct=0
		for i in ctn.split():
			if i==c:
				ct+=1
		if ct:
			print("No. of Occurances.:",ct)
		else:
			print("No Occurance found")
	else:
		print("Invalid file or path given for existing file ")
	
def main():
	fname=input("Give File name.: ")
	c=input("Give word to find its occurance.:")
	try:
		file_word_occurance(fname,c)
	except ValueError:
		print("Invlaid Input Datatype")
	except Exception as e:
		print(e)

if __name__=="__main__":
	main()