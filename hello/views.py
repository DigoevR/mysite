from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def view_counter(request: HttpRequest) -> HttpResponse:
    view_count: int = request.session.get('view_count', 1)
    request.session['view_count'] = view_count + 1 if view_count < 5 else 1
    response = HttpResponse('view count=' + str(view_count))
    response.set_cookie('dj4e_cookie', '0eaf0f79', max_age=1000)
    return response
