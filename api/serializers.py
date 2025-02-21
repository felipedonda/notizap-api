from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Reminder, UserProfile

# User Register Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    # Additional fields for UserProfile
    display_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    timezone = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['display_name', 'email', 'password', 'password2','phone_number', 'timezone']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],  # Using email as username
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        user_profile = UserProfile.objects.create(
            user=user,
            display_name=validated_data['display_name'],
            phone_number=['phone_number'],
            timezone=['timezone']
        )

        return user_profile


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested user object

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'display_name', 'phone_number', 'timezone']

# Reminder Serializer
class ReminderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Store user by ID

    class Meta:
        model = Reminder
        fields = ['id',
                  'title',
                  'description',
                  'scheduled_time',
                  'user',
                  'minutes_prior',
                  'all_day',
                  'remind_daybefore',
                  'is_task',
                  'done',
                  'recurring',
                  'frequency',
                  'frequency_skips',
                  'created_at',
                  'updated_at'
                ]