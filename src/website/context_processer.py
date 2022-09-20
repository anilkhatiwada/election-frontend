from .views import hosturl, url


def urls(request):
    return {
        "hosturl": hosturl,
        "userapiurl": url,
    }
