from django.urls import path
from .views import upload_resume

urlpatterns = [
    path('abc', upload_resume, name='upload_resume'),
]

