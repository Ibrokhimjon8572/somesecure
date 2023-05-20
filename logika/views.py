from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import GetUserDetailSerializer
import base64
from .models import Foydalanuvchi


def generate_base64(isim):
    sample_string_bytes = isim.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    # base64_string = base64_bytes.decode("ascii")
    return str(base64_bytes)


class GetTokenForUser(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request: Request):
        print(request.headers)
        t = ""
        if "isim" in request.data:
            basecode = request.data.get("isim")
            t = generate_base64(basecode)
            serializer = GetUserDetailSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
            # user = Foydalanuvchi.objects
            # user["key"] = t
            # print("-"*100, user)
            # user.save()

        return Response({
            "isim": request.data.get("isim"),
            "key": t
        }, status=status.HTTP_200_OK)

# Create your views here.
