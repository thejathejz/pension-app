from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from rest_framework import generics,mixins,status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import ActivationSerializer, UserRegistrationSerializer, TokenGenerationSerializer, \
    ChangePasswordSerializer,ProfileSerializer,  ServiceStatusSerializer,  BookAppointmentSerializer, ResendOtpSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import Profile


# Django Channels
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
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

    def post(self, request, *args, **kwargs):
        serializer = ActivationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Thank you for your OTP confirmation. Now you can login your account.",
        }, status=status.HTTP_201_CREATED)
class ResendOtp(generics.GenericAPIView):
    serializer_class = ResendOtpSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResendOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            
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




class UserProfile(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    # def post(self, request, *args, **kwargs):
    #     serializer = ProfileSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     return Response({
    #         "user": serializer.data,
    #         "message": "your profile has been created successfully",
    #     }, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = ProfileSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = Profile.objects.create(
            user = request.user,
            #DOB = serializer.validated_data['DOB'],
            gender = serializer.validated_data['gender'],
            address = serializer.validated_data['address'],
            #email = serializer.validated_data['email'],
            
            )
            user.save()
            data['response'] = 'fields added sucessfuly'
        else:
            data = serializer.errors
        return Response(data)
    def put(self, request):
        user = Profile.objects.get(user = request.user)
        data = {}
        serializer = ProfileSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'profile updated sucessfully'
            return Response(data)   
        else:
            data = serializer.errors
        return Response(data)

class ServiceStatus(generics.GenericAPIView):
    serializer_class =  ServiceStatusSerializer

    def post(self, request, *args, **kwargs):
        serializer =  ServiceStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Employee service status",
        }, status=status.HTTP_201_CREATED)


class BookAppointment(generics.GenericAPIView):
    serializer_class = BookAppointmentSerializer

    def post(self, request, *args, **kwargs):
        serializer = BookAppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializer.data,
            "message": "Employee Appointment",
        }, status=status.HTTP_201_CREATED)

