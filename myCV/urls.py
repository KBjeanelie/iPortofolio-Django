from django.urls import path

from myCV.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
