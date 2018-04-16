

from .serializer import EarningSerializer
from .serializer import RatingSerializer
from rest_framework.views import APIView
from django.views.generic.edit import CreateView
from django.views import generic
from .models import Car,CarOwnerProfile,Earning,Rating
from rest_framework.response import Response




class Earninglist(APIView):

    def get(self,request):
        earings = Earning.objects.all()
        serializer = EarningSerializer(earings,many=True)
        return Response(serializer.data)


class Ratinglist(APIView):
    def get(self,request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings,many=True)
        return Response(serializer.data)



class CarOwnerView(generic.ListView):
    template_name = 'carowner_form.html'
    context_object_name = 'owners'
    def get_queryset(self):
        return CarOwnerProfile.objects.all()

class CarView(generic.ListView):
    template_name = "car_view_form.html"
    context_object_name = 'cars'
    def get_queryset(self):
        return Car.objects.all()


class CarCreate(CreateView):
    model = Car
    fields = [
              'make',
              'body_type',
              'transmission',
              'colour',
              'registration_number',
              'fuel_type',
              'series',
              'seats',
              'comments'
              ]
    template_name = "car_create_form.html"

class CarOwnerCreate(CreateView):
    model = CarOwnerProfile
    fields = [
            'user',
            'name'
           ]
    template_name = "carowner_create_form.html"






