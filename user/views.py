from django.shortcuts import render, render_to_response
from .models import user
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    if request.method == 'POST':
        e = request.GET.get('email', None)
        p = request.GET.get('password', None)
        try:
            if user.objects.get(email=e).password == p:
                request.session['logged_in'] = user.objects.get(email=e).u_id
                return Response(True)
        except ObjectDoesNotExist:
            pass
    return Response(False)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def logout(request):
    if request.method == 'POST':
        request.session['logged_in'] = None
        return Response(True)
    return Response(False)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    if request.method == 'POST':
        
        return Response("hi")
    
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def find_user(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        objs = user.objects.filter(name__icontains=keyword)
        s = '[ '
        for obj in objs:
            s = s + '{"name":"' + str(obj.name) + '", "u_id":"' + str(obj.u_id) + '"},'
        s=s[:-1] + ']'
        return Response(s)
    return Response('')