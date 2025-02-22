
from django.urls import path
from . import views

#localhost:8000/firstapp
#localhost:8000/firstapp/order


urlpatterns = [
path('',views.all_index,name='all_index'),
#path('order/',views.order,name='order'),
              ]