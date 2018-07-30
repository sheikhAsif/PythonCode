import smtplib
import getpass

def main():

    print("\n\n******Welcome******")
    print("\nWelcome to Email Service\n")
    print("Enter your login details -\n")

    gmail_user = input("\n\nEmail : ")
    gmai_password = getpass.getpass("Password : ")
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465) #binding
        print("\n\nConnection Established")
        server.ehlo() #handshake
        server.login(gmail_user,gmai_password)
        print("\n\nYou have successfully logged in your account ",gmail_user)
    except Exception as e:

        print("\n\nError!!! in Connection")
        print(e)
        exit(0)
    sent_from = gmail_user
    i = int(input("\n\nEnter no. of recipients -"))
    print("\n\nEnter Recipients Email Addresses - \n")
    to = []
    for k in range(i):
        to.append(input())
        print()

    subject = input("\n\nPlease Type in Subject of the mail -")
    print("\n\nType in your message (type in EOF to FINISH)\n\n")

    message=[]
    while True:
        msg = input()
        if msg.upper() == 'EOF' :
            break
        else :
            message.append(msg)
    print("\n\nMessage is ready for delivery\n\n")
    body = '\n'.join(message)
    email_text = """From:%s
    To=%s
    Subject=%s
    body=%s
    """%(sent_from,",".join(to),subject,body)
    try:
            print("\n\nEmail sending is in processing -\n")
            server.sendmail(sent_from,to, email_text)
            server.close()
    except Exception as e:
            print("\nSomething went wrong...",e)
    else:
            print("\nMessage Delivered to -\n")
            for i in to:
                print(i)
                print()

            print("\n\n**********Exiting*********\n\n")
            print("\n\nThanks for using mail service \n\n")
if __name__=="__main__":
    main()
