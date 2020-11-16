from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from book.tasks import sleep_task


# @cache_page(2)
def hello(request):
	sleep_task.delay(5, request.user.id)
	return HttpResponse(f"hello world")

def check(request):
	return HttpResponse(f"you have {request.user.tables.count()}")