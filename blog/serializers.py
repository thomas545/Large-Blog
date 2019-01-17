from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url' , 'id' , 'title' , 'content' , 'date_posted' , 'author']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url' , 'id' , 'first_name' , 'last_name' ,'username' , 'email',
                    'is_staff' , 'is_superuser' , 'is_active' , 'last_login','date_joined']
