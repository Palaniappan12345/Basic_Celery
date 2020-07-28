from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//',backend = 'amqp')

@app.task
def add(x, y):
    return x + y
