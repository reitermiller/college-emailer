import csv
import smtplib, ssl

# open password file. no, its not encrypted.
gmail_password = open("password.txt", "r").read()

# assign variables
USER_NAME = "John Doe" # full name
HIGHSCHOOL = "Hogwarts High School" # currently enrolled highschool
CITY_STATE = "Atlantis" # city, state of above highschool
ADDRESS = "123 RealStreet LN Town, ST 12345" # address for promo mats to be sent to
SIGNATURE = "Thank you, \n \n John Doe \n johndoe@mail.lol" # email signature
EMAIL = "johndoe@mail.lol" # gmail email to send from. if you have a school-affiliated email to use and your administration doesn't care, use it to verify your highschool enrollment.

# open csv files with school emails and names

with open('emails.csv', newline='') as csvfile:
    emails = list(csv.reader(csvfile))

with open('names.csv', newline='') as csvfile:
    names = list(csv.reader(csvfile))

x = 0 #startine
i = 499 #endline

# mail funciton

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = EMAIL
        self.password = gmail_password

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()

# run mail function

ta_key = "true"
while ta_key == "true":
    if __name__ == '__main__':
        mails = (emails[x][0]).split()
        subject = ('Attending ' + (names[x][0]) + ' in the fall')
        content = ("Good Afternoon! My name is " + USER_NAME + " and I plan on attending " + (names[x][0]) + " in the fall semester of 2022. I am currently a senior at " + HIGHSCHOOL + " in " + CITY_STATE + ". I recently took a tour of your campus and it seems like a perfect fit for me. My Uncle was an alumni in 1999 and has praised your campus lifestyle, and from how he has described it, it will be great for me. I was wondering, though I'm sure you get plenty of these requests, is there a chance I could receive any promotional materials? I would love to represent school pride as early as possible. My current address is " + ADDRESS + ". I am looking forward to being a student and I am very excited to start life on your campus. \n \n" + SIGNATURE)

        mail = Mail()
        mail.send(mails, subject, content)
        # advance "x" by one for line in csv to read.
        x = x + 1
        print(x)
        # while variable 'x' (line to read in csv) is below 'i' (maximum csv line), print current line and run function again. when x>=i, stop running.
        while x>=i:
            ta_key = false
            print("Completed.")
