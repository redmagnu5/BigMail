import smtplib
import base64
import cmd
import argparse
import sys
import yaml
import getpass
from os import path
from termcolor import colored
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from smtplib import SMTP, SMTPException, SMTPAuthenticationError

parser = argparse.ArgumentParser(description="")
parser.add_argument('-p', help='path to binary payload attachment')
parser.add_argument('-v', action='store_true', help='verbose')
args = parser.parse_args()

with open('config.yaml') as stream:
    yamlLoad = yaml.safe_load(stream)

counter = []
Domain = []
Port = []
List = []
User = []
Password = []
Sender = yamlLoad['SendInfo']['Sender']

class BigMail():
    def __init__(self):
        self.banner()
        self.Config()
        self.Import(List[0])
        print(colored(str(len(counter)) + " email(s) have been sent!", "green"))
        print(colored("F I N", "blue"))

    def banner(self):
        print(colored("""
                    ________________________________
                     ____  _       __  __       _ _
                    | __ )(_) __ _|  \/  | __ _(_) |
                    |  _ \| |/ _` | |\/| |/ _` | | |
                    | |_) | | (_| | |  | | (_| | | |
                    |____/|_|\__, |_|  |_|\__,_|_|_|
                    ________ |___/ Mass Mailer _____
                     Author: redmagnu5@github.com

       Email list must be a basic text file (.txt) and have the
       following structure:

                            user@domain
                            user2@domain
                            user3@domain
                              .....

        """, "green"))
        print(colored("""
                  PLEASE DO NOT USE FOR SPAMMING \n
        """, "red"))

    def Config(self):
        Domain.append(input(colored("Domain of mail server: ", "white")))
        Port.append(input(colored("SMTP port: ", "white")))
        User.append(input(colored("Username for mail server: ", "white")))
        Password.append(getpass.getpass(colored("Password for mail server: ", "white")))
        List.append(input(colored("Path to recipient list: ", "white")))

    def Import(self, file):
        extension = path.splitext(file)[1]
        if extension == '.txt':
            with open(file, 'r') as fileStream:
                lines = fileStream.readlines()
                for index in range(0, len(lines)):
                    line = lines[index].replace("\n", "")
                    send = self.createMessage(line)
                    self.Send(line, send)
        else:
            print(colored('File type not supported: ' + extension, 'red'))

    def createMessage(self, recipients):
        msg = MIMEMultipart()
        msg['Subject'] = yamlLoad['SendInfo']['Subject']
        msg['From'] = Sender
        msg['To'] = recipients

        if args.v:
            print(colored("Delivering to " + recipients + ", from: " + sender, "yellow"))

        data = MIMEText(yamlLoad['SendInfo']['Body'], 'html')
        msg.attach(data)

        if args.v:
            print(colored("Message to be delivered: \n", "yellow"))
            print(colored(data, "white", "on_blue"))

        if args.p:
            try:
                payloadPath = args.p
                fp = open(payloadPath, 'rb')
                attach = MIMENonMultipart('application', 'exe')
                payload = base64.b64encode(fp.read()).decode('ascii')
                attach.set_payload(payload)
                attach['Content-Transfer-Encoding'] = 'base64'
                nameFile = yamlLoad['SendInfo']['Attachment']
                attach.add_header('Content-Disposition', 'attachment', filename = nameFile)
                msg.attach(attach)
                fp.close()

                if args.v:
                    print(colored("Name of attachment to be sent: " + nameFile, "yellow"))

            except:
                print(colored("Incorrect file path \n", "yellow"))

        if args.v:
            print(colored("Message created successfuly \n", "green"))

        message = msg.as_string()
        return message

    def Send(self, recipients, msg):
        try:
            s = smtplib.SMTP(Domain[0], Port[0])
            s.connect(Domain[0], Port[0])
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(User[0], Password[0])
            s.sendmail(Sender, recipients, msg)
            counter.append(1)
            if args.v:
                print(colored("Message sent \n", "green"))
            s.quit()

        except SMTPException:
            print("An exception has occured")
        except SMTPAuthenticationError:
            print("Incorrect user/password")
        except:
            print(colored("Error: Unable to send message \n", "red"))



B = BigMail()
