
from django.conf.urls import url
from .views import CarView, CarCreate,CarOwnerView, CarOwnerCreate,Earninglist,Ratinglist

urlpatterns = [
    url(r'^$', CarOwnerView.as_view(),name='owner-view'),
    url(r'^car/view/$', CarView.as_view(),name='car-view'),
    url(r'^car/add/$', CarCreate.as_view(),name='car-add'),
    url(r'^owner/add/$', CarOwnerCreate.as_view(),name='owner-add'),
    url(r'^earning/$', Earninglist.as_view(),name='earning'),
    url(r'^rating/$', Ratinglist.as_view(),name='rating')
]