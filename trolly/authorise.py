'''
Created on 8 Nov 2012

@author: plish
'''

from __future__ import print_function

from trolly.client import Client


class Authorise( Client ):
    """
    Class for helping get user auth token.
    """

    def __init__( self, api_key ):
        super( Authorise, self ).__init__( api_key )


    def getAuthorisationUrl( self, application_name, token_expire = '1day' ):
        """
        Returns a URL that needs to be opened in a browser to retrieve an
        access token.
        """
        query_params = {
                'name': application_name,
                'expiration': token_expire,
                'response_type': 'token',
                'scope': 'read,write'
            }

        authorisation_url = self.buildUri(
                path = '/authorize',
                query_params = self.addAuthorisation(query_params)
            )

        print('Please go to the following URL and get the user authorisation token:\n', authorisation_url)
        return authorisation_url


if __name__ == "__main__":

    import sys

    option = ''

    try:
        option = sys.argv[1]
        api_key = sys.argv[2]
        application_name = sys.argv[3]

        if len( sys.argv ) >= 5:
            token_expires = sys.argv[4]

        else:
            token_expires = '1day'

    except:
        pass

    if option in ( '-h', '--h', '-help' ):
        print('\n%s \n\t%s \n\t%s \n\t%s\n\n' % (
                'Use the -a option to get the authorisation URL.',
                'First argument API key.',
                'Second Argument application name',
                'Third argument token expires (optional, default is 1day)'
            ))

    elif option == '-a':
        authorise = Authorise( api_key )
        authorise.getAuthorisationUrl( application_name, token_expires )

    else:
        print("Try running from a terminal using --h for help")











