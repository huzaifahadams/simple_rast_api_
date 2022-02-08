from rest_framework.response import Response
from rest_framework.decorators import api_view
from drfapp.models import stuff
from .serializers import stuffSerializer


@api_view(['GET'])
def getData(request):
    stuffs = stuff.objects.all()
    serializer =stuffSerializer(stuffs, many=True)
    #person = {'name': 'Adams', 'age': 45}
    return Response(serializer.data)

@api_view(['POST'])
def addStuff(request):
    serializer = stuffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


