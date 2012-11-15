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

#### User Authorisation

User

#### Oauth

This library (currently) has no Oauth support however the code this was based on includes Oauth support. So for 
inspiration on how to extend the Client class to include this check out the link above.