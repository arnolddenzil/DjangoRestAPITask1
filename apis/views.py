from rest_framework import viewsets

# import local data
from .serializers import SimpleUserSerializer
from .models import SimpleUser


from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


class SimpleUserViewSet(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        users = SimpleUser.objects.all()
        serializer = SimpleUserSerializer(users, many=True)
        return Response({'data': 'login'})

    def post(self, request, format=None):
        print(request.data)
        username = request.data[0]['username']
        password = request.data[0]['password']

        try:
            object = SimpleUser.objects.get(Q(username=username) & Q(password=password))
            print(f"object is {object}------------")

            serializer = SimpleUserSerializer(object)
            return Response({'status': 'success'})

        except SimpleUser.DoesNotExist:
            return Response({'status': 'unsuccessfull'})





