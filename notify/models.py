from django.db import models
from django.contrib.auth.models import User

class NotificationUser(models.Model):
    # custom field example
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify = models.TextField(max_length=20)
    isseen = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
