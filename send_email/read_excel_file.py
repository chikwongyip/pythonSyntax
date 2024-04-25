# coding:utf-8
# 读取excel文件sheet1内容
from email import encoders
from email.mime.base import MIMEBase

import pandas as pd
import smtplib

# 读取Excel文件
excel_file = 'Book1.xlsx'
df = pd.read_excel(excel_file, sheet_name='Sheet1')
print(df)


# 发送邮件并带附件
def send_email(subject, content, to_email):
    # 邮件内容
    message = f"Subject: {subject}\n\n{content}"

    # 把附件添加到邮件中
    with open('Book1.xlsx', 'rb') as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename= {excel_file}')
        message.attach(p)

    # 发送邮件
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail('your_email@example.com', to_email, message.as_string())
