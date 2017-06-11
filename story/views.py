from django.contrib.auth.models import User
from django.http import Http404

from story.serializers import UserSerializer
from story.serializers import StorySerializer
from story.serializers import UploadSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from story.models import Story
from django.db import IntegrityError


def check_db_error(func):
    def checker(*args):
        try:
            returned_value = func(*args)
        except IntegrityError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return returned_value
    return checker


class UserList(APIView):
    """
    List all users, or create a new user.
    """

    @check_db_error
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @check_db_error
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_db_error
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    @check_db_error
    def _get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @check_db_error
    def get(self, request, pk, format=None):
        user = self._get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    @check_db_error
    def put(self, request, pk, format=None):
        user = self._get_object(pk)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_db_error
    def delete(self, request, pk, format=None):
        user = self._get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StoryList(APIView):
    """
    List all stories, or create a new story.
    """
    @check_db_error
    def get(self, request, format=None):
        query = 'SELECT * FROM `story_story` ' \
                'left join `story_upload` on `story_upload`.id = story_story.upload_id' \
                ' where `story_story`.`user_id`={user_id}'.format(user_id=1)
        data = Story.objects.raw(query)

        serializer = StorySerializer(data , many=True)
        return Response(serializer.data)

    @check_db_error
    def post(self, request, format=None):

        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_db_error
    def delete(self, request, id, format=None):
        story = self.get_object(id)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoList(APIView):
    @check_db_error
    def post(self, request, format=None):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
