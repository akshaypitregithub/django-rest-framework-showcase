from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.authentication import CustomAuthentication
from api.models import Person
from api.permissions import ReadOnlyAndAuthenticated
from api.serializers import PersonSerializer


class PersonViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving persons.
    """

    authentication_classes = [CustomAuthentication]
    permission_classes = [ReadOnlyAndAuthenticated]

    def list(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


class PersonModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [ReadOnlyAndAuthenticated]
