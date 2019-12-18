import os
from sys import *
import psutil
import datetime
import schedule as sch
import time
import logging as lg
lg.basicConfig(filename='log_13.txt',level=lg.DEBUG)

def md5(fname):
	import hashlib
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def ProcessDisplay(dir_name):
	chk_sum=[]
	tot_files=0
	dup_files=0
	del_files=[]
	
	sc = datetime.datetime.now()
	
	for i,j,k in os.walk(dir_name):		
		for fname in k:
			dirf=dir_name+"//"+fname
			fn=os.path.abspath(dirf)
			#fpb=open(fn, 'rb')
			#chks=hashlib.md5(fpb).hexdigest()
			chks=md5(fn)
			#fpb.close()
			tot_files+=1
			if chks not in chk_sum:
				chk_sum.append(chks)
			else:
				del_files.append(fn)
				dup_files+=1
	
	for fn in del_files:
		os.remove(str(fn))
	dt = datetime.datetime.now()
	mk_dir="Marvellous"
	if not os.path.exists(mk_dir):
		os.makedirs(mk_dir)
	fn=str(mk_dir+"//"+"log"+str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)+"_"+str(dt.hour)+"-"+str(dt.minute)+"-"+str(dt.second)+".txt")
	fp=open(fn,'w')
	for i in del_files:
		fp.writelines(str(os.path.relpath(i))+"\n")
	fp.close()
	return fn,sc,tot_files,dup_files
		
def is_connected():
	try:
		import socket
		socket.create_connection(("www.google.com", 80))
		return True
	except OSError:
		pass
	return False

def send_email(logf,sct,tf,df,email_id):
	if is_connected():
		import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText
		from email.mime.base import MIMEBase
		from email import encoders
		sender = "abc@gmail.com" #enter ur gmail

		to = email_id
		data = MIMEMultipart()
		data['From'] = sender
		data['To'] = to
		data['Subject'] = "This email sent by program about Duplicate file log report "
		body = str("Starting time of scanning : "+str(sct)+"\n"+"Total number of files scanned : "+str(tf)+"\n"+"Total number of duplicate files found : "+str(df))
		data.attach(MIMEText(body, 'plain'))
		filename = os.path.basename(logf)
		attachment = open(os.path.abspath(logf), "rb")
		p = MIMEBase('application', 'octet-stream')
		p.set_payload((attachment).read())
		encoders.encode_base64(p)
		p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		data.attach(p)
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(sender, "Passwd") #enter ur password
		text = data.as_string()
		s.sendmail(sender, to, text)
		s.quit()
	else:
		lg.info("Failed to send email,No internet Connection")

def Do_jobs(dir,email):
		logf,sct,tf,df=ProcessDisplay(dir)
		send_email(logf,sct,tf,df,email)
def main():
	if(len(argv)!=4):
		lg.info("Give proper input,like Directory_Path(E:/Data/Demo),time in min.(50) and email_id(marvellousinfosystem@gmail.com)")
		exit()
	try:
			if not os.path.exists(os.path.abspath(str(argv[1]))):
				lg.warning("Give Proper and absolute path of directory")
				exit()
			if not int(argv[2])>0 :
				lg.warning("Give time in number(minutes) greater than 0")
				exit()
			email=argv[3]
			
			import re
			regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
			if(re.search(regex,email)):
					#Do_jobs()
				sch.every(int(argv[2])).minutes.do(Do_jobs,dir=argv[1],email=email)
				while True:
					sch.run_pending()
					time.sleep(1)
			else:
				lg.warning("Give proper email_id")
				exit()
		
	except ValueError as e:
			lg.warning("Invlaid Input Datatype.:",e)
	except Exception as e:
			lg.warning(e)
	
if __name__ == "__main__":
	main()