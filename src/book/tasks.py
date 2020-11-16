from celery import shared_task
from time import sleep
from book.models import Table



@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def sleep_task(pause, user_id):
	sleep(pause)
	Table.objects.create(
		result=pause ** 2,
		user_id=user_id)
	return f"hello world {pause}"

@shared_task
def hello():
	return "hello task"