import threading
from threading import Thread, Event
import asyncio
import datetime
import time


from utils.local_deps import local_deps
from utils.singleton_exception import SingletonException
local_deps()
import schedule






# not being used
class CronTasksRunner(Thread):
    init= False
    client = None
    task = None
    def __init__(self):
        if(self.init):
            raise SingletonException
        else:
            self.init = True


    async def my_task(self):
        CONFIGS = self.CONFIGS
        while True:
            # replace this with your task code
            CONFIGS.blog_manager.grab_articles(CONFIGS.mysql_manager)
            await asyncio.sleep(24 * 60 * 60)  # wait 24 hours

    async def cron_job_main(self):
        self.task = asyncio.create_task(self.my_task())
        return self.task


    def run_cron_tasks(self,CONFIGS):
        self.CONFIGS = CONFIGS
        asyncio.run(self.cron_job_main())

    def stop_task(self):
        self.task.cancel()


