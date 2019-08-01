import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'jeanbaptisteservais26@gmail.com'
msg['To'] = 'jb26400@hotmail.fr'
msg['Subject'] = 'Le sujet de mon mail' 
message = 'Bonjour !'
path = r'C:\Users\jeanbaptiste\Desktop\site_travail\environement_virtuel\projetto\app_email\function_email.py'
msg.attach(MIMEText(path))



msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()

mailserver.login('jeanbaptisteservais26@gmail.com', 'onsaitjamais')

mailserver.sendmail('jb26400@hotmail.fr',
                    'jb26400@hotmail.fr',
                    msg.as_string())
mailserver.quit()
