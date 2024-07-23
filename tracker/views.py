from django.shortcuts import redirect, render
from django.http import HttpRequest
from .models import Click


def track_click(request: HttpRequest):
    ip_address = request.META.get("REMOTE_ADDR")
    browser = request.META.get("HTTP_USER_AGENT")

    Click.objects.create(ip_address=ip_address, browser=browser)

    return redirect("tracker:thank_you")


def thank_you(request: HttpRequest):
    return render(request, "tracker/thank_you.html")
