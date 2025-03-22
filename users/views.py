from rest_framework.decorators import api_view
from rest_framework import status
from random import choices
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import ConfirmModel
from .serializers import UserRegisterSerializer, UserConfirmSerializer, UserAuthSerializer
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED, data={'User credentials are wrong!'})


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    email = serializer.validated_data.get('email')

    user = User.objects.create_user(username=username, password=password, email=email, is_active=False)

    code = ''.join(choices('0123456789', k=6))
    ConfirmModel.objects.create(user=user, code=code)
    send_mail(
        'Registration code',
        message=code,
        from_email='<EMAIL>',
        recipient_list=[user.email]
    )
    return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def confirm_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    code = serializer.validated_data.get('code')
    email = serializer.validated_data.get('email')

    try:
        confirm_record = ConfirmModel.objects.get(user__email=email, code=code)
    except ConfirmModel.DoesNotExist:
        return Response({'error': 'Code not found!'}, status=status.HTTP_404_NOT_FOUND)

    confirm_record.user.is_active = True
    confirm_record.user.save()
    confirm_record.delete()
    return Response({'Message': 'User confirmed successfully'}, status=status.HTTP_200_OK)