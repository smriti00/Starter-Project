from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! Welcome to my Django app.")
