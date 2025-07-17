from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User

# Serializer for Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Serializer for built-in User model
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")
        return value

def validate_email(self, value):
        if not value.endswith('@gmail.com') and not value.endswith('@yahoo.com'):
            raise serializers.ValidationError("Email must be a valid Gmail or Yahoo address.")
        return value