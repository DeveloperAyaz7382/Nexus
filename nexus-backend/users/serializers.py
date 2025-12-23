from rest_framework import serializers
from .models import User, Profile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','role']

    def create(self, data):
        user = User(
            username=data['username'],
            email=data['email'],
            role=data['role']
        )
        user.set_password(data['password'])
        user.save()
        Profile.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
