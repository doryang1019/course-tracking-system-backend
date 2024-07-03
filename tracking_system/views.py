from django.http import JsonResponse
from .models import Drink
from .serializers import serializers, DrinkSerializer

def drink_list(request):
  drinks = Drink.objects.all()
  serializer  = DrinkSerializer(drinks, many = True)
  return JsonResponse(serializer.data, safe=False)
