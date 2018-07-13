
import smtplib
import time

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
#ccaddr = prompt("CC:")
toaddrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
'''
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
'''
#msg = ("From: Security Compliance(donaldt@us.gov) \r\nCC: %s \r\nTo: %s\r\n\r\n" % (ccaddr,", ".join(toaddrs)))#use this to hide the actual sender of mail
#msg = ("From: Edward Snowden \n \r\nTo: %s\r\n\r\n Subject: Mass Surveillance\n " % (", ".join(toaddrs)))
msg = ("From: Edward Snowden  \r\nTo: %s \r\nSubject: Mass Surveillance\r\n\r\n " % (", ".join(toaddrs)))
'''
while True:
	try:
		#line = input()
		
	except EOFError:
		break
	if not line:
		break
	msg = msg + line
'''
line = "Hi,\n As you are aware that situation in tense in South America regarding the new world order of Bit Coin devaluation, our prestigious (BHG) Black Hat Group wanted to have your service. We would like you put entire South America on Surveillance please go ahead and take the root access to NSA California.\n\nCheers\nEdward "
msg = msg + line
	
print("Message length is", len(msg))
print("Sleeping for a while")
time.sleep(10)

server = smtplib.SMTP('Eamil Exchange Server',465)
server.set_debuglevel(1)
user = 'username'
pwd = 'password'
server.ehlo()
server.starttls()
server.ehlo
server.login(user,pwd)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()	