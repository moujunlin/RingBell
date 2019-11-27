import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import BellRingMatch as m
import email_contents as c

mail_host = 'smtp.gmail.com'
mail_user = 'empowerchange.peerlistener@gmail.com'
mail_pass = 'EC123456789'
sender = 'empowerchange.peerlistener@gmail.com'

def sendGmail(html_content,receiver,title):
    message = MIMEMultipart('alternative')
    message['Subject'] = title 
    message['From'] = sender 
    message['To'] = receiver  

    text = ""
    html = html_content
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1) # text must be the first one
    message.attach(part2) # html must be the last one

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587) 
        #smtpObj.connect(mail_host,25)
        smtpObj.ehlo()
        smtpObj.starttls()

        smtpObj.login(mail_user,mail_pass) 
    
        smtpObj.sendmail(
            sender,receiver,message.as_string()) 

        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e)

def generate_email_content(bell_ringer, listener, time):
    succeed_title = '解聆人线上倾听 (匹配成功 :)'
    fail_title = '解聆人线上倾听 (匹配失败 :('
    #------bell ringer email content------
    if listener != -1:
        br_content = c.html_br_content_success
        br_content =  br_content.replace("@X",bell_ringer.name,1)
        br_content =  br_content.replace("@X",listener.name,1)
        br_content =  br_content.replace("@X",time,1)
        title = succeed_title
    else:
        br_content = c.html_br_content_fail
        br_content =  br_content.replace("@X",bell_ringer.name,1)
        title = fail_title

    #------listener email content------
    if listener != -1:
        l_content = c.html_l_content
        l_content =  l_content.replace("@X",listener.name,1)
        l_content =  l_content.replace("@X",bell_ringer.name,1)
        l_content =  l_content.replace("@X",time,1)
        l_content =  l_content.replace("@X",bell_ringer.name,1)
        l_content =  l_content.replace("@X",bell_ringer.name,1)
        l_content =  l_content.replace("@X",bell_ringer.email,1)
        l_content =  l_content.replace("@X",bell_ringer.topic,1)
        title = succeed_title
    else:
        l_content = -1
    return br_content,l_content,title