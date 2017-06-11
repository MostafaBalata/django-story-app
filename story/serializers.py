from django.contrib.auth.models import User
from story.models import Story
from story.models import Upload


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class StorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(required=True)
    image = serializers.CharField(read_only=True)
    upload_id = serializers.IntegerField()
    note = serializers.CharField(required=False)
    location = serializers.CharField(required=True)

    class Meta:
        model = Story
        fields = ('id', 'user_id', 'image','upload_id', 'note', 'location')


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ('id', 'name', 'image')


