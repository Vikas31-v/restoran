from django.shortcuts import render
from .models import Breakfast

def breakfast_view(request):
    # Fetch all breakfast items from the database
    breakfast_items = Breakfast.objects.all()
    
    # Render the breakfast items in the template
    return render(request, 'category.html', {'breakfast_items': breakfast_items})