from django.shortcuts import render

# Create your views here.

def web_view(request):
    return render(request, 'web/index.html', {})