from django.urls import path
from . views import Notification, Notificationrec
urlpatterns = [
    path('api/notifications/', Notification.as_view(), name="notifications"),
    path('api/notificationrec/', Notificationrec.as_view(), name="Notificationrec"),
]