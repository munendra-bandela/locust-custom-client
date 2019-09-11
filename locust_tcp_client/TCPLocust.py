from locust import TaskSet, task, Locust, events
from TCPClient import TCPClient
from StopWatch import timer
import random


class TCPLocust(Locust):
    def __init__(self):
        super(TCPLocust, self).__init__()
        self.client = TCPClient()


class TCPTasks(TaskSet):
    def on_start(self):
        self.client.connect('10.224.89.247', 7564)

    def on_stop(self):
        self.client.disconnect()

    @task
    @timer
    def send_message(self):
        message = self._get_message()
        self.client.send_socket_message(message)
        response = self.client.receive_response()
        if 'MESSAGE_ACK' in response:
            return response
        else:
            raise Exception(response)

    def _get_message(self):
        STARTCHAR = chr(0x02)
        ENDCHAR = chr(0x03)
        message = 'tcp message'
        lpn = random.randint(1, 10)
        print('test' + str(lpn))
        return '%s%s%s' % (STARTCHAR, message % lpn, ENDCHAR)


class Host(TCPLocust):
    task_set = TCPTasks
    min_wait = 10
    max_wait = 20
