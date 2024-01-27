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
        existing_email_user = CustomUser.objects.filter(email=data['email'] , username = data['username']).first()
        if existing_email_user:
            raise serializers.ValidationError({'email': 'A user with this email or username already exists.'})
        return data
    
    