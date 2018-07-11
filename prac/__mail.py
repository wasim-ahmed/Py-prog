'''
from smtplib import SMTP
with SMTP("https://blrexchcas003.techmahindra.com/mapi/emsmdb/?MailboxId=6daa3959-3cf7-4a8b-aae7-a85c9840e659@techmahindra.com",25) as smtp:
	print(smtp.noop())
	WA00434454@TechMahindra.com
	blrexchmbx001.techmahindra.com
'''

import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))

server = smtplib.SMTP('blrexchmbx001.techmahindra.com',465)
server.set_debuglevel(1)
user = 'username'
pwd = 'password'
server.ehlo()
server.starttls()
server.ehlo
server.login(user,pwd)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()	
