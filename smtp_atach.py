import smtplib
import base64
import getpass

print("\nWelcome to attachment send service")
print("\n\nPlease Enter your login details -\n")

sender = input("Email Address : ")
password = getpass.getpass("Password : ")

print("\n\n****Trying to logging you in your account****")

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(sender,password)
except Exception as e:
    print("\n\nError in login !!",e)
    exit(0)
else:
    print("\n\n******Your login is sucessfull******")

filename = input("\n\nEnter full path to your file which you want to send as attachment \n(remember path should be like c://some//dir//filename and that should be only text file) -\n\n")

try:
    f = open(filename,"rb")
except Exception as e:
    print("\n\nError!!",e)
    exit(0)
else:
    filecontent = f.read()
encodedcontent = base64.b64encode(filecontent)

n = int(input("\n\nEnter no. of recipients-"))
print("\n\nType in recipients email addressess (each in new line)\n\n")

rec=[]
for i in range(n):
    rec.append(input())

rcv = ','.join(rec)
marker = "AUNIQUEMARKER"
subject = input("\n\nSubject:")

print("\n\n*****Message - (Type EOF to quit typing)\n\n")

msg = []

while True:
    k = input()
    if k.upper() == 'EOF':
        break
    else:
        msg.append(k)
body = "\n".join(msg)
print("\n\n***Message is saved ***\n\n")

header1 = """From:%s
TO:%s
Subject=%s
MIME-Version:1.0
Content-type:multipart/mixed;boundary=%s--%s"""%(sender,rcv,subject,marker,marker)

header2 = """Content-type:text/plain
Content-transfer-Encoding:8bit
%s--%s"""%(body,marker)

header3 = """Content-Type:  multipart/mixed;name = \"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s
%s
--%s--"""%(filename,filename,encodedcontent,marker)

message = header1+header2+header3
print(message)

print("\n\n*****Trying to send your message with attachment*****\n\n")
try:
    server.sendmail(sender,rcv,message)
    server.close()
except Exception as e:
    print("\n\nError in sending mail as -\n!!",e)
    exit(0)
else:
    print("\n\nyour mail is successfully Delivered\n\n")
print("Thanks for using our mail services\n\n\n")
