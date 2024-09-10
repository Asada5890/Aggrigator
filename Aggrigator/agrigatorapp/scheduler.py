from apscheduler.schedulers.blocking import BlockingScheduler
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aggrigator.settings')
django.setup()

from parser import parser_fun

def start_scheduler():
    sched = BlockingScheduler()
    sched.add_job(parser_fun, 'interval', minutes=1)
    sched.start()

if __name__ == '__main__':
    start_scheduler()