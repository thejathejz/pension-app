from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import ActivationSerializer, UserRegistrationSerializer, TokenGenerationSerializer, \
    ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# View for User Registration
class PensionUserRegister(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "An otp has sent to the phone number  and email verify  your account "
        else:
            data = serializer.errors
        return Response(data)


# Activation view 
class UserActivation(generics.GenericAPIView):
    serializer_class = ActivationSerializer

    def post(self, request, args, *kwargs):
        serializer = ActivationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Thank you for your OTP confirmation. Now you can login your account.",
        }, status=status.HTTP_201_CREATED)

# View for Token generation, Login view
class LoginView(TokenObtainPairView):

    permission_classes = (AllowAny,)
    serializer_class = TokenGenerationSerializer

# Change Password

class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

