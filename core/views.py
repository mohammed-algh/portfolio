from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.

class ParkingView(View):
    
    def get(self, request):
        return render(request, 'parking.html')

class PortfolioView(View):

    def get(self, request):
        return HttpResponse("Hello, world. You're at the portfolio index.")