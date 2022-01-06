from django.core.mail import send_mail
from twilio.rest import Client

def send_otp_by_email(otp):
    print("sending")
    subject = 'Please Confirm Your Account'
    message = 'Your 6 Digit Verification Pin: {}'.format(otp)
    email_from = 'theja@techversantinfo.com'
    recipient_list = ['theja@techversantinfo.com', ]
    send_mail(subject, message, email_from, recipient_list)

def send_otp_by_sms(otp, phone_number):
    # twilio code
    account_sid = 'ACf7ea714175f05c105816d939bc81c035'
    auth_token = 'b21f1eacf4890b8327ebe021ec55ff5b'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Hi, your OTP is {otp}. Great job',
        from_='+14843098241',
        #to='+918086785290',
        to=phone_number,
    )

    print(message.sid)