from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AddProduct


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]

        # what the below lines does is that we are telling django that accept password while creating the user
        # but dont return the password when we are giving the information about the user
        extra_kwargs={"password":{"write_only":True}}

    # THIS IS FUNCTION IS USED TO CREATE A USER

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddProduct
        fields='__all__'

class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddProduct
        fields='__all__'
    
class DeleteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddProduct
        fields='__all__'


        