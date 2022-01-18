# from django.conf.urls import url
from django.urls import path

from . import views
from .views import PensionUserRegister, UserActivation, LoginView, ChangePasswordView,UserProfile,ServiceStatus,BookAppointment,ResendOtp
urlpatterns = [
    path('api/register/', PensionUserRegister.as_view()),
    path('api/activation/', UserActivation.as_view(), name='user-activation'),
    path('api/Resend_Otp/', ResendOtp.as_view(), name='Resend_Otp'),
    path('api/user_login/', LoginView.as_view(), name='user-login'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/userprofile/', UserProfile.as_view(), name='userprofile'),
    path('api/service-status/', ServiceStatus.as_view(), name='service-status'),
    path('api/book-appointment/', BookAppointment.as_view(), name='book-appointment'),
    
]