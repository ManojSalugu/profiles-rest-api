from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """Test API View"""

  def get(self, request, format=None):
      """Returns list of API features"""
      an_apiview = [
      'Use HTTP methods as function (get, post, patch, delete)',
      'Is similar to traditional django view',
      'Is mapped manually to urls',
      ]

      return Response({'message': 'Hello', 'an_apiview': an_apiview})
