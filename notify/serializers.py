from .models import NotificationUser
from rest_framework import serializers
class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationUser
        fields = ('user', 'notify',)

