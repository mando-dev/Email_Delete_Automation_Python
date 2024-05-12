import imaplib
import email
import smtplib
from email.header import decode_header

# Login credentials
email_address = "gmail.com" #put your own email here, 
password = "kkky " #make sure you create an app password 

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login(email_address, password)
mail.select('inbox')  # Connect to the inbox

# Search for specific emails with a specific subject
subject = "Security alert"
status, email_ids = mail.search(None, f'(SUBJECT "{subject}")')

# fetch n delete the emails
for email_id in email_ids[0].split():
    # mark the email for delettion without checking the subject again
    mail.store(email_id, '+FLAGS', '\\Deleted')

# Permanently remove the deleted emails
mail.expunge()

# Close the connection
mail.logout()
