##################### Extra Hard Starting Project ######################

import datetime as dt
import pandas
import random
import smtplib

today_date = dt.date.today()
letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = random.choice(letters_list)

with open("birthdays.csv") as bdy:
    file = pandas.read_csv(bdy)
    file["date"] = pandas.to_datetime(file[["year", "month", "day"]])
    date = pandas.Timestamp(today_date)
    if any(file[file["date"] == date]):
        filter_date = file[file["date"] == date]
        name = filter_date["name"].to_string(index= False)
        email = filter_date["email"].to_string(index= False)
        update_line = []
        with open(letter, "r") as lt:
            data = lt.read()
            updated_content = data.replace("[NAME]", name)
        with open(letter, "w") as ltt:
            ltt.write(updated_content)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            my_email = "your email"
            password1 = "your pass"
            
            connection.login(user= my_email, password= password1)
            connection.sendmail(
                from_addr= my_email, 
                to_addrs= email, 
                msg= f"Subject: Birthday Greetings\n\n{updated_content}"
            )
        










