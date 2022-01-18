from asgiref.sync import async_to_sync
from django.shortcuts import render
from .serializers import NotificationSerializer
from .models import NotificationUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from channels.layers import get_channel_layer
# Create your views here.
class Notification(APIView):
    serializer_class= NotificationSerializer

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
            #     user = self.request.user
            #     notification = serializer.data['notification']
                serializer.save()
                user= serializer.data['user']
                username = User.objects.get(id=user).username
                channel_layer = get_channel_layer()
                notification = serializer.data['notify']
                notification_objs = models.Notification.objects.filter(user_has_seen =False, user= user).count()
                data = {'count':notification_objs,'current_notifications':notification}
                

                async_to_sync(channel_layer.send)(
                    username,{
                        'type':'send_notification',
                        'value':data
                    }
                )
        except:
            data= serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)
class Notificationrec(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        notification = "no notification"
        username = request.user.username
        print(username)
        channel_layer = get_channel_layer()
        try:
            notification = async_to_sync(channel_layer.receive)(username)
            print(notification)
        except Exception as e:
            print(e)
        return Response(notification)



