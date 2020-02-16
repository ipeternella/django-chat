"""
Views for the web app.
"""
from django.http import HttpRequest
from django.http import HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    """
    Index page of the web app.
    """
    return HttpResponse("hi", status=200)
