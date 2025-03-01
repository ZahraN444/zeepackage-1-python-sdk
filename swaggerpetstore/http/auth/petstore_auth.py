# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth
from swaggerpetstore.api_helper import APIHelper
from swaggerpetstore.models.o_auth_token import OAuthToken
from apimatic_core.utilities.auth_helper import AuthHelper


class PetstoreAuth(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in PetstoreAuth

        """
        return "PetstoreAuth: OAuthToken is undefined or expired."

    def __init__(self, petstore_auth_credentials, config):
        auth_params = {}
        self._o_auth_client_id = petstore_auth_credentials.o_auth_client_id \
            if petstore_auth_credentials is not None else None
        self._o_auth_redirect_uri = petstore_auth_credentials.o_auth_redirect_uri \
            if petstore_auth_credentials is not None else None
        if petstore_auth_credentials is not None \
                and isinstance(petstore_auth_credentials.o_auth_token, OAuthToken):
            self._o_auth_token = OAuthToken.from_dictionary(
                APIHelper.to_dictionary(petstore_auth_credentials.o_auth_token))
        else:
            self._o_auth_token = petstore_auth_credentials.o_auth_token \
                if petstore_auth_credentials is not None else None
        if petstore_auth_credentials is not None \
                and isinstance(petstore_auth_credentials.o_auth_scopes, list):
            self._o_auth_scopes = petstore_auth_credentials.o_auth_scopes
        else:
            self._o_auth_scopes = None
        self._config = config
        if self._o_auth_token and hasattr(self._o_auth_token, 'access_token'):
            auth_params["Authorization"] = "Bearer {}".format(self._o_auth_token.access_token)
        super().__init__(auth_params=auth_params)

    def is_valid(self):
        return self._o_auth_token and not self.is_token_expired()

    def get_authorization_url(self, state=None, additional_params=None):
        """ Builds and returns an authorization URL. The user is expected to
            obtain an authorization code from this URL and then call the authorize
            function with that authorization code.

        Args:
            state (str): An opaque state string.
            additional_params (dict): Any additional query parameters to be added to the URL.

        Returns:
            str: The authorization URL.

        """
        auth_url = self._config.get_base_uri()
        auth_url += '/authorize'
        query_params = {
            'response_type': 'code',
            'client_id': self._o_auth_client_id,
            'redirect_uri': self._o_auth_client_id
        }
        if self._o_auth_scopes:
            query_params['scope'] = ' '.join(self._o_auth_scopes)
        if state:
            query_params['state'] = state
        if additional_params:
            query_params.update(additional_params)
        auth_url = APIHelper.append_url_with_query_parameters(auth_url, query_params)
        return APIHelper.clean_url(auth_url)

    def is_token_expired(self):
        """ Checks if OAuth token has expired.

        Returns:
            bool: True if OAuth token has expired, False otherwise.

        """
        return hasattr(self._o_auth_token, 'expiry') and AuthHelper.is_token_expired(
            self._o_auth_token.expiry)


class PetstoreAuthCredentials:

    @property
    def o_auth_client_id(self):
        return self._o_auth_client_id

    @property
    def o_auth_redirect_uri(self):
        return self._o_auth_redirect_uri

    @property
    def o_auth_token(self):
        return self._o_auth_token

    @property
    def o_auth_scopes(self):
        return self._o_auth_scopes

    def __init__(self, o_auth_client_id, o_auth_redirect_uri, o_auth_token=None,
                 o_auth_scopes=None):
        if o_auth_client_id is None:
            raise ValueError('o_auth_client_id cannot be None')
        self._o_auth_client_id = o_auth_client_id
        if o_auth_redirect_uri is None:
            raise ValueError('o_auth_redirect_uri cannot be None')
        self._o_auth_redirect_uri = o_auth_redirect_uri
        self._o_auth_token = o_auth_token
        self._o_auth_scopes = o_auth_scopes

    def clone_with(self, o_auth_client_id=None, o_auth_redirect_uri=None,
                   o_auth_token=None, o_auth_scopes=None):
        return PetstoreAuthCredentials(
            o_auth_client_id or self.o_auth_client_id,
            o_auth_redirect_uri or self.o_auth_redirect_uri,
            o_auth_token or self.o_auth_token,
            o_auth_scopes or self.o_auth_scopes)
