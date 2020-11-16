from django.urls import path
from book.views import hello, check

urlpatterns = [
	path("check/", check),
	path('', hello)
]