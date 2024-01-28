from rest_framework import serializers
from .models import CustomUser 

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=True)
    balance = serializers.DecimalField(max_digits=10 , decimal_places= 2, required=True)
    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate(self, data):
        # Check if a user with the same email already exists
        existing_email_user = CustomUser.objects.filter(email=data['email']).first()
        existing_username_user = CustomUser.objects.filter(username = data['username']).first()
        if existing_email_user:
            raise serializers.ValidationError({'email': 'A user with this email  already exists.'})
        if existing_username_user:
            raise serializers.ValidationError({'email': 'A user with this  username already exists.'})
        if data['balance'] <= 0:
            raise serializers.ValidationError({'error': 'User balance must be greater then zeo'})
        return data
    
    