from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterUserSerializer


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)

        if serializer_data.is_valid():
            serializer_data.save()
            response = {
                "status": "User registered successfully",
                "data": serializer_data.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class BlackListTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(data=e, status=status.HTTP_400_BAD_REQUEST)
