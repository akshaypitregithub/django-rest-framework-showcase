from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Person


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
