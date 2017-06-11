from django.shortcuts import render
from django.utils import timezone
from .models import Rejestracja

def post_list(request):
    posts = Rejestracja.objects.filter(data_wizyty__lte=timezone.now()).order_by('data_wizyty')
    return render(request, 'recepcja/post_list.html', {'posts': posts})
