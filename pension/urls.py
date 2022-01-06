# from django.conf.urls import url
from django.urls import path

from . import views
from .views import PensionUserRegister, UserActivation, LoginView, ChangePasswordView

urlpatterns = [
    path('api/register/', PensionUserRegister.as_view()),
    path('api/activation/', UserActivation.as_view(), name='user-activation'),
    path('api/user_login/', LoginView.as_view(), name='user-login'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    # path('request-reset-email/', RequestPasswordResetEmail.as_view(),
    #      name="request-reset-email"),
    # path('password-reset/<uidb64>/<token>/',
    #      PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    # path('password-reset-complete', SetNewPasswordAPIView.as_view(),
    #      name='password-reset-complete')

]