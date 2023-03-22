import smtplib

my_email = "will.jordan0788@gmail.com"
password = "hotdog1()"

# Must modify the security settings for the email host server.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="wjordan1@kent.edu",
        msg="Subject:Hello\n\nThis is the body of my email.")


connection.close()