from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from fragmenting.models import Peer
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json, requests
from json import JSONEncoder, JSONDecoder
from django.urls import reverse
import threading
from threading import Thread


