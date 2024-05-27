from datetime import datetime, timedelta
import pyotp
import os
# from twilio.rest import Client
import smtplib
import traceback
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from  .models import User
def authenticate(request, username=None, password=None):
        print(username, password)
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user

            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
def send_otp( request):
    totp= pyotp.TOTP(pyotp.random_base32(), interval= 600)
    otp = totp.now()
    # request.session['otp_secret_key'] = totp.secret
    # valid_date = datetime.now() + timedelta(minutes=1)
    # request.session['otp_valid_date'] = str(valid_date)
    print(otp)
    return otp, totp.secret


def sendEmail(request, recipient_list, message, subject):



    message= f"""Hello there, 
Thank you for joining femmecare. 
{message}.
    """
    from_email = 'nikitaban24@gmail.com'
    password = 'xwqd ejit agls vgpk'
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()  # setting the ESMTP protocol
    smtp_server.starttls()  # setting up to TLS connection
    smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()

    try:
        smtp_server.login(from_email, password)  # logging into out email id
        send_mail(subject, message, from_email, recipient_list)
        smtp_server.quit()  # terminating the server
        return "success"
    
    except Exception as e:
        traceback.print_exc()
        return "unsuccess"