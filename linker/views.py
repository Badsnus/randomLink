import random

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from .models import Links


def index(request, link_name):
    link = get_object_or_404(Links, link_name=link_name)
    link.count_visits += 1
    link.save()
    redirect_link = random.choice(link.links.split(','))
    return redirect(redirect_link)
