
from rest_framework import serializers
from .models import Earning,Rating

class EarningSerializer(serializers.ModelSerializer):


    class Meta:
        model = Earning
        fields = ('owner','balance')


class RatingSerializer(serializers.ModelSerializer):


    class Meta:
        model = Rating
        fields = ('owner','carcomment')
