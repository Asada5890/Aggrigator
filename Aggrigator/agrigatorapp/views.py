from django.shortcuts import render
from agrigatorapp.models import Article

def index(request):
    return render(request, 'index.html', {'articles': Article.objects.all()})
 