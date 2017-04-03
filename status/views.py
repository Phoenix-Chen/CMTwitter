from django.shortcuts import render, render_to_response
from user.models import user
from user.models import follow
from .models import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import re

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_new_status(request):
    if request.method == 'GET':
        try:
            uid = request.session['logged_in']
            followings = re.findall(r"[\w']+", follow.objects.get(u_id=uid).following)
            s = '[ '
            for f in followings:
                objs = status.objects.filter(author_id=f)
                for obj in objs:
                    if datetime.strptime(obj.time, '%Y-%m-%d %H:%M:%S') > datetime.strptime(request.session['last_update'], '%Y-%m-%d %H:%M:%S'):
                        s = s + '{ "post_id":"' + str(obj.post_id) + '", "author_id":"' + str(obj.author_id) + '", "author_name":"' + obj.author_name + '", "text":"' + obj.text + '", "time":"' + obj.time + '","liked":"'
                        likes = re.findall(r"[\w']+", obj.likes)
                        if str(uid) in likes:
                            s += str(True)
                        else:
                            s += str(False)
                        s = s + '"},'
            s = s[:-1] + ']'
            #request.session['last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")           
            return Response(s)
        except ObjectDoesNotExist:
            pass
    return Response('')