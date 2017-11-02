from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'It is simmilar to a traditional Django view',
            'Gives you the most control over your logic',
            'It is mapped manualy to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
