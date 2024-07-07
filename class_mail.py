import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import join
import class_log
headerLog={}

def buildMail(toMail,ccMail,testo,oggetto,attachFile):
    returnObj={
        "to":toMail,
        "cc":ccMail,
        "testo":testo,
        "oggetto":oggetto,
        "toAttach":[]
    }
    for att in attachFile:
        filename =att
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())       
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        returnObj["toAttach"].append(part)
    return returnObj

def multiSend(byCfg,byMailMsg):

    attemp=0
    sentMail=False
    while sentMail != True and attemp < byCfg["retry"]:        
        startDate=class_log.getDateMillis()
        sentMail=sendMail(byCfg,byMailMsg)
        attemp+=1
        if sentMail==False:
            class_log.printRowLog("SEND_MAIL","OK","OK",startDate,attemp)
        else:            
            class_log.printRowLog("SEND_MAIL","KO","KO",startDate,attemp)
    return sentMail

def sendMail(byCfg,byMailMsg):
    server=byCfg["smtp"]
    msg = MIMEMultipart()
    msg['From'] = byCfg["sender"]
    msg['To'] = ",".join(byMailMsg["to"])
    msg['Cc'] = ', '.join(byMailMsg["cc"])
    msg['Bcc'] = ', '.join(byCfg["bcc"])
    msg['Subject'] = byMailMsg["oggetto"]
    msg.attach(MIMEText(byMailMsg["testo"], 'plain'))   
   
    try: 
        for attc in byMailMsg["toAttach"]:
            msg.attach(attc)
        server = smtplib.SMTP(byCfg["smtp"], byCfg["port"])
        server.starttls()
        server.login(str(os.getenv(byCfg["user"])), str(os.getenv(byCfg["pass"])))
        text = msg.as_string()
        server.sendmail(byCfg["sender"], byMailMsg["to"], text)
        server.quit()
        return True
    except:
        return False
    