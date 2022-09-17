from django.shortcuts import render
from django.views.generic import View
import requests
import json

url = "http://127.0.0.1:7000/api/1/"
hosturl = "http://127.0.0.1:7000"


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"home").json()
        return render(request, 'website/index.html', data)


class NewsPageView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"news").json()
        return render(request, 'website/news.html', data)


class BlogsPageView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"blog").json()
        return render(request, 'website/blogs.html', data)


class BlogPageView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"blog/"+str(kwargs["id"])).json()
        return render(request, 'website/blog.html', data)


class ImageGalleryView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"gallery").json()
        return render(request, 'website/gallery.html', data)


class ImageView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"gallery/"+str(kwargs["id"])).json()
        return render(request, 'website/galleryimage.html', data)


class VideoView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"videos").json()
        return render(request, 'website/video.html', data)


class WhoAmIView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"whoami").json()
        return render(request, 'website/whoiam.html', data)


class AgendaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/agenda.html')


class AgendasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/agendas.html')


class DonatonView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"donations").json()
        return render(request, 'website/donaton.html', data)


class EventsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/events.html')


class EventView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/event.html')


class NoticesView(View):
    def get(self, request, *args, **kwargs):
        data = requests.get(
            url+"notices").json()
        return render(request, 'website/notices.html', data)
