from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Peer, Fragment
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json, requests
from json import JSONEncoder, JSONDecoder
from django.urls import reverse
import threading
from threading import Thread


@csrf_exempt
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return


@csrf_exempt
def makeFragments(request):
    context = {
        'username': "phenom",
        'fragment': "123456789987654321"
    }
    peer = Peer.objects.filter()
    address = "http://192.168.43.59:8000/fragmenting/recieveFragment/"
    response = requests.post(address, data=context)
    return HttpResponse(response.content)

@csrf_exempt
def sendFragmentRequest(request):
    context = {
        'username': "phenom",
    }
    peer = Peer.objects.filter()
    address = "http://192.168.43.59:8000/fragmenting/fragmentRequest/"
    response = requests.post(address, data=context)
    return HttpResponse(response.content)


@csrf_exempt
def recieveFragment(request):
    username = request.POST.get('username', None)
    fragment = request.POST.get('fragment', None)
    if fragment is None or username is None:
        return HttpResponse("Incomplete Data")
    else:
        newFragment = Fragment()
        newFragment.createNewFragment(username, fragment)
        newFragment.save()

        return HttpResponse("Success")

@csrf_exempt
def fragmentRequest(request):
    username = request.POST.get('username', None)
    if username is None:
        return HttpResponse("Incomplete Data")
    else:
        fragment = Fragment.objects.filter(username=username) or None
        if fragment is not None:
            return HttpResponse(fragment[0].fragment_data)
        else:
            return HttpResponse("Fragment Not Found!")




