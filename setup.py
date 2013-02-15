'''
Created on 15 Feb 2013

@author: plish
'''

from distutils.core import setup

setup( 
        name = 'Trolly',
        version = '0.1.0',
        author = 'plish',
        author_email = 'plish.development@gmail.com',
        url = 'https://github.com/plish/Trolly',
        packages = ['trolly'],
        license = 'LICENCE.txt',
        description = 'Trello api',
        long_description = open( 'README.md' ).read()
    )
