import os

import requests
from django.shortcuts import render, redirect

from .forms import QueryForm

URL = 'https://api.unsplash.com/photos/random?page=1&query={}&orientation=landscape&client_id={}'
CLIENT_ID = os.getenv('CLIENT_ID')


def get_photo_url(query):
    response = requests.get(URL.format(query, CLIENT_ID)).json()
    return response['urls']['full']


def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST or None)
        if form.is_valid():
            query = form.cleaned_data['query']
            return redirect(get_photo_url(query))
    else:
        form = QueryForm()
        return render(request, 'index.html', {'form': form})
