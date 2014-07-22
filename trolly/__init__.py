"""
Created on 8 Nov 2012

@author: plish
"""


class ResourceUnavailable(Exception):
    """
    Exception representing a failed request to a resource
    """

    def __init__(self, message, http_response):
        super(ResourceUnavailable, self).__init__()
        self.message = message
        self.status = http_response.status

    def __str__(self):
        return "Resource unavailable: %s (HTTP status: %s)" % (self.message, self.status)


class Unauthorised(Exception):
    """
    This is raised if you don't have access to the requested object
    """

    def __init__(self, message, http_response):
        super(Unauthorised, self).__init__()
        self.message = message
        self.status = http_response.status

    def __str__(self):
        return "Unauthorised access to resource: %s (HTTP status: %s)" % (self.message, self.status)
