from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):

    @task(1)
    def index(self):
        with open("/scripts/locust.filelist", "r") as listdoc:
             urls = listdoc.read().splitlines()

        for url in urls:
            self.client.get(url)

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
