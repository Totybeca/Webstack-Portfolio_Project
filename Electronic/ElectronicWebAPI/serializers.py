from rest_framework import serializers
from .models import CustomUser

# Create serializers here
class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
