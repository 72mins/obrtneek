from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from obrtneek_app.models import CustomUser
from obrtneek_app.serializers.user import (
    CustomRefreshSerializer,
    CustomTokenPairSerializer,
)


class CustomTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer
    parser_classes = [FormParser, MultiPartParser]

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]

        user = CustomUser.objects.filter(email=email).first()
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )

        if not user:
            return Response(
                "A user with this email does not exist",
                status=status.HTTP_400_BAD_REQUEST,
            )

        elif not user.is_active:
            return Response(
                "This user is not active", status=status.HTTP_400_BAD_REQUEST
            )

        elif not user.check_password(password):
            return Response("Incorrect password", status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class CustomRefreshView(TokenRefreshView):
    serializer_class = CustomRefreshSerializer
    parser_classes = [FormParser, MultiPartParser]
