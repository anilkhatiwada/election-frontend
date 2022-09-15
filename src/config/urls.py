
from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home_page"),
    path('gallery', ImageGalleryView.as_view(), name="gallery"),
    path('gallery/<int:id>', ImageView.as_view(), name="image"),
    path('gallery/video', VideoView.as_view(), name="video"),
    path('whoami', WhoAmIView.as_view(), name="whoami"),
    path('agenda', AgendaView.as_view(), name="agenda"),
    path('news', NewsPageView.as_view(), name="news"),
    path('blogs', BlogsPageView.as_view(), name="blogs"),
    path('blog/<int:id>', BlogPageView.as_view()),
    path('agendas', AgendasView.as_view(), name="agendas"),
    path('donation', DonatonView.as_view(), name="donation"),
    path('events', EventsView.as_view(), name="events"),
    path('notices', NoticesView.as_view(), name="notices"),
]
