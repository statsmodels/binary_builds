#!/usr/bin/python
"""
Gets current git revision and renames files.

Sends e-mail when files are done updating with current uploaded versions.
"""
import smtplib
import base64
from email.MIMEText import MIMEText
from rename_binaries import git_version

with open('C:\Users\skipper\statsmodels\gmail.txt') as f:
    pwd = f.readline().strip()
gmail_pwd = base64.b64decode(pwd)

email_name ='statsmodels.dev' + 'AT' + 'gmail' +'.com'
email_name = email_name.replace('AT','@')

to_email = [email_name, ('josef.pktd' + 'AT' + 'gmail' + '.com').replace('AT',
    '@')]
#to_email = [email_name]

def email_me(git_rev):
    message = """
    Windows binaries uploaded successfully for git revision %s.

    https://github.com/statsmodels/statsmodels/commit/%s
    http://statsmodels.sourceforge.net/binaries/
    """ % (git_rev[:7], git_rev)
    subject = "Windows Binaries Uploaded"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = email_name
    msg['To'] = email_name

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email_name, gmail_pwd)
    server.sendmail(email_name, to_email, msg.as_string())
    server.close()

if __name__ == "__main__":
    git_rev = git_version()
    email_me(git_rev)
