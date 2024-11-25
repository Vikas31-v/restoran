from django.urls import path
from . import views
urlpatterns = [
    path('popular_breakfast/',views.breakfast_view,name='breakfast')



    
]



