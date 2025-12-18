from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def assessments(request):
    return render(request, 'core/assessments.html')

