import datetime
import random
import smtplib

import pandas

MY_EMAIL = "zakihorakhsh2028@gmail.com"
PASSWORD = "izbt umrb wxek jfxb"

now = datetime.datetime.now()

month = now.month
day = now.day

today_date = (month, day)

data = pandas.read_csv("birthdays.csv")

########################

letter = open(f"letter_templates/letter_{random.randint(1,3)}.txt")
letter_to_send = letter.read()

########################

for index, row in data.iterrows():
    email = row["email"]
    name = row['name']
    month = row['month']
    day = row['day']

    birthday = (month, day)

    if today_date == birthday:
        name_to_insert = name
        letter_with_name = letter_to_send.replace("[NAME]", name_to_insert)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"subject:Happy Birthday!\n\n{letter_with_name}")
    else:
        print("Failure")
