# middleware.py

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from .settings import DEFAULT_PAGE, PARKING, DEBUG
from django.shortcuts import render



class RedirectToDefaultURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if PARKING and not DEBUG:
            if not request.path.startswith(reverse('parking')) and not request.path.startswith('/admin/'):
                return HttpResponseRedirect(reverse('parking'))
        return self.get_response(request)
        # response = self.get_response(request)
        # # Parking page so if the PARKING is True then it will show the parking page
        # if response.status_code == 404 and not request.path.startswith('/admin/'):
        #     return HttpResponseRedirect(reverse(DEFAULT_PAGE))
        # return self.get_response(request)