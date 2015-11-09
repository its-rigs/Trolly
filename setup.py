'''
Created on 15 Feb 2013

@author: plish
'''

from distutils.core import setup



setup( 
        name = 'Trolly',
        version = '0.2.2',
        author = 'plish',
        author_email = 'plish.development@gmail.com',
        url = 'https://github.com/plish/Trolly',
        packages = ['trolly'],
        license = 'LICENCE.txt',
        install_requires = ['httplib2'],
        description = 'Trello API Wrapper',
        long_description = 'For more detail please see the github page'
    )
