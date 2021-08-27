from django.shortcuts import render
from django.http import HttpResponse
from .models import AssestsConfig


def index(request):
    Images = AssestsConfig.objects.all()
    return render(request, 'dashboard.html', context={'Images': Images})
