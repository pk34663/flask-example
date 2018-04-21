from subprocess import Process

class runquery:
    def __init__(self,query):
        self._query = query

    def run(self):
        process = Process
