from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy


def index(request):
    return render(
        request,
        "pages/page_home.html",
    )

