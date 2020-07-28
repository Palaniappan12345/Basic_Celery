from celery import Celery
from time import sleep

app = Celery('tasks',broker='pyamqp://guest@localhost//', backend='amqp')
@app.task
def reverse(text):
    sleep(5)
    
    return text[::-1]
