"""
Views for the web app.
"""
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Index page of the web app.
    """
    return render(request, template_name="web/index.html", context={"user_name": "igp!"})
