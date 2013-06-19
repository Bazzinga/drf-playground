from rest_framework import viewsets
from rest_framework.response import Response

from apitest.serializers import UserSerializer
from apitest.models import MyModel


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyModel.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.queryset.filter(id=1)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
