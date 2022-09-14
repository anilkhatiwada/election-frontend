from django.shortcuts import render
from django.views.generic import View
import requests
import json

url = "https://f058-103-163-182-45.in.ngrok.io/api/1/"


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
        return render(request, 'website/galleryimage.html')


class ImageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/image.html')


class VideoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/video.html')


class WhoAmIView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/whoiam.html')


class AgendaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/agenda.html')


class AgendasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/agendas.html')


class DonatonView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/donaton.html')


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
