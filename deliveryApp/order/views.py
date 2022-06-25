from django.http import JsonResponse
from django.shortcuts import render
from order.models import Shop, Menu, Order, OrderFood
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

def shop(request):
    if request.method == 'GET':
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return JsonResponse(serializer.date, safe=False)

    elif request.method == 'POST':