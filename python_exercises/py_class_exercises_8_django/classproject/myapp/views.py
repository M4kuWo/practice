from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Superhero, Creatures
from .serializers import SuperheroSerializer, CreaturesSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as auth_login
from .forms import RegisterForm

# Home page view
def home(request):
    return HttpResponse("Welcome to the homepage!")

def redirect_to_index(request):
    return HttpResponseRedirect('/static/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index_redirect')  # Redirect to a page after registration
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# List all superheroes or create a new superhero
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def superhero_list(request):
    if request.method == 'GET':
        superheroes = Superhero.objects.all()
        serializer = SuperheroSerializer(superheroes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperheroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a specific superhero
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def superhero_detail(request, id):
    try:
        superhero = Superhero.objects.get(id=id)
    except Superhero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SuperheroSerializer(superhero)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperheroSerializer(superhero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        superhero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# List all creatures or create a new creature
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def creatures_list(request):
    if request.method == 'GET':
        creatures = Creatures.objects.all()
        serializer = CreaturesSerializer(creatures, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreaturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a specific creature
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def creatures_detail(request, id):
    try:
        creature = Creatures.objects.get(id=id)
    except Creatures.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CreaturesSerializer(creature)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CreaturesSerializer(creature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        creature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
