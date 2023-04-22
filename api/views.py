from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import PostIt
from api import serializers
from .serializers import PostItSerializer
from .utils import updatePostIt, getPostItInfo, deletePostIt, getPostIts, createPostIt
# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
       
        {
            'Endpoint': '/postits/',
            'method': 'GET',
            'body': None,
        },
        {
            'Endpoint': '/postits/id',
            'method': 'GET',
            'body': None,
        },
        {
            'Endpoint': '/postits/create/',
            'method': 'POST',
            'body': {'body': ""},
        },
        {
            'Endpoint': '/postits/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
        },
        {
            'Endpoint': '/postits/id/delete/',
            'method': 'DELETE',
            'body': None,
        },
    ]
    return Response(routes)

# Get, Put, and Delete Routes
@api_view(['GET', 'PUT', 'DELETE'])
def getPostIt(request, pk):

    if request.method == 'GET':
        return getPostItInfo(request, pk)

    if request.method == 'PUT':
        return updatePostIt(request, pk)

    if request.method == 'DELETE':
        return deletePostIt(request, pk)
        
# Get and Post Routes
@api_view(['GET', 'POST'])
def getPostIts(request):

    if request.method == 'GET':
        return getPostIts(request)

    if request.method == 'POST':
        return createPostIt(request)

