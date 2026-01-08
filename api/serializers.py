from rest_framework import serializers
from django.contrib.auth.models import User
from products.models import Product
from accounts.models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        is_admin = validated_data.pop('is_admin')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, is_admin=is_admin)
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
