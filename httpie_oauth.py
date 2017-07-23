"""
OAuth plugin for HTTPie.

"""
import os
from httpie.plugins import AuthPlugin
from requests_oauthlib import OAuth1


__version__ = '1.0.2'
__author__ = 'Jakub Roztocil'
__licence__ = 'BSD'


class OAuth1Plugin(AuthPlugin):

    name = 'OAuth 1.0a 2-legged'
    auth_type = 'oauth1'
    description = ''

    def get_auth(self, username, password):
        client_key = os.environ.get('OAUTH_CLIENT_KEY', None)
        client_secret = os.environ.get('OAUTH_CLIENT_SECRET', None)
        return OAuth1(client_key=client_key, client_secret=client_secret,
                      resource_owner_key=username, resource_owner_secret=password)
