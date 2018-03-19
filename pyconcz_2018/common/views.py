from django.template.response import TemplateResponse

from pyconcz_2018.programme.models import Speaker


def homepage(request):
    keynoters = Speaker.objects.filter(is_public=True, talks__is_keynote=True,
                                       talks__is_public=True, talks__is_backup=False)

    return TemplateResponse(request, 'pages/homepage.html', {'keynoters': keynoters})
