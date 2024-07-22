from time import time


class Status:
    def __init__(self):
        self.start_time = time()
        self.request_count = 0

    def increment_requests(self):
        self.request_count += 1

    def get_status(self):
        return {
            "time_from_start": time() - self.start_time,
            "number_of_requests": self.request_count,
        }
