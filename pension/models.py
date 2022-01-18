from django.contrib.auth.models import User
from django.db import models
from twilio.rest import Client
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail




# Model for User Registration
class UserAccountDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    otp = models.IntegerField(default=00000)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# Model for User Registration

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "sandra@techversantinfo.com",
        # to:
        [reset_password_token.user.email]
    )





class Profile(models.Model):
    GENDER = (
        ('M', 'male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER)
    #date = models.DateField()
    address = models.CharField(max_length=120, blank=False)
    #email = models.EmailField(unique=True, db_index=True)
    def __unicode__(self):
        return u'Profile of user: {0}'.format(self.user.email)
    def __str__(self):
        return self.user.username

class ServiceStatus(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Retired', 'Retired'),
    )

    status = models.CharField(max_length=8, choices=STATUS)
    def __unicode__(self):
        return u'Employee service status: {0}'.format(self.user.status)


class BookAppointment(models.Model):

    date= models.DateField()
    time = models.TimeField()
    def __unicode__(self):
        return u'Your date and time slot for the verification: {0}'.format(self.user.status)




