from django.shortcuts import render
from django.views.generic import View


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/index.html')


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
        return render(request, 'website/notices.html')


class NoticeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'website/notice.html')
