import time
from celery_radis.celery import app


@app.task()
def summ(x, y):
    time.sleep(7)
    res = x + y
    print(res, 'результат сложения')
    return res