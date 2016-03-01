from functools import update_wrapper
from singledispatch import singledispatch


def singledispatchmethod(method):
    '''
    Enable singledispatch for class methods.

    See http://stackoverflow.com/a/24602374/274318
    '''
    dispatcher = singledispatch(method)
    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)
    wrapper.register = dispatcher.register
    update_wrapper(wrapper, dispatcher)
    return wrapper

