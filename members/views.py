from django.shortcuts import render

# Create your views here.
'''
from rest_framework import viewsets
from .models import Client, Artist, Work
from .serializers import ClientSerializer, ArtistSerializer, WorkSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
'''

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Work, Artist

@api_view(['GET'])
def work_list(request):
    work_type = request.query_params.get('work_type', None)
    artist_name = request.query_params.get('artist', None)
    if work_type is not None:
        works = Work.objects.filter(link_type=work_type)
    elif artist_name is not None:
        artist = get_object_or_404(Artist, name=artist_name)
        works = artist.works.all()
    else:
        works = Work.objects.all()
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@csrf_exempt
def register(request):
    username = request.data.get('testuser')  #username
    password = request.data.get('123123')   #password
    if username is None or password is None:
        return Response({'error': 'Username and password are required.'}, status=400)
    user = User.objects.create_user(username=username, password=password)
    return JsonResponse({'username': user.username})
    
    
def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
  
  
  
