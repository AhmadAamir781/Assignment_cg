# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer

class CreateUserView(APIView):
    """
    API view for user registration.
    """
    def post(self, request):
        # Deserialize and validate user data
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the user and return success response
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

        # Return error response if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUserView(APIView):
    """
    API view for retrieving user information.
    """
    def get(self, request, username):
        # Retrieve user from the database
        user = CustomUser.objects.filter(username=username).first()
        if user:
            # Serialize and return user data
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Return error response if user not found
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
