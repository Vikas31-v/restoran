from django.urls import path
from . import views
urlpatterns =[
    path('checkout/',views.checkout,name='checkout'),
    path('Proceed_to_payment/',views.Proceed_to_payment,name='Proceed_to_payment')

]