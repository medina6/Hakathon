from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import RegistrationSerializer, ActivationSerializer, \
    LoginSerializer, ChangePasswordSerializer, ForgotPasswordSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            Successfully registered!
            The mail with activation is sent to you.
            """
            return Response(message)

class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('You are successfully registered')


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.create_new_password()
            return Response('New password has been sent to your email')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data,
                                              context={'request' : request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Password successfully updated')