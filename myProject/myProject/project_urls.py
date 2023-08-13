from django.http import HttpRequest, HttpResponse


def about_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about about ")


def nothing_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about nothing ")


def article_view(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f" about {article} ")


def article_comment_view(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f" about {article} and comment ")


def create_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about create ")


def article_update_view(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f" about {article} and update ")


def article_delete_view(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f" about {article} and delete ")


def topics_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about topics ")


def topics_subscribe_view(request: HttpRequest, topics: str) -> HttpResponse:
    return HttpResponse(f" about topics,{topics} and subscribe ")


def topics_unsubscribe_view(request: HttpRequest, topics: str) -> HttpResponse:
    return HttpResponse(f" about topics,{topics} and unsubscribe ")


def profile_username_view(request: HttpRequest, username: str) -> HttpResponse:
    return HttpResponse(f" about profile,{username}")


def setPassword_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about set-password ")


def setUserdata_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about set-userdata ")


def deactivate_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about deactivate ")


def register_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about register ")


def login_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about login ")


def logout_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f" about logout ")