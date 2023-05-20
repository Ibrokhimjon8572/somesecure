from rest_framework import serializers
from .models import Foydalanuvchi


class GetUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydalanuvchi
        fields = ('isim', 'id')
