from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def homepage_view(request):
    return render(request, "home.html")