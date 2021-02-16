# Keylogger-for-Ethical-Hackers
This is a simple keylogger python script that sends an email to itself every 120 seconds.
While the script is running, it sends email to itself the logs that are entered on the keyboard. 

## Usage
You should change "your_email" and "your_password" with your email address and password in the code.
For example send_email("test@gmail.com","test123",logs).
Before running the code, you should allow less secure apps and disable 2-step verification on your gmail account. You can change it on this [site](https://myaccount.google.com/u/1/lesssecureapps?pli=1&pageId=none).
## Required Libraries
pip install pynput
pip install smtplib
