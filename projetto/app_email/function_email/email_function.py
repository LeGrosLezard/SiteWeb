import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email import encoders


def email(addresse, sujet,
          message_recruteur,
          path_cv, path_motivation):
    
    msg = MIMEMultipart()
    msg['From'] = 'jeanbaptisteservais26@gmail.com'
    msg['To'] = addresse
    msg['Subject'] = sujet
    message = message_recruteur


    nom_fichier = "Curriculum vitae.pdf"
    piece = open(path_cv, "rb")    ## Ouverture du fichier
    part = MIMEBase('application', 'octet-stream')    
    part.set_payload((piece).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
    msg.attach(part)    



    nom_fichier1 = "lettre de motivation.pdf"
    piece1 = open(path_motivation, "rb")    ## Ouverture du fichier
    part1 = MIMEBase('application', 'octet-stream')    
    part1.set_payload((piece1).read())
    encoders.encode_base64(part1)
    part1.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier1)
    msg.attach(part1)    


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












