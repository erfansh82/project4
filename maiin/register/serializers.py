
from rest_framework import serializers
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True,required=True)

    class Meta:
        model=User
        fields=('first_name','last_name','username','login_id','password','password2')
        extra_kwargs={
            'password':{'write_only':True},
        }
    def create(self,validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)    
    
    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password must match ...')
        return data

