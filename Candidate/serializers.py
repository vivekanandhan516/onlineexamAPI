from rest_framework import serializers
from .models import candidate
from django.contrib.auth.models import User




class MainRegisterSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password','candidate')

'''
class RegisterSerializer(serializers.ModelSerializer):
    register = MainRegisterSerializer()

    class Meta:
        model = candidate
        fields = [ 'register','name','mobile']
        user = MainRegisterSerializer()
'''

		
		
		
