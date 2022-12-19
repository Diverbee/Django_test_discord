from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import roomSerializer

@api_view(['GET'])
def getRoutes(request):
  routes = [
    'GET /api/',
    'GET /api/rooms/',
    'GET /api/rooms/:id/',
  ]
  return Response(routes)



@api_view(['GET'])
def getRoom(request):
  rooms = Room.objects.all()
  serialzer = roomSerializer(rooms, many=True)
  return Response(serialzer.data)