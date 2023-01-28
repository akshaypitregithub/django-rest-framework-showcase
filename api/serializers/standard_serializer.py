from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Person, LANGUAGE_CHOICES, Employer


class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    height = serializers.CharField(max_length=200)
    occupation = serializers.CharField(max_length=200)
    created = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(max_length=100, default='')
    code = serializers.CharField()
    employed = serializers.BooleanField(default=False)
    employer = serializers.CharField(max_length=200)
    language = serializers.CharField(default='ENGLISH', max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        """
        validated_data["employer"] = Employer.objects.first()
        validated_data["owner"] = User.objects.first()
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Person` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.height = validated_data.get('linenos', instance.height)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance
