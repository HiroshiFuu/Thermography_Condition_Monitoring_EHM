import smtplib
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-t', '--recipient', required=True, help='Recipient e-mail address') 
ap.add_argument('-s', '--subject', required=True, help='E-mail subject') 
ap.add_argument('-b', '--body', required=True, help='E-mail body') 
args = vars(ap.parse_args())

recipient = args['recipient']
gmail_user = 'HiroshiFuu@gmail.com'
gmail_pwd = 'Hir0shiFuu'
FROM = 'HiroshiFuu@gmail.com'
TO = recipient if type(recipient) is list else [recipient]
SUBJECT = args['subject']
TEXT = args['body']

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_user, gmail_pwd)
	server.sendmail(FROM, TO, message)
	server.close()
	print 'successfully sent the mail'
except:
	print "failed to send mail"
