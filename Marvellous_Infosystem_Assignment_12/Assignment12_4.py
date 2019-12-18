import os
from sys import *
import psutil;
import logging as lg
lg.basicConfig(filename='log_12_4.txt',level=lg.DEBUG)
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
	return fpath
	
def is_connected():
	try:
		import socket
		socket.create_connection(("www.google.com", 80))
		return True
	except OSError:
		pass
	return False

def send_email(rp,email_id):
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
		data['Subject'] = "This email sent by program about process log report "
		import time
		localtime = time.asctime( time.localtime(time.time()) )
		body = "This script generated on, "+localtime
		data.attach(MIMEText(body, 'plain'))
		filename = "Process_log.txt"
		attachment = open(os.path.abspath(rp), "rb")
		p = MIMEBase('application', 'octet-stream')
		p.set_payload((attachment).read())
		encoders.encode_base64(p)
		p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		data.attach(p)
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(sender, "Enter ur Password")
		text = data.as_string()
		s.sendmail(sender, to, text)
		s.quit()
	else:
		lg.info("No internet Connection")
	
	

def main():
	if(len(argv)!=3):
		lg.info("Give proper input,like process name (eg-notepad.exe) and email id(eg-abc@xyz.com)")
		exit()
	try:
			email=argv[2]
			rp=0
			import re
			regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
			if(re.search(regex,email)):  
					rp=ProcessDisplay(argv[1])
					if rp!=0:
						send_email(rp,argv[2])
					else:
						lg.warning("Not Able to send email")
			else:
				lg.warning("Give proper email_id")
				exit()
		
	except ValueError as e:
			lg.warning("Invlaid Input Datatype.:",e)
	except Exception as e:
			lg.warning(e)
	
if __name__ == "__main__":
	main()