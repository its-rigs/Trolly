# Trolly

A wrapper around the Trello API. Provides a group of classes to represent Trello Objects. None of the classes cache 
values as they are designed to be inherited and extended to suit the needs of each user. Each class includes a basic 
set of methods based on general use cases. This library was based on work done by 
[sarumont](https://github.com/sarumont/py-trello). Very little was kept from this code, but still props on the initial 
work.


## Getting Started

### Dependencies

This library requires python 2.5 and above.

Before getting stated with this library you will need a few extra things:
- [httplib2](http://code.google.com/p/httplib2/)
- An [API key](https://trello.com/docs/gettingstarted/index.html#getting-an-application-key) for your Trello user
- User authorisation token ( see below for how to obtain )

### Authorisation

#### User Authorisation Token

A user authorisation token isn't too hard to get hold of. There are instruction on how to get one on the 
[Trello](https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user). For those too lazy there is a 
python class in the library called Authorise(). To use this class simply navigate to the file and type:
    
    python authorise.py -a API_KEY APPLICATION_NAME WHEN_TO_EXPIRE

The API key and application names are required but the "WHEN_TO_EXPIRE" will default to 1day if not specified. Running
this file will return a URL. Copy and paste it into your browser and away you go. You might want to store this somewhere
for future use, especially if you have set it to never expire.

#### Oauth

This library (currently) has no Oauth support however the code this was based on includes Oauth support. So for 
inspiration on how to extend the Client class to include this check out the link above.


## Overview

### Trello Client

### Trello Object

### Extending Trello Classes