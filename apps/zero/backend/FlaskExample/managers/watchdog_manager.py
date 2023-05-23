import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # os._exit(0)
        None

class WatchdogManager():
    def shutdown_app(self):
        time.sleep(3)
        os._exit(0)
        None
    def __init__(self):
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, '.', recursive=True)
        observer.start()


