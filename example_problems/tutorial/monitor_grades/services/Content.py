import time

class Content(object):
    def __init__(self,  data : str, content : str):
        self.data = data
        self.content = content
        
    def toString(self, sep=' '):
        datestr = time.strftime('%Y-%m-%d %H-%M-%S', self.data)
        return datestr + sep + self.content
