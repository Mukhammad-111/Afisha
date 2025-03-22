from rest_framework import serializers


class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()
    email = serializers.EmailField()


class UserAuthSerializer(UserBaseSerializer):
    pass

class UserRegisterSerializer(UserBaseSerializer):
    pass


class UserConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    email = serializers.EmailField()