from django.http import HttpResponse


def index(request):
    return HttpResponse("""
{
    hoge: {
        fuga: piyo,
        hoge2: piyo2
    }
}
""")