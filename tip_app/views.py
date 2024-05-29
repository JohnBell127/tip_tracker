from django.shortcuts import render

# Create your views here.

def add_tip(request):
    return render(request, 'tip_app/add_tip.html')
