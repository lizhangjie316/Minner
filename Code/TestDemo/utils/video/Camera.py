import os

class Camera(object):
    def __init__(self,location,url):
        self.location=location
        self.url=url

    def SetLocation(self,location):
        self.location = location

    def GetLocation(self):
        return self.location

    def SetUrl(self,url):
        self.url = url

    def GetUrl(self):
        return self.url