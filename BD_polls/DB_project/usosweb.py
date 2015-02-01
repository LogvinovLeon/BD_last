"""
UsosWeb OAuth1 backend, docs at:
    NULL
"""
from social.backends.oauth import BaseOAuth1
from social.exceptions import AuthCanceled


class UsosWebOAuth(BaseOAuth1):
    """UsosWeb OAuth authentication backend"""
    name = 'usosweb'
    EXTRA_DATA = [('id', 'id')]
    AUTHORIZATION_URL = 'https://usosapps.uw.edu.pl/services/oauth/authorize'
    REQUEST_TOKEN_URL = 'https://usosapps.uw.edu.pl/services/oauth/request_token'
    ACCESS_TOKEN_URL = 'https://usosapps.uw.edu.pl/services/oauth/access_token'

    def process_error(self, data):
        if 'denied' in data:
            raise AuthCanceled(self)
        else:
            super(UsosWebOAuth, self).process_error(data)

    def get_user_details(self, response):
        """Return user details from Twitter account"""
        fullname, first_name, last_name = self.get_user_names(first_name=response['first_name'],
                                                              last_name=response['last_name'])
        return {'username': fullname,
                'email': '',  # not supplied
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name}

    def user_data(self, access_token, *args, **kwargs):
        """Return user data provided"""
        return self.get_json(
            'https://usosapps.uw.edu.pl/services/users/user',
            auth=self.oauth_auth(access_token)
        )