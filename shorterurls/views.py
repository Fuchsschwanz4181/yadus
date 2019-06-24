from django.shortcuts import render
from django.shortcuts import redirect
from django.db import IntegrityError
from django.http import HttpResponse
from django.urls import reverse

from .models import StoredUrls
from .forms import ShortForm

import random


def generate(tries):
    length = 5
    length += tries
    dictionary = "ABCDEFGHJKLMNOPRSTUVWXYZabcdefghjkmnoprstuvwxyz1234567890"

    return ''.join(random.choice(dictionary) for _ in range(length))


def makeshorter(link):

    for tries in range(3):
        try:
            short = generate(tries)
            prepared = StoredUrls(full_url=link, short_url=short)
            prepared.save()
            return prepared.short_url

        except IntegrityError:
            continue


# define a function able to redirect you from short to normal link
def makelonger(link):
    try:
        url = StoredUrls.objects.get(short_url__exact=link)
    except StoredUrls.DoesNotExist:
        raise KeyError("invalid shortlink")
    return url.full_url


def index(request):
    form = ShortForm()
    shorten = ''
    if request.method == 'POST':
        form = ShortForm(request.POST)
        if form.is_valid():
            toshort = form.cleaned_data["yoururl"]
            shorten = makeshorter(toshort)
    return render(request, 'shorterurls/base.html', {'form': form, "shorturl": reverse('index') + shorten})


def getfull(request, link):
    try:
        link = makelonger(link)
        return redirect(link)
    except Exception as e:
        return HttpResponse(e.args)
